# PowerShell script to run Docker via WSL
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Starting E-Commerce App with Docker" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Close any running manual services
Write-Host "Note: Please close any PowerShell windows running backend/frontend manually" -ForegroundColor Yellow
Write-Host "Press Enter to continue..." -ForegroundColor Yellow
$null = Read-Host

Write-Host ""
Write-Host "Starting Docker containers via WSL..." -ForegroundColor Cyan
Write-Host ""

# Convert Windows path to WSL path
$currentPath = (Get-Location).Path
$wslPath = $currentPath -replace '\\', '/' -replace '^([A-Z]):', '/mnt/$1' | ForEach-Object { $_.ToLower() }

Write-Host "Windows path: $currentPath" -ForegroundColor Gray
Write-Host "WSL path: $wslPath" -ForegroundColor Gray
Write-Host ""

# Run the bash script via WSL
wsl bash -c "cd '$wslPath' && chmod +x start-docker.sh && ./start-docker.sh"

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Green
    Write-Host "Application is running!" -ForegroundColor Green
    Write-Host "========================================" -ForegroundColor Green
    Write-Host ""
    Write-Host "Opening browser..." -ForegroundColor Cyan
    Start-Sleep -Seconds 2
    Start-Process "http://localhost:5173"
    Write-Host ""
    Write-Host "To stop all containers, run:" -ForegroundColor Yellow
    Write-Host "  wsl bash -c 'cd $wslPath && docker-compose down'" -ForegroundColor Cyan
} else {
    Write-Host ""
    Write-Host "Failed to start Docker containers" -ForegroundColor Red
    Write-Host ""
    Write-Host "Troubleshooting:" -ForegroundColor Yellow
    Write-Host "1. Make sure Docker is running in WSL: wsl docker --version" -ForegroundColor Gray
    Write-Host "2. Check if ports are free: netstat -ano | findstr '5173 8080 8000 5432'" -ForegroundColor Gray
    Write-Host "3. Try running manually from Ubuntu terminal" -ForegroundColor Gray
}

Write-Host ""
Write-Host "Press any key to exit..." -ForegroundColor Gray
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
