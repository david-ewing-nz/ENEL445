# Check C: drive for moveable items to D: drive

Write-Host "`n=== Checking C: Drive for Moveable Items ===" -ForegroundColor Cyan
Write-Host ""

$results = @()

# 1. Hugging Face cache
Write-Host "Checking Hugging Face cache..." -ForegroundColor Yellow
$hfCache = "C:\Users\$env:USERNAME\.cache\huggingface"
if (Test-Path $hfCache) {
    $size = [math]::Round((Get-ChildItem $hfCache -Recurse -File -ErrorAction SilentlyContinue | Measure-Object -Property Length -Sum).Sum / 1MB, 2)
    $results += [PSCustomObject]@{
        Item = "Hugging Face Models"
        Location = $hfCache
        'Size(MB)' = $size
        Moveable = "Yes - Set HF_HOME env variable"
        Priority = "High"
    }
}

# 2. Pip cache
Write-Host "Checking pip cache..." -ForegroundColor Yellow
$pipCache = "C:\Users\$env:USERNAME\AppData\Local\pip"
if (Test-Path $pipCache) {
    $size = [math]::Round((Get-ChildItem $pipCache -Recurse -File -ErrorAction SilentlyContinue | Measure-Object -Property Length -Sum).Sum / 1MB, 2)
    $results += [PSCustomObject]@{
        Item = "Pip Cache"
        Location = $pipCache
        'Size(MB)' = $size
        Moveable = "Yes - Set PIP_CACHE_DIR"
        Priority = "Medium"
    }
}

# 3. npm cache
Write-Host "Checking npm cache..." -ForegroundColor Yellow
$npmCache = "C:\Users\$env:USERNAME\AppData\Local\npm-cache"
if (Test-Path $npmCache) {
    $size = [math]::Round((Get-ChildItem $npmCache -Recurse -File -ErrorAction SilentlyContinue | Measure-Object -Property Length -Sum).Sum / 1MB, 2)
    $results += [PSCustomObject]@{
        Item = "npm Cache"
        Location = $npmCache
        'Size(MB)' = $size
        Moveable = "Yes - npm config"
        Priority = "Low"
    }
}

# 4. VS Code extensions (if on C:)
Write-Host "Checking VS Code extensions..." -ForegroundColor Yellow
$vscodeExt = "C:\Users\$env:USERNAME\.vscode\extensions"
if (Test-Path $vscodeExt) {
    $size = [math]::Round((Get-ChildItem $vscodeExt -Recurse -File -ErrorAction SilentlyContinue | Measure-Object -Property Length -Sum).Sum / 1MB, 2)
    $results += [PSCustomObject]@{
        Item = "VS Code Extensions"
        Location = $vscodeExt
        'Size(MB)' = $size
        Moveable = "Already on D: (D:\VSCode)"
        Priority = "N/A"
    }
}

# 5. Python packages
Write-Host "Checking Python packages..." -ForegroundColor Yellow
$pythonLocal = "C:\Users\$env:USERNAME\AppData\Local\Programs\Python"
if (Test-Path $pythonLocal) {
    $size = [math]::Round((Get-ChildItem $pythonLocal -Recurse -File -ErrorAction SilentlyContinue | Measure-Object -Property Length -Sum).Sum / 1MB, 2)
    $results += [PSCustomObject]@{
        Item = "Python (Local)"
        Location = $pythonLocal
        'Size(MB)' = $size
        Moveable = "Complex - reinstall recommended"
        Priority = "Low"
    }
}

# 6. Temp folders
Write-Host "Checking Temp folders..." -ForegroundColor Yellow
$temp = "C:\Users\$env:USERNAME\AppData\Local\Temp"
if (Test-Path $temp) {
    $size = [math]::Round((Get-ChildItem $temp -File -ErrorAction SilentlyContinue | Measure-Object -Property Length -Sum).Sum / 1MB, 2)
    $results += [PSCustomObject]@{
        Item = "Temp Files"
        Location = $temp
        'Size(MB)' = $size
        Moveable = "Can delete (not move)"
        Priority = "Medium"
    }
}

# 7. Windows Package Cache
Write-Host "Checking Package Cache..." -ForegroundColor Yellow
$pkgCache = "C:\ProgramData\Package Cache"
if (Test-Path $pkgCache) {
    $size = [math]::Round((Get-ChildItem $pkgCache -Recurse -File -ErrorAction SilentlyContinue | Measure-Object -Property Length -Sum).Sum / 1MB, 2)
    $results += [PSCustomObject]@{
        Item = "Package Cache"
        Location = $pkgCache
        'Size(MB)' = $size
        Moveable = "No - System folder"
        Priority = "N/A"
    }
}

# 8. Check if conda exists
$condaCache = "C:\Users\$env:USERNAME\.conda"
if (Test-Path $condaCache) {
    $size = [math]::Round((Get-ChildItem $condaCache -Recurse -File -ErrorAction SilentlyContinue | Measure-Object -Property Length -Sum).Sum / 1MB, 2)
    $results += [PSCustomObject]@{
        Item = "Conda Cache"
        Location = $condaCache
        'Size(MB)' = $size
        Moveable = "Yes - Set CONDA_PKGS_DIRS"
        Priority = "Medium"
    }
}

Write-Host ""
Write-Host "=== Results ===" -ForegroundColor Cyan
$results | Format-Table -AutoSize

Write-Host ""
Write-Host "=== Summary ===" -ForegroundColor Cyan
$totalMoveable = ($results | Where-Object { $_.Moveable -like "Yes*" } | Measure-Object -Property 'Size(MB)' -Sum).Sum
Write-Host "Total Moveable: $([math]::Round($totalMoveable, 2)) MB" -ForegroundColor Green
Write-Host ""
