# run_and_archive_tex.ps1
# compile a xelatex file and archive inputs/outputs with a timestamp
# usage: .\run_and_archive_tex.ps1 <path-to-tex-file>

param(
    [Parameter(Mandatory = $true)]
    [string]$TexFilePath
)

# -- resolve paths
$projectRoot = Resolve-Path "$PSScriptRoot\.."
$texFile     = Resolve-Path $TexFilePath
$texDir      = Split-Path $texFile -Parent
$texBase     = [System.IO.Path]::GetFileNameWithoutExtension($texFile)

# -- timestamp
$timestamp = Get-Date -Format "yyyyMMddHHmmss"

# -- archive folders
$archiveBase = Join-Path $projectRoot "archive\$timestamp"
$archiveTex  = Join-Path $archiveBase "tex"
$archiveFigs = Join-Path $archiveBase "figs"

# -- output folders
$resultsPDF  = Join-Path $projectRoot "results\pdf"
$resultsHTML = Join-Path $projectRoot "results\html"

# -- create all folders
foreach ($folder in @($archiveTex, $archiveFigs, $resultsPDF, $resultsHTML)) {
    if (-not (Test-Path $folder)) {
        New-Item -ItemType Directory -Path $folder -Force | Out-Null
        Write-Host "Created: $folder"
    }
}

# -- copy tex file to archive before compilation
Copy-Item $texFile $archiveTex -Force
Write-Host "Archived tex: $texFile -> $archiveTex"

# -- copy root-level figs folder contents to archive
$rootFigs = Join-Path $projectRoot "figs"
if (Test-Path $rootFigs) {
    Copy-Item "$rootFigs\*" $archiveFigs -Recurse -Force
    Write-Host "Archived figs: $rootFigs -> $archiveFigs"
}

# -- also copy a local figs folder adjacent to the tex file (if different from root)
$localFigs = Join-Path $texDir "figs"
if ((Test-Path $localFigs) -and ($localFigs -ne $rootFigs)) {
    Copy-Item "$localFigs\*" $archiveFigs -Recurse -Force
    Write-Host "Archived local figs: $localFigs -> $archiveFigs"
}

# -- compile with xelatex (twice for cross-references and ToC)
Write-Host ""
Write-Host "Compiling: $texBase (pass 1)..."
Push-Location $texDir
try {
    xelatex -interaction=nonstopmode "$texFile"
    Write-Host "Compiling: $texBase (pass 2)..."
    xelatex -interaction=nonstopmode "$texFile"
}
finally {
    Pop-Location
}

Write-Host ""

# -- copy PDF to archive and results
$pdfOut = Join-Path $texDir "$texBase.pdf"
if (Test-Path $pdfOut) {
    Copy-Item $pdfOut $archiveTex  -Force
    Copy-Item $pdfOut $resultsPDF  -Force
    Write-Host "PDF -> $resultsPDF"
} else {
    Write-Host "No PDF generated - check compile log for errors"
}

# -- copy HTML to archive and results (if generated)
$htmlOut = Join-Path $texDir "$texBase.html"
if (Test-Path $htmlOut) {
    Copy-Item $htmlOut $archiveTex  -Force
    Copy-Item $htmlOut $resultsHTML -Force
    Write-Host "HTML -> $resultsHTML"
}

Write-Host ""
Write-Host "Archive: $archiveBase"
