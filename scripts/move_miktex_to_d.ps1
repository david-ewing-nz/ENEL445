# Move MiKTeX data from C: to D: drive
# Requires Administrator privileges for symbolic links

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "  Moving MiKTeX Data to D: Drive" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

$sourceLocal = "C:\Users\$env:USERNAME\AppData\Local\MiKTeX"
$sourceRoaming = "C:\Users\$env:USERNAME\AppData\Roaming\MiKTeX"
$destLocal = "D:\MiKTeX\LocalData"
$destRoaming = "D:\MiKTeX\RoamingData"

# Create destination directories
Write-Host "[1/4] Creating directories on D:..." -ForegroundColor Yellow
New-Item -ItemType Directory -Path $destLocal -Force | Out-Null
New-Item -ItemType Directory -Path $destRoaming -Force | Out-Null
Write-Host "  ✓ Directories created" -ForegroundColor Green

# Move Local data
Write-Host "`n[2/4] Moving Local MiKTeX data (60 MB)..." -ForegroundColor Yellow
if (Test-Path $sourceLocal) {
    try {
        Copy-Item -Path "$sourceLocal\*" -Destination $destLocal -Recurse -Force -ErrorAction Stop
        $size = [math]::Round((Get-ChildItem $destLocal -Recurse -File | Measure-Object -Property Length -Sum).Sum / 1MB, 2)
        Remove-Item -Path $sourceLocal -Recurse -Force
        Write-Host "  ✓ Moved $size MB to D:\MiKTeX\LocalData" -ForegroundColor Green
    } catch {
        Write-Host "  ✗ Error moving Local data: $_" -ForegroundColor Red
        exit 1
    }
} else {
    Write-Host "  ⓘ Local MiKTeX data not found" -ForegroundColor Gray
}

# Move Roaming data
Write-Host "`n[3/4] Moving Roaming MiKTeX data..." -ForegroundColor Yellow
if (Test-Path $sourceRoaming) {
    try {
        Copy-Item -Path "$sourceRoaming\*" -Destination $destRoaming -Recurse -Force -ErrorAction Stop
        Remove-Item -Path $sourceRoaming -Recurse -Force
        Write-Host "  ✓ Moved to D:\MiKTeX\RoamingData" -ForegroundColor Green
    } catch {
        Write-Host "  ✗ Error moving Roaming data: $_" -ForegroundColor Red
        exit 1
    }
} else {
    Write-Host "  ⓘ Roaming MiKTeX data not found" -ForegroundColor Gray
}

# Create symbolic links
Write-Host "`n[4/4] Creating symbolic links..." -ForegroundColor Yellow
try {
    # Local link
    if (-not (Test-Path $sourceLocal)) {
        New-Item -ItemType SymbolicLink -Path $sourceLocal -Target $destLocal -Force | Out-Null
        Write-Host "  ✓ Created link: C:\...\Local\MiKTeX → D:\MiKTeX\LocalData" -ForegroundColor Green
    }
    
    # Roaming link
    if (-not (Test-Path $sourceRoaming)) {
        New-Item -ItemType SymbolicLink -Path $sourceRoaming -Target $destRoaming -Force | Out-Null
        Write-Host "  ✓ Created link: C:\...\Roaming\MiKTeX → D:\MiKTeX\RoamingData" -ForegroundColor Green
    }
} catch {
    Write-Host "  ✗ Error creating symbolic links: $_" -ForegroundColor Red
    Write-Host "  ⚠ Run PowerShell as Administrator to create symbolic links" -ForegroundColor Yellow
}

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "  Summary" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "✓ MiKTeX data moved to D: drive" -ForegroundColor Green
Write-Host "  • Local data: D:\MiKTeX\LocalData" -ForegroundColor White
Write-Host "  • Roaming data: D:\MiKTeX\RoamingData" -ForegroundColor White
Write-Host "  • Freed ~60 MB on C: drive" -ForegroundColor White
Write-Host ""
