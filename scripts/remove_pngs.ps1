# Remove PNG references from markdown files and delete PNG files
$mdDir = "d:\github\ENEL445\reference\notes_new"
$figsDir = "d:\github\ENEL445\figs"

Write-Host "Removing PNG references from markdown files..." -ForegroundColor Cyan

# Process each markdown file
Get-ChildItem -Path $mdDir -Filter "*.md" | ForEach-Object {
    $file = $_.FullName
    Write-Host "Processing: $($_.Name)" -ForegroundColor Yellow
    
    # Read content
    $content = Get-Content -Path $file -Raw
    
    # Remove lines with PNG references (lines like: ![Page 1](../../figs/.../page_001.png))
    $newContent = $content -replace '!\[Page \d+\]\([^\)]+\.png\)\r?\n?', ''
    
    # Write back
    Set-Content -Path $file -Value $newContent -NoNewline
    
    Write-Host "  ✓ PNG references removed" -ForegroundColor Green
}

Write-Host "`nDeleting PNG files from figs directory..." -ForegroundColor Cyan

# Count PNG files before deletion
$pngCount = (Get-ChildItem -Path $figsDir -Filter "*.png" -Recurse).Count
Write-Host "Found $pngCount PNG files" -ForegroundColor White

# Delete all PNG files
Get-ChildItem -Path $figsDir -Filter "*.png" -Recurse | ForEach-Object {
    Remove-Item -Path $_.FullName -Force
}

Write-Host "✓ All PNG files deleted" -ForegroundColor Green
Write-Host "✓ Cleanup complete!" -ForegroundColor Green
