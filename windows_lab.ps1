# Read-only checks for your OWN Windows test machine. No admin privilege required for most checks.
Write-Host "=== Windows Version ==="
Get-ComputerInfo | Select-Object WindowsProductName, WindowsVersion, OsBuildNumber
Write-Host "=== IP configuration ==="
Get-NetIPConfiguration | Select-Object InterfaceAlias, IPv4Address, DNSServer
Write-Host "=== Last 5 System Errors (if accessible) ==="
Get-WinEvent -FilterHashtable @{LogName='System'; Level=2} -MaxEvents 5 -ErrorAction SilentlyContinue | Select-Object TimeCreated, ProviderName, Id, Message
Write-Host "Example ONLY: use an authorized isolated lab to explore local account management."
Write-Host 'Get-LocalUser'
# No account creation, password reset, or domain modification in this script.
