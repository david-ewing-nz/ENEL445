# clean_tex_artefacts.ps1
# remove xelatex/pdflatex build artefacts from the repository tree
# excludes: archive/, .venv/, node_modules/
# usage: .\scripts\clean_tex_artefacts.ps1 [-DryRun]

param(
    [switch]$DryRun
)

$repoRoot = Resolve-Path "$PSScriptRoot\.."
$exts     = @("*.aux","*.log","*.toc","*.out","*.synctex.gz","*.fls","*.fdb_latexmk")
$excluded = @('\\archive\\', '\\.venv\\', '\\node_modules\\')

$found = @()
foreach ($ext in $exts) {
    Get-ChildItem -Path $repoRoot -Recurse -Filter $ext -ErrorAction SilentlyContinue |
        Where-Object {
            $path = $_.FullName
            -not ($excluded | Where-Object { $path -match $_ })
        } |
        ForEach-Object { $found += $_ }
}

if ($found.Count -eq 0) {
    Write-Host "No artefacts found."
    exit 0
}

foreach ($f in $found) {
    if ($DryRun) {
        Write-Host "[dry-run] would remove: $($f.FullName)"
    } else {
        Remove-Item $f.FullName -Force
        Write-Host "Removed: $($f.FullName)"
    }
}

Write-Host ""
if ($DryRun) {
    Write-Host "$($found.Count) file(s) would be removed. Re-run without -DryRun to delete."
} else {
    Write-Host "$($found.Count) file(s) removed."
}
