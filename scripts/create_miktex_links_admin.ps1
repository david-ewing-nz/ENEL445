# Create MiKTeX symbolic links (Run as Administrator)

$sourceLocal = "C:\Users\$env:USERNAME\AppData\Local\MiKTeX"
$sourceRoaming = "C:\Users\$env:USERNAME\AppData\Roaming\MiKTeX"
$destLocal = "D:\MiKTeX\LocalData"
$destRoaming = "D:\MiKTeX\RoamingData"

Write-Host "Creating MiKTeX symbolic links..." -ForegroundColor Cyan

# Local link
if (-not (Test-Path $sourceLocal)) {
    New-Item -ItemType SymbolicLink -Path $sourceLocal -Target $destLocal -Force | Out-Null
    Write-Host "✓ Created: $sourceLocal → $destLocal" -ForegroundColor Green
} else {
    Write-Host "⚠ $sourceLocal already exists" -ForegroundColor Yellow
}

# Roaming link
if (-not (Test-Path $sourceRoaming)) {
    New-Item -ItemType SymbolicLink -Path $sourceRoaming -Target $destRoaming -Force | Out-Null
    Write-Host "✓ Created: $sourceRoaming → $destRoaming" -ForegroundColor Green
} else {
    Write-Host "⚠ $sourceRoaming already exists" -ForegroundColor Yellow
}

Write-Host "`n✓ Symbolic links created successfully!" -ForegroundColor Green
Write-Host "MiKTeX will now use D: drive for all data." -ForegroundColor White
