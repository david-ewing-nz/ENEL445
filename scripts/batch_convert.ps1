# Batch convert all PDFs using Marker
$pdfDir = "d:\github\ENEL445\contents"
$mdOutputDir = "d:\github\ENEL445\reference\notes_new"
$texOutputDir = "d:\github\ENEL445\reference\tex_files"

New-Item -ItemType Directory -Path $mdOutputDir -Force | Out-Null
New-Item -ItemType Directory -Path $texOutputDir -Force | Out-Null

$pdfFiles = Get-ChildItem $pdfDir -Filter "*.pdf" | Sort-Object Name
$total = $pdfFiles.Count

Write-Host "Found $total PDF files to convert" -ForegroundColor Cyan
Write-Host "Output: $mdOutputDir" -ForegroundColor White
Write-Host ""

$i = 0
foreach ($pdf in $pdfFiles) {
    $i++
    Write-Host "[$i/$total] Converting: $($pdf.Name)" -ForegroundColor Cyan
    
    # Step 1: PDF → Markdown using Marker
    Push-Location $mdOutputDir
    & "D:\Python\Scripts\marker_single.exe" $pdf.FullName 2>&1 | Out-Null
    Pop-Location
    
    $mdFile = Join-Path $mdOutputDir "$($pdf.BaseName).md"
    if (Test-Path $mdFile) {
        Write-Host "  ✓ Markdown created" -ForegroundColor Green
        
        # Step 2: Remove PNG references from markdown
        $content = Get-Content -Path $mdFile -Raw
        $content = $content -replace '!\[Page \d+\]\([^\)]+\.png\)\r?\n?', ''
        Set-Content -Path $mdFile -Value $content -NoNewline
        Write-Host "  ✓ PNG references removed" -ForegroundColor Green
        
        # Step 3: Delete PNG files for this document
        $figDir = Join-Path "d:\github\ENEL445\figs" $pdf.BaseName
        if (Test-Path $figDir) {
            Remove-Item -Path $figDir -Recurse -Force
            Write-Host "  ✓ PNG files deleted" -ForegroundColor Green
        }
        
        # Step 4: Markdown → .tex using Pandoc
        $texFile = Join-Path $texOutputDir "$($pdf.BaseName).tex"
        & "C:\Program Files\Pandoc\pandoc.exe" $mdFile -f markdown -t latex --pdf-engine=xelatex -s -o $texFile 2>&1 | Out-Null
        
        if (Test-Path $texFile) {
            Write-Host "  ✓ LaTeX created" -ForegroundColor Green
        } else {
            Write-Host "  ⚠ Pandoc failed" -ForegroundColor Yellow
        }
    } else {
        Write-Host "  ✗ Marker failed" -ForegroundColor Red
    }
    
    Write-Host ""
}

Write-Host "✓ Batch conversion complete!" -ForegroundColor Green
Write-Host "  Markdown files: $mdOutputDir" -ForegroundColor White
Write-Host "  LaTeX files: $texOutputDir" -ForegroundColor White
