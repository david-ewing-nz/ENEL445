# Move all cache and programs to D: drive
# Run this script as Administrator if you encounter permission issues

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "  Moving Cache & Programs to D: Drive" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

$moved = @()
$errors = @()

# ============================================
# 1. Move Pip Cache (370 MB)
# ============================================
Write-Host "[1/4] Moving Pip Cache..." -ForegroundColor Yellow

$pipSource = "C:\Users\$env:USERNAME\AppData\Local\pip"
$pipDest = "D:\Cache\pip"

if (Test-Path $pipSource) {
    try {
        New-Item -ItemType Directory -Path $pipDest -Force | Out-Null
        
        # Move cache files
        $items = Get-ChildItem -Path $pipSource -Recurse -ErrorAction SilentlyContinue
        foreach ($item in $items) {
            $destPath = $item.FullName.Replace($pipSource, $pipDest)
            $destDir = Split-Path -Parent $destPath
            
            if (-not (Test-Path $destDir)) {
                New-Item -ItemType Directory -Path $destDir -Force | Out-Null
            }
            
            if ($item.PSIsContainer -eq $false) {
                Copy-Item -Path $item.FullName -Destination $destPath -Force -ErrorAction SilentlyContinue
            }
        }
        
        # Verify move
        if (Test-Path $pipDest) {
            Remove-Item -Path $pipSource -Recurse -Force -ErrorAction SilentlyContinue
            $moved += "Pip Cache: 370 MB → D:\Cache\pip"
            Write-Host "  ✓ Pip cache moved to D:\Cache\pip" -ForegroundColor Green
        }
    } catch {
        $errors += "Pip Cache: $_"
        Write-Host "  ✗ Failed to move pip cache: $_" -ForegroundColor Red
    }
} else {
    Write-Host "  ⓘ Pip cache not found on C:" -ForegroundColor Gray
}

# ============================================
# 2. Set Hugging Face to D: (before download)
# ============================================
Write-Host "`n[2/4] Configuring Hugging Face Cache..." -ForegroundColor Yellow

$hfDest = "D:\Cache\huggingface"
New-Item -ItemType Directory -Path $hfDest -Force | Out-Null

try {
    [System.Environment]::SetEnvironmentVariable('HF_HOME', $hfDest, 'User')
    [System.Environment]::SetEnvironmentVariable('TRANSFORMERS_CACHE', $hfDest, 'User')
    [System.Environment]::SetEnvironmentVariable('HF_DATASETS_CACHE', $hfDest, 'User')
    $moved += "Hugging Face: Future downloads → $hfDest"
    Write-Host "  ✓ Hugging Face will use D:\Cache\huggingface" -ForegroundColor Green
    
    # Check if any HF cache exists on C: and move it
    $hfSource = "C:\Users\$env:USERNAME\.cache\huggingface"
    if (Test-Path $hfSource) {
        Write-Host "  → Moving existing HF cache to D:..." -ForegroundColor Yellow
        Copy-Item -Path "$hfSource\*" -Destination $hfDest -Recurse -Force -ErrorAction SilentlyContinue
        Remove-Item -Path $hfSource -Recurse -Force -ErrorAction SilentlyContinue
        Write-Host "  ✓ Existing HF cache moved" -ForegroundColor Green
    }
} catch {
    $errors += "Hugging Face: $_"
    Write-Host "  ✗ Failed to set HF environment: $_" -ForegroundColor Red
}

# ============================================
# 3. Set Pip Cache Directory
# ============================================
Write-Host "`n[3/4] Setting Pip Cache Directory..." -ForegroundColor Yellow

try {
    [System.Environment]::SetEnvironmentVariable('PIP_CACHE_DIR', $pipDest, 'User')
    Write-Host "  ✓ Pip will use D:\Cache\pip" -ForegroundColor Green
} catch {
    $errors += "Pip Env Variable: $_"
    Write-Host "  ✗ Failed to set pip environment: $_" -ForegroundColor Red
}

# ============================================
# 4. Clean Temp Files
# ============================================
Write-Host "`n[4/4] Cleaning Temp Files..." -ForegroundColor Yellow

$tempPath = "C:\Users\$env:USERNAME\AppData\Local\Temp"
try {
    $tempSize = [math]::Round((Get-ChildItem -Path $tempPath -File -ErrorAction SilentlyContinue | Measure-Object -Property Length -Sum).Sum / 1MB, 2)
    Remove-Item -Path "$tempPath\*" -Recurse -Force -ErrorAction SilentlyContinue
    $moved += "Temp Files: $tempSize MB deleted"
    Write-Host "  ✓ Cleaned $tempSize MB of temp files" -ForegroundColor Green
} catch {
    Write-Host "  ⚠ Some temp files could not be deleted (in use)" -ForegroundColor Yellow
}

# ============================================
# Summary
# ============================================
Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "  Summary" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

if ($moved.Count -gt 0) {
    Write-Host "✓ Successfully moved/configured:" -ForegroundColor Green
    foreach ($item in $moved) {
        Write-Host "  • $item" -ForegroundColor White
    }
}

if ($errors.Count -gt 0) {
    Write-Host "`n✗ Errors encountered:" -ForegroundColor Red
    foreach ($error in $errors) {
        Write-Host "  • $error" -ForegroundColor White
    }
}

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "Environment Variables Set (User Level):" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  PIP_CACHE_DIR = D:\Cache\pip" -ForegroundColor White
Write-Host "  HF_HOME = D:\Cache\huggingface" -ForegroundColor White
Write-Host "  TRANSFORMERS_CACHE = D:\Cache\huggingface" -ForegroundColor White
Write-Host "  HF_DATASETS_CACHE = D:\Cache\huggingface" -ForegroundColor White

Write-Host "`n⚠ IMPORTANT: Restart PowerShell for environment variables to take effect!" -ForegroundColor Yellow
Write-Host ""
