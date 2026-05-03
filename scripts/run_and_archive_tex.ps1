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
# compile inside the archive tex folder to keep all artefacts out of the source folder
$archiveTexFile = Join-Path $archiveTex "$texBase.tex"

# -- ensure MiKTeX is on PATH (needed when spawned by VS Code LaTeX Workshop)
$miktexBin = "D:\MiKTeX\miktex\bin\x64"
if ($env:PATH -notlike "*$miktexBin*") {
    $env:PATH = "$miktexBin;$env:PATH"
}

Write-Host ""
Write-Host "Compiling: $texBase (pass 1)..."
Push-Location $archiveTex
try {
    xelatex -interaction=nonstopmode "$archiveTexFile"

    # Run biber after first xelatex pass so biblatex entries are processed
    Write-Host "Running biber for: $texBase ..."
    if (Get-Command biber -ErrorAction SilentlyContinue) {
        biber $texBase
    } elseif (Test-Path (Join-Path $miktexBin 'biber.exe')) {
        & (Join-Path $miktexBin 'biber.exe') $texBase
    } else {
        Write-Host "Warning: biber not found on PATH; bibliography will not be processed."
    }

    Write-Host "Compiling: $texBase (pass 2)..."
    xelatex -interaction=nonstopmode "$archiveTexFile"
}
finally {
    Pop-Location
}

Write-Host ""

# -- copy PDF to results
$pdfOut = Join-Path $archiveTex "$texBase.pdf"
if (Test-Path $pdfOut) {
    Copy-Item $pdfOut $resultsPDF -Force
    Write-Host "PDF -> $resultsPDF"
} else {
    Write-Host "No PDF generated - check compile log for errors"
}

# -- copy HTML to results (if generated)
$htmlOut = Join-Path $archiveTex "$texBase.html"
if (Test-Path $htmlOut) {
    Copy-Item $htmlOut $resultsHTML -Force
    Write-Host "HTML -> $resultsHTML"
}

Write-Host ""
Write-Host "Archive: $archiveBase"
