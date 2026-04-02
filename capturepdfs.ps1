
[CmdletBinding(SupportsShouldProcess = $true)]
param(
    [Parameter(Mandatory = $true, Position = 0)]
    [string]$zipfile,
    [Alias('--dryrun')]
    [switch]$dryrun
)

# Resolve script directory
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition

# Resolve zipfile path relative to execution directory
$zipPath = Join-Path -Path (Get-Location) -ChildPath $zipfile

# Destination 'contents' folder relative to script location
$destinationRoot = Join-Path -Path $scriptDir -ChildPath 'contents'
if (!(Test-Path $destinationRoot)) {
    New-Item -Path $destinationRoot -ItemType Directory | Out-Null
}

if (!(Test-Path $zipPath)) {
    Write-Host "Zip file not found: $zipPath"
    exit 1
}

if ($dryrun) {
    try {
        Add-Type -AssemblyName System.IO.Compression.FileSystem
        $zip = [System.IO.Compression.ZipFile]::OpenRead($zipPath)
        $pdfFiles = $zip.Entries | Where-Object { $_.Name -match '\.pdf$' -and $_.Length -gt 0 }
        if ($pdfFiles.Count -eq 0) {
            Write-Host "[Dry Run] No PDF files found in the zip archive."
        } else {
            Write-Host "[Dry Run] PDF files that would be extracted:"
            foreach ($entry in $pdfFiles) {
                Write-Host "  $($entry.Name)"
            }
        }
        $zip.Dispose()
        Write-Host "---"
        Write-Host "Dry run completed. No files were actually extracted."
    } catch {
        Write-Host "Failed to read zip: $_"
        exit 1
    }
} else {
    try {
        Add-Type -AssemblyName System.IO.Compression.FileSystem
        $zip = [System.IO.Compression.ZipFile]::OpenRead($zipPath)
        $pdfFiles = $zip.Entries | Where-Object { $_.Name -match '\.pdf$' -and $_.Length -gt 0 }
        if ($pdfFiles.Count -eq 0) {
            Write-Host "No PDF files found in the zip archive."
        } else {
            foreach ($entry in $pdfFiles) {
                $baseName = [System.IO.Path]::GetFileNameWithoutExtension($entry.Name)
                $extension = [System.IO.Path]::GetExtension($entry.Name)
                $destFile = Join-Path $destinationRoot $entry.Name
                $counter = 1
                while (Test-Path $destFile) {
                    $destFile = Join-Path $destinationRoot ("{0}-{1}{2}" -f $baseName, $counter, $extension)
                    $counter++
                }
                $fileStream = [System.IO.File]::Open($destFile, [System.IO.FileMode]::CreateNew)
                $entry.Open().CopyTo($fileStream)
                $fileStream.Close()
                Write-Host "Extracted: $($entry.FullName) -> $destFile"
            }
        }
        $zip.Dispose()
        Write-Host "All PDF files extracted to $destinationRoot (flat, no subfolders)."
    } catch {
        Write-Host "Failed to extract zip: $_"
        exit 1
    }
}
