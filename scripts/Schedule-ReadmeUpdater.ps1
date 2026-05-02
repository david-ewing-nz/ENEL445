#Requires -Version 5.1
#Requires -RunAsAdministrator
<#
.SYNOPSIS
    Registers a Windows Task Scheduler task to run Update-Readme.ps1 hourly.
.NOTES
    Must be run once as Administrator.
    Task runs under the current user account without requiring a password prompt.
#>

$taskName  = 'ENEL445-ReadmeUpdater'
$scriptPath = 'D:\github\ENEL445\scripts\Update-Readme.ps1'
$pwsh       = (Get-Command pwsh.exe).Source

$action  = New-ScheduledTaskAction -Execute $pwsh -Argument "-NonInteractive -WindowStyle Hidden -File `"$scriptPath`""
$trigger = New-ScheduledTaskTrigger -RepetitionInterval (New-TimeSpan -Hours 1) -Once -At (Get-Date)
$settings = New-ScheduledTaskSettingsSet -ExecutionTimeLimit (New-TimeSpan -Minutes 2) -StartWhenAvailable

# Remove existing task if present
if (Get-ScheduledTask -TaskName $taskName -ErrorAction SilentlyContinue) {
    Unregister-ScheduledTask -TaskName $taskName -Confirm:$false
    Write-Host "Removed existing task '$taskName'."
}

Register-ScheduledTask `
    -TaskName $taskName `
    -Action   $action `
    -Trigger  $trigger `
    -Settings $settings `
    -RunLevel Highest `
    -Description 'Hourly mechanical snapshot of ENEL445 project state to README-WHEN-YOU-RETURN.md' | Out-Null

Write-Host "Task '$taskName' registered. Runs hourly via Task Scheduler."
Write-Host "To trigger immediately: Start-ScheduledTask -TaskName '$taskName'"
