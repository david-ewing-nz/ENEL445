# Batch convert all PDFs using Marker - DEBUG VERSION
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
$converted = 0
$failed = 0

foreach ($pdf in $pdfFiles) {
    $i++
    
    # Skip if already converted
    $mdFile = Join-Path $mdOutputDir "$($pdf.BaseName).md"
    if (Test-Path $mdFile) {
        Write-Host "[$i/$total] Skipping (already exists): $($pdf.Name)" -ForegroundColor Gray
        $converted++
        continue
    }
    
    Write-Host "[$i/$total] Converting: $($pdf.Name)" -ForegroundColor Cyan
    
    try {
        # Step 1: PDF → Markdown using Marker (with timeout and error handling)
        Push-Location $mdOutputDir
        
        # Run Marker with error catching
        $process = Start-Process -FilePath "D:\Python\Scripts\marker_single.exe" `
                                  -ArgumentList "`"$($pdf.FullName)`"" `
                                  -NoNewWindow -Wait -PassThru `
                                  -RedirectStandardError "$env:TEMP\marker_error.txt" `
                                  -RedirectStandardOutput "$env:TEMP\marker_output.txt"
        
        Pop-Location
        
        if ($process.ExitCode -ne 0) {
            Write-Host "  ✗ Marker crashed (exit code: $($process.ExitCode)) - Skipping" -ForegroundColor Yellow
            $failed++
            continue
        }
        
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
            
            $converted++
        } else {
            Write-Host "  ✗ Markdown file not created" -ForegroundColor Red
            $failed++
        }
    } catch {
        Write-Host "  ✗ Error: $_" -ForegroundColor Red
        $failed++
    }
    
    Write-Host ""
}

Write-Host "`n=== Conversion Summary ===" -ForegroundColor Cyan
Write-Host "Total PDFs:     $total" -ForegroundColor White
Write-Host "Converted:      $converted" -ForegroundColor Green
Write-Host "Failed:         $failed" -ForegroundColor Red
Write-Host "Remaining:      $($total - $converted - $failed)" -ForegroundColor Yellow
