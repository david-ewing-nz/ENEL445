# Convert only BASE PDFs (no -1, -2, etc. duplicates)
$pdfDir = "d:\github\ENEL445\contents"
$mdOutputDir = "d:\github\ENEL445\reference\notes_new"
$texOutputDir = "d:\github\ENEL445\reference\tex_files"

New-Item -ItemType Directory -Path $mdOutputDir -Force | Out-Null
New-Item -ItemType Directory -Path $texOutputDir -Force | Out-Null

# Get only base PDFs (exclude -1, -2, etc.)
$pdfFiles = Get-ChildItem $pdfDir -Filter "*.pdf" | 
            Where-Object { $_.Name -notmatch '-\d+\.pdf$' } |
            Sort-Object Name

$total = $pdfFiles.Count

Write-Host "Found $total BASE PDF files to convert (excluding duplicates)" -ForegroundColor Cyan
Write-Host "Output: $mdOutputDir" -ForegroundColor White
Write-Host ""

$i = 0
$converted = 0
$failed = 0
$skipped = 0

foreach ($pdf in $pdfFiles) {
    $i++
    
    # Skip if already converted
    $mdFile = Join-Path $mdOutputDir "$($pdf.BaseName).md"
    if (Test-Path $mdFile) {
        Write-Host "[$i/$total] Already converted: $($pdf.Name)" -ForegroundColor Gray
        $skipped++
        continue
    }
    
    Write-Host "[$i/$total] Converting: $($pdf.Name)" -ForegroundColor Cyan
    
    try {
        # PDF → Markdown using Marker
        Push-Location $mdOutputDir
        $null = & "D:\Python\Scripts\marker_single.exe" $pdf.FullName 2>&1
        Pop-Location
        
        if (Test-Path $mdFile) {
            Write-Host "  ✓ Markdown created" -ForegroundColor Green
            
            # Remove PNG references
            $content = Get-Content -Path $mdFile -Raw
            $content = $content -replace '!\[Page \d+\]\([^\)]+\.png\)\r?\n?', ''
            Set-Content -Path $mdFile -Value $content -NoNewline
            Write-Host "  ✓ PNG references removed" -ForegroundColor Green
            
            # Delete PNG files
            $figDir = Join-Path "d:\github\ENEL445\figs" $pdf.BaseName
            if (Test-Path $figDir) {
                Remove-Item -Path $figDir -Recurse -Force
                Write-Host "  ✓ PNG files deleted" -ForegroundColor Green
            }
            
            $converted++
        } else {
            Write-Host "  ✗ Conversion failed" -ForegroundColor Yellow
            $failed++
        }
    } catch {
        Write-Host "  ✗ Error: $_" -ForegroundColor Red
        $failed++
    }
    
    Write-Host ""
}

Write-Host "`n=== Conversion Summary ===" -ForegroundColor Cyan
Write-Host "Total BASE PDFs:  $total" -ForegroundColor White
Write-Host "Converted:        $converted" -ForegroundColor Green
Write-Host "Skipped:          $skipped" -ForegroundColor Gray
Write-Host "Failed:           $failed" -ForegroundColor Red
