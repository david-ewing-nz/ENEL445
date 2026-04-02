# Auto-replace notes as conversions complete
$sourceDir = "d:\github\ENEL445\reference\notes_new"
$targetDir = "d:\github\ENEL445\reference\notes"
$logFile = "d:\github\ENEL445\conversion_log.txt"

"=== Conversion Monitor Started: $(Get-Date) ===" | Out-File $logFile

Write-Host "Monitoring conversions and auto-replacing files..." -ForegroundColor Cyan
Write-Host "Log: $logFile" -ForegroundColor White
Write-Host ""

$processed = @()

while ($true) {
    $mdFiles = Get-ChildItem $sourceDir -Filter "*.md" -ErrorAction SilentlyContinue
    
    foreach ($mdFile in $mdFiles) {
        if ($processed -contains $mdFile.Name) { continue }
        
        # Wait a bit to ensure file is fully written
        Start-Sleep -Seconds 2
        
        # Check if file has content
        if ($mdFile.Length -gt 1KB) {
            $targetFile = Join-Path $targetDir $mdFile.Name
            
            # Backup old file if exists
            if (Test-Path $targetFile) {
                $backupDir = "d:\github\ENEL445\reference\notes_backup"
                New-Item -ItemType Directory -Path $backupDir -Force | Out-Null
                Copy-Item $targetFile (Join-Path $backupDir $mdFile.Name) -Force
            }
            
            # Copy new file
            Copy-Item $mdFile.FullName $targetFile -Force
            $processed += $mdFile.Name
            
            $msg = "✓ Replaced: $($mdFile.Name) ($([math]::Round($mdFile.Length/1KB, 1)) KB)"
            Write-Host $msg -ForegroundColor Green
            $msg | Out-File $logFile -Append
        }
    }
    
    # Check if batch conversion still running
    $batchProc = Get-Process powershell -ErrorAction SilentlyContinue | Where-Object { $_.Id -eq 28248 }
    if (-not $batchProc) {
        $msg = "Batch conversion completed. Total replaced: $($processed.Count)"
        Write-Host "`n$msg" -ForegroundColor Cyan
        $msg | Out-File $logFile -Append
        break
    }
    
    Start-Sleep -Seconds 10
}

"=== Monitor Ended: $(Get-Date) ===" | Out-File $logFile -Append
Write-Host "`n✓ All done! Check $logFile for details" -ForegroundColor Green
