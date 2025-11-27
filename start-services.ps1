# Script to wait for Docker and start services
Write-Host "Waiting for Docker Desktop to be ready..." -ForegroundColor Yellow

$maxAttempts = 30
$attempt = 0
$dockerReady = $false

while ($attempt -lt $maxAttempts -and -not $dockerReady) {
    try {
        $result = docker ps 2>&1
        if ($LASTEXITCODE -eq 0) {
            $dockerReady = $true
            Write-Host "Docker is ready!" -ForegroundColor Green
            break
        }
    } catch {
        # Continue waiting
    }
    
    $attempt++
    Write-Host "Attempt $attempt/$maxAttempts - Waiting for Docker..." -ForegroundColor Gray
    Start-Sleep -Seconds 5
}

if (-not $dockerReady) {
    Write-Host "Docker Desktop is taking longer than expected to start." -ForegroundColor Red
    Write-Host "Please ensure Docker Desktop is running and try again." -ForegroundColor Yellow
    exit 1
}

Write-Host "Building Docker images..." -ForegroundColor Cyan
docker compose build

if ($LASTEXITCODE -eq 0) {
    Write-Host "Starting all services..." -ForegroundColor Cyan
    docker compose up -d
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "`n========================================" -ForegroundColor Green
        Write-Host "All services are starting!" -ForegroundColor Green
        Write-Host "========================================" -ForegroundColor Green
        Write-Host "Frontend:  http://localhost:3000" -ForegroundColor Cyan
        Write-Host "Backend:   http://localhost:8080/api" -ForegroundColor Cyan
        Write-Host "Recommender: http://localhost:8000" -ForegroundColor Cyan
        Write-Host "`nTo view logs: docker compose logs -f" -ForegroundColor Yellow
        Write-Host "To stop: docker compose down" -ForegroundColor Yellow
    } else {
        Write-Host "Failed to start services. Check Docker Desktop is running." -ForegroundColor Red
    }
} else {
    Write-Host "Failed to build images." -ForegroundColor Red
}

