# 📂 (Same folder as the script)
# ├── UC-course-class-contents.zip               # ZIP archive from Learn
# │     └── <random-folder-name>                 # additional layer!!
# │            │ 
# │            ├── <random-folder-name1>        # expected folder
# │            │     └── content                # Target folder for PDFs        
# │            │           └── <filename1-pdf>  # PDFs    
# │            │ 
# │            ├── <random-folder-name2>        # expected folder
# │            .      └── content               # Target folder for PDFs        
# │            .          └── <filename2-pdf>   # PDFs 
# │            .   
# │            └─(other similar folders)
# │ 
# ├── contents
# │    └── contents                             # Target folder for PDFs
# └── capture-course-pdfs-from-zip-RELATIVE.ps1

[CmdletBinding(SupportsShouldProcess = $true)]
param(
    [Alias('--dryrun')]
    [switch]$dryrun
)

# Validate parameters
if ($args.Count -gt 0) {
    Write-Host "Wrong option: $($args -join ', ')"
    exit 1
}

# --- BASE DIRECTORY ---
$scriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Path

# --- RELATIVE PATHS ---
$zipPath         = Join-Path $scriptRoot "ENEL445-26S1_1771808777.zip"
$extractRoot     = Join-Path $scriptRoot "_unzipped"
$destinationRoot = Join-Path $scriptRoot "contents"

# --- Ensure ZIP file is available locally (downloaded from OneDrive) ---
try {
    [void](Get-Item $zipPath).Length
} catch {
    Write-Error "Zip file is not available locally. Make sure it's downloaded from OneDrive."
    exit 1
}

# --- Ensure extract and destination directories exist ---
if (-not (Test-Path -Path $extractRoot)) {
    Write-Host "[Info] Creating extract folder: $extractRoot (even in dry run mode)"
    New-Item -Path $extractRoot -ItemType Directory -Force | Out-Null
}

if (-not (Test-Path -Path $destinationRoot)) {
    Write-Host "[Info] Creating destination folder: $destinationRoot (even in dry run mode)"
    New-Item -Path $destinationRoot -ItemType Directory -Force | Out-Null
}

# --- List PDF files in the zip if in dry run mode ---
if ($dryrun) {
    Write-Host "`n[Dry Run] Listing all PDF files inside the zip archive:`n"
    Add-Type -AssemblyName System.IO.Compression.FileSystem
    $zip = [System.IO.Compression.ZipFile]::OpenRead($zipPath)

    $pdfs = $zip.Entries | Where-Object { $_.FullName -match '/content/[^/]+$' }
    if ($pdfs.Count -eq 0) {
        Write-Host "  No PDF files found in the archive."
    } else {
        $pdfs | ForEach-Object {
            Write-Host "  $($_.FullName)"
        }
    }

    $zip.Dispose()
    Write-Host "`n[Dry Run] No extraction or copying performed."
    exit 0
}

# --- Expand the archive ---
Expand-Archive -Path $zipPath -DestinationPath $extractRoot -Force

# --- Locate the inner top-level folder created by zip ---
$topFolder = Get-ChildItem -Path $extractRoot -Directory | Select-Object -First 1
if (-not $topFolder) {
    Write-Error "Could not find top-level folder inside extracted zip."
    exit 1
}

# --- Process folders named 'content' and copy all file types ---
Get-ChildItem -Path $topFolder.FullName -Recurse -Directory |
Where-Object { $_.Name -eq "content" } |
ForEach-Object {
    Get-ChildItem -Path $_.FullName -File |
    ForEach-Object {
        $baseName = $_.BaseName
        $extension = $_.Extension

        $existingFiles = @(Get-ChildItem -Path $destinationRoot -File |
            Where-Object { $_.BaseName -match "^$([regex]::Escape($baseName))(?:-(\d+))?$" })

        $nextNumber = if ($existingFiles.Count -gt 0) {
            ($existingFiles | ForEach-Object {
                if ($_.BaseName -match "-(\d+)$") { [int]$matches[1] }
                else { 0 }
            } | Measure-Object -Maximum).Maximum + 1
        } else { $null }

        $newName = if ($nextNumber -ne $null) {
            "${baseName}-${nextNumber}${extension}"
        } else {
            "${baseName}${extension}"
        }

        $newPath = Join-Path -Path $destinationRoot -ChildPath $newName
        Copy-Item -Path $_.FullName -Destination $newPath -Force
    }
}
