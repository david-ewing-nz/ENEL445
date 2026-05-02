#Requires -Version 5.1
<#
.SYNOPSIS
    Hourly mechanical snapshot writer for README-WHEN-YOU-RETURN.md.
    Skips execution if the machine has been idle for more than 10 minutes.
.DESCRIPTION
    Writes a snapshot of the project state (timestamp, git log, file counts,
    recently modified files) to README-WHEN-YOU-RETURN.md.
    Run hourly via Windows Task Scheduler.
#>

param(
    [string]$RepoRoot = 'D:\github\ENEL445',
    [int]$IdleThresholdMinutes = 10
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

# ---------------------------------------------------------------------------
# Idle-time detection via Win32 GetLastInputInfo
# ---------------------------------------------------------------------------
$getLastInputSrc = @'
using System;
using System.Runtime.InteropServices;

public class IdleTimer {
    [StructLayout(LayoutKind.Sequential)]
    private struct LASTINPUTINFO {
        public uint cbSize;
        public uint dwTime;
    }

    [DllImport("user32.dll")]
    private static extern bool GetLastInputInfo(ref LASTINPUTINFO plii);

    public static TimeSpan GetIdleTime() {
        var info = new LASTINPUTINFO();
        info.cbSize = (uint)Marshal.SizeOf(info);
        GetLastInputInfo(ref info);
        uint idleMs = (uint)Environment.TickCount - info.dwTime;
        return TimeSpan.FromMilliseconds(idleMs);
    }
}
'@

if (-not ([System.Management.Automation.PSTypeName]'IdleTimer').Type) {
    Add-Type -TypeDefinition $getLastInputSrc -Language CSharp
}

$idleTime = [IdleTimer]::GetIdleTime()
if ($idleTime.TotalMinutes -gt $IdleThresholdMinutes) {
    Write-Host "Machine idle for $([int]$idleTime.TotalMinutes) minutes — skipping README update."
    exit 0
}

# ---------------------------------------------------------------------------
# Gather project state
# ---------------------------------------------------------------------------
Push-Location $RepoRoot

$timestamp = Get-Date -Format 'yyyy-MM-dd HH:mm:ss'

# Last git commit
$gitHash    = git rev-parse --short HEAD 2>$null
$gitMessage = git log -1 --pretty=format:"%s" 2>$null
$gitDate    = git log -1 --pretty=format:"%ci" 2>$null

# File counts
$countPython   = (Get-ChildItem -Path 'python'   -Filter '*.py'     -ErrorAction SilentlyContinue).Count
$countArchive  = (Get-ChildItem -Path 'archive'  -Directory         -ErrorAction SilentlyContinue).Count
$countResults  = (Get-ChildItem -Path 'results'  -File -Recurse     -ErrorAction SilentlyContinue).Count
$countContents = (Get-ChildItem -Path 'contents' -Filter '*.pdf'    -ErrorAction SilentlyContinue).Count

# Recently modified files (last 24 hours, excluding archive/ and .git/)
$cutoff = (Get-Date).AddHours(-24)
$recentFiles = Get-ChildItem -Path $RepoRoot -File -Recurse -ErrorAction SilentlyContinue |
    Where-Object {
        $_.LastWriteTime -gt $cutoff -and
        $_.FullName -notmatch '\\\.git\\' -and
        $_.FullName -notmatch '\\archive\\'
    } |
    Sort-Object LastWriteTime -Descending |
    Select-Object -First 15 |
    ForEach-Object {
        $rel = $_.FullName.Replace($RepoRoot + '\', '')
        "- $($_.LastWriteTime.ToString('HH:mm:ss'))  $rel"
    }

$recentBlock = if ($recentFiles) { $recentFiles -join "`n" } else { '- (none in past 24 hours)' }

Pop-Location

# ---------------------------------------------------------------------------
# Write README
# ---------------------------------------------------------------------------
$content = @"
# ENEL445 — When You Return

*Auto-updated: $timestamp (idle at write: $([int]$idleTime.TotalMinutes) min)*

---

## Project Overview

**Course**: ENEL445 Applied Engineering Optimisation  
**Student**: David Ewing (82171165)  
**Project**: Gradient-Based Optimisation for Variational Inference  
— CAVI baseline + Gibbs MCMC gold standard; applying course methods (gradient descent, Nelder-Mead, GA, etc.) to maximise the ELBO.

**Deliverables**:
- Oral presentation — Week 11
- Final report — Week 12

---

## Git Status

| Property | Value |
|----------|-------|
| Last commit | ``$gitHash`` |
| Message | $gitMessage |
| Date | $gitDate |

---

## File Counts

| Folder | Count |
|--------|-------|
| python/ .py files | $countPython |
| archive/ runs | $countArchive |
| results/ files | $countResults |
| contents/ PDFs | $countContents |

---

## Recently Modified (past 24 h)

$recentBlock

---

## Key Files

| Purpose | Path |
|---------|------|
| Main LaTeX report | ``results/vi_optimisation_solution.tex`` |
| CAVI + Gibbs impl. | ``python/vb_algorithms_py.py`` |
| Utilities (archive, plot, I/O) | ``python/vb_utils_py.py`` |
| Copilot instructions | ``.github/copilot-instructions.md`` |

---

## Notes

- Python environment: ``D:\Python`` (numpy, scipy, polars, matplotlib). No venv.
- LaTeX compiler: ``xelatex``. MiKTeX at ``D:\MiKTeX``.
- Run this script manually: ``pwsh -File D:\github\ENEL445\scripts\Update-Readme.ps1``
- To schedule hourly: see ``scripts\Schedule-ReadmeUpdater.ps1``
"@

Set-Content -Path (Join-Path $RepoRoot 'README-WHEN-YOU-RETURN.md') -Value $content -Encoding UTF8
Write-Host "README updated at $timestamp"
