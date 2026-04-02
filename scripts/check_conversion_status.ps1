# Check PDF to MD conversion status
$pdfCount = (Get-ChildItem "d:\github\ENEL445\contents" -Filter "*.pdf").Count
$mdCount = (Get-ChildItem "d:\github\ENEL445\reference\notes_new" -Filter "*.md" | Where-Object { $_.Name -ne "QUALITY_REPORT.md" }).Count

Write-Host "`n=== Conversion Status ===" -ForegroundColor Cyan
Write-Host "PDFs in contents/:     $pdfCount" -ForegroundColor White
Write-Host "MDs created:           $mdCount" -ForegroundColor Green
Write-Host "Remaining:             $($pdfCount - $mdCount)" -ForegroundColor Yellow

$percentComplete = [math]::Round(($mdCount / $pdfCount) * 100, 1)
Write-Host "Progress:              $percentComplete%" -ForegroundColor Cyan

if ($mdCount -eq $pdfCount) {
    Write-Host "`n✓ CONVERSION COMPLETE!" -ForegroundColor Green
} else {
    Write-Host "`n⏳ Conversion in progress..." -ForegroundColor Yellow
}
Write-Host ""
