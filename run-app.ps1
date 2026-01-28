# Start Services Script - Supports both Docker and Manual modes
# Usage: .\run-app.ps1 [docker|manual]

param(
    [Parameter(Mandatory=$false)]
    [ValidateSet('docker', 'manual')]
    [string]$Mode = 'manual'
)

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "E-Commerce Application Launcher" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

if ($Mode -eq 'docker') {
    Write-Host "Starting with Docker..." -ForegroundColor Yellow
    Write-Host ""
    
    # Check if Docker is available
    try {
        $dockerVersion = docker --version 2>&1
        Write-Host "✓ Docker found: $dockerVersion" -ForegroundColor Green
    } catch {
        Write-Host "✗ Docker not found! Please install Docker Desktop." -ForegroundColor Red
        exit 1
    }
    
    # Check if docker-compose.yml exists
    if (!(Test-Path "docker-compose.yml")) {
        Write-Host "✗ docker-compose.yml not found!" -ForegroundColor Red
        exit 1
    }
    
    Write-Host "`nStarting Docker containers..." -ForegroundColor Cyan
    docker-compose up -d
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "`n✓ All services started successfully!" -ForegroundColor Green
        Write-Host ""
        Write-Host "========================================" -ForegroundColor Green
        Write-Host "Service URLs:" -ForegroundColor Green
        Write-Host "========================================" -ForegroundColor Green
        Write-Host "Frontend:    http://localhost:5173" -ForegroundColor Cyan
        Write-Host "Backend:     http://localhost:8080/api" -ForegroundColor Cyan
        Write-Host "Backend Docs: http://localhost:8080/api/docs" -ForegroundColor Cyan
        Write-Host "Recommender:  http://localhost:8000" -ForegroundColor Cyan
        Write-Host ""
        Write-Host "To view logs: docker-compose logs -f" -ForegroundColor Yellow
        Write-Host "To stop:      docker-compose down" -ForegroundColor Yellow
    } else {
        Write-Host "`n✗ Failed to start Docker containers!" -ForegroundColor Red
        exit 1
    }
}
    
} elseif ($Mode -eq 'manual') {
    Write-Host "Starting services manually..." -ForegroundColor Yellow
    Write-Host ""
    
    # Check if .env files exist
    $envMissing = $false
    if (!(Test-Path "backend\.env")) {
        Write-Host "⚠ backend\.env not found!" -ForegroundColor Yellow
        $envMissing = $true
    }
    if (!(Test-Path "recommender\.env")) {
        Write-Host "⚠ recommender\.env not found!" -ForegroundColor Yellow
        $envMissing = $true
    }
    if (!(Test-Path "frontend\.env")) {
        Write-Host "⚠ frontend\.env not found!" -ForegroundColor Yellow
        $envMissing = $true
    }
    
    if ($envMissing) {
        Write-Host ""
        $response = Read-Host "Create .env files from templates? (y/n)"
        if ($response -eq 'y') {
            if (!(Test-Path "backend\.env")) {
                Copy-Item "backend\.env.example" "backend\.env"
                Write-Host "✓ Created backend\.env" -ForegroundColor Green
            }
            if (!(Test-Path "recommender\.env")) {
                Copy-Item "recommender\.env.example" "recommender\.env"
                Write-Host "✓ Created recommender\.env" -ForegroundColor Green
            }
            if (!(Test-Path "frontend\.env")) {
                Copy-Item "frontend\.env.example" "frontend\.env"
                Write-Host "✓ Created frontend\.env" -ForegroundColor Green
            }
            Write-Host ""
            Write-Host "⚠ Please update .env files with your settings and run this script again!" -ForegroundColor Yellow
            exit 0
        }
    }
    
    Write-Host "========================================" -ForegroundColor Cyan
    Write-Host "Starting services in separate windows..." -ForegroundColor Cyan
    Write-Host "========================================" -ForegroundColor Cyan
    Write-Host ""
    
    # Start Backend
    Write-Host "Starting Backend API..." -ForegroundColor Yellow
    Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$PWD\backend'; .\venv\Scripts\Activate.ps1; Write-Host '🚀 Starting Backend API on port 8080...' -ForegroundColor Green; uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload"
    Start-Sleep -Seconds 2
    
    # Start Recommender
    Write-Host "Starting Recommender Service..." -ForegroundColor Yellow
    Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$PWD\recommender'; .\venv\Scripts\Activate.ps1; Write-Host '🚀 Starting Recommender Service on port 8000...' -ForegroundColor Green; uvicorn app:app --host 0.0.0.0 --port 8000 --reload"
    Start-Sleep -Seconds 2
    
    # Start Frontend
    Write-Host "Starting Frontend..." -ForegroundColor Yellow
    Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$PWD\frontend'; Write-Host '🚀 Starting Frontend on port 5173...' -ForegroundColor Green; npm run dev"
    Start-Sleep -Seconds 2
    
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Green
    Write-Host "✓ All services started!" -ForegroundColor Green
    Write-Host "========================================" -ForegroundColor Green
    Write-Host ""
    Write-Host "Services are running in separate windows." -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Service URLs:" -ForegroundColor Yellow
    Write-Host "  Frontend:     http://localhost:5173" -ForegroundColor Cyan
    Write-Host "  Backend:      http://localhost:8080/api" -ForegroundColor Cyan
    Write-Host "  Backend Docs: http://localhost:8080/api/docs" -ForegroundColor Cyan
    Write-Host "  Recommender:  http://localhost:8000" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "⚠ To stop services, close each PowerShell window" -ForegroundColor Yellow
    Write-Host "  or press Ctrl+C in each window" -ForegroundColor Yellow
    Write-Host ""
}

Write-Host "Press any key to exit..." -ForegroundColor Gray
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
