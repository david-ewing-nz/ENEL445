# Quick status check for PDF conversion
Write-Host "`n=== ENEL445 PDF Conversion Status ===" -ForegroundColor Cyan
Write-Host "Date: $(Get-Date)" -ForegroundColor White

# Check processes
$batch = Get-Process powershell -ErrorAction SilentlyContinue | Where-Object { $_.Id -eq 28248 }
$monitor = Get-Process powershell -ErrorAction SilentlyContinue | Where-Object { $_.Id -eq 28864 }

Write-Host "`nProcesses:" -ForegroundColor Yellow
if ($batch) { 
    Write-Host "  ✓ Batch conversion: RUNNING (CPU: $([math]::Round($batch.CPU, 1))s)" -ForegroundColor Green 
} else { 
    Write-Host "  ✗ Batch conversion: STOPPED" -ForegroundColor Red 
}
if ($monitor) { 
    Write-Host "  ✓ Auto-replacer: RUNNING" -ForegroundColor Green 
} else { 
    Write-Host "  ✗ Auto-replacer: STOPPED" -ForegroundColor Red 
}

# Check output
Write-Host "`nOutput:" -ForegroundColor Yellow
$mdNew = (Get-ChildItem "d:\github\ENEL445\reference\notes_new" -Filter "*.md" -ErrorAction SilentlyContinue).Count
$tex = (Get-ChildItem "d:\github\ENEL445\reference\tex_files" -Filter "*.tex" -ErrorAction SilentlyContinue).Count
$notesReplaced = (Get-ChildItem "d:\github\ENEL445\reference\notes" -Filter "*.md" | Where-Object { $_.LastWriteTime -gt (Get-Date).AddHours(-24) }).Count

Write-Host "  Markdown (new): $mdNew / 44" -ForegroundColor White
Write-Host "  LaTeX files: $tex / 44" -ForegroundColor White
Write-Host "  Notes replaced: $notesReplaced" -ForegroundColor White

# Check log
if (Test-Path "d:\github\ENEL445\conversion_log.txt") {
    Write-Host "`nRecent activity:" -ForegroundColor Yellow
    Get-Content "d:\github\ENEL445\conversion_log.txt" -Tail 10
}

Write-Host ""
