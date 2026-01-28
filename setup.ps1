# Quick Setup Script for E-Commerce Application
# This script helps you set up the development environment quickly

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "E-Commerce Application Setup" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check prerequisites
Write-Host "Checking prerequisites..." -ForegroundColor Yellow

# Check Python
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✓ Python found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ Python not found! Please install Python 3.11+" -ForegroundColor Red
    exit 1
}

# Check Node.js
try {
    $nodeVersion = node --version 2>&1
    Write-Host "✓ Node.js found: $nodeVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ Node.js not found! Please install Node.js 18+" -ForegroundColor Red
    exit 1
}

# Check PostgreSQL
try {
    $pgVersion = psql --version 2>&1
    Write-Host "✓ PostgreSQL found: $pgVersion" -ForegroundColor Green
} catch {
    Write-Host "⚠ PostgreSQL not found in PATH. Make sure it's installed!" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Setup Options" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "1. Full Setup (Backend + Recommender + Frontend)"
Write-Host "2. Backend Only"
Write-Host "3. Recommender Only"
Write-Host "4. Frontend Only"
Write-Host "5. Create .env files from templates"
Write-Host "6. Exit"
Write-Host ""

$choice = Read-Host "Enter your choice (1-6)"

switch ($choice) {
    "1" {
        Write-Host "`nSetting up all services..." -ForegroundColor Yellow
        
        # Backend
        Write-Host "`n[1/3] Setting up Backend..." -ForegroundColor Cyan
        Set-Location backend
        if (!(Test-Path "venv")) {
            Write-Host "Creating virtual environment..." -ForegroundColor Yellow
            python -m venv venv
        }
        Write-Host "Activating virtual environment..." -ForegroundColor Yellow
        .\venv\Scripts\Activate.ps1
        Write-Host "Installing dependencies..." -ForegroundColor Yellow
        pip install -r requirements.txt
        Set-Location ..
        
        # Recommender
        Write-Host "`n[2/3] Setting up Recommender..." -ForegroundColor Cyan
        Set-Location recommender
        if (!(Test-Path "venv")) {
            Write-Host "Creating virtual environment..." -ForegroundColor Yellow
            python -m venv venv
        }
        Write-Host "Activating virtual environment..." -ForegroundColor Yellow
        .\venv\Scripts\Activate.ps1
        Write-Host "Installing dependencies..." -ForegroundColor Yellow
        pip install -r requirements.txt
        Set-Location ..
        
        # Frontend
        Write-Host "`n[3/3] Setting up Frontend..." -ForegroundColor Cyan
        Set-Location frontend
        Write-Host "Installing npm packages..." -ForegroundColor Yellow
        npm install
        Set-Location ..
        
        Write-Host "`n✓ All services setup complete!" -ForegroundColor Green
    }
    
    "2" {
        Write-Host "`nSetting up Backend..." -ForegroundColor Cyan
        Set-Location backend
        if (!(Test-Path "venv")) {
            python -m venv venv
        }
        .\venv\Scripts\Activate.ps1
        pip install -r requirements.txt
        Set-Location ..
        Write-Host "✓ Backend setup complete!" -ForegroundColor Green
    }
    
    "3" {
        Write-Host "`nSetting up Recommender..." -ForegroundColor Cyan
        Set-Location recommender
        if (!(Test-Path "venv")) {
            python -m venv venv
        }
        .\venv\Scripts\Activate.ps1
        pip install -r requirements.txt
        Set-Location ..
        Write-Host "✓ Recommender setup complete!" -ForegroundColor Green
    }
    
    "4" {
        Write-Host "`nSetting up Frontend..." -ForegroundColor Cyan
        Set-Location frontend
        npm install
        Set-Location ..
        Write-Host "✓ Frontend setup complete!" -ForegroundColor Green
    }
    
    "5" {
        Write-Host "`nCreating .env files from templates..." -ForegroundColor Cyan
        
        if (!(Test-Path "backend\.env")) {
            Copy-Item "backend\.env.example" "backend\.env"
            Write-Host "✓ Created backend\.env" -ForegroundColor Green
        } else {
            Write-Host "⚠ backend\.env already exists, skipping" -ForegroundColor Yellow
        }
        
        if (!(Test-Path "recommender\.env")) {
            Copy-Item "recommender\.env.example" "recommender\.env"
            Write-Host "✓ Created recommender\.env" -ForegroundColor Green
        } else {
            Write-Host "⚠ recommender\.env already exists, skipping" -ForegroundColor Yellow
        }
        
        if (!(Test-Path "frontend\.env")) {
            Copy-Item "frontend\.env.example" "frontend\.env"
            Write-Host "✓ Created frontend\.env" -ForegroundColor Green
        } else {
            Write-Host "⚠ frontend\.env already exists, skipping" -ForegroundColor Yellow
        }
        
        Write-Host "`n✓ .env files created! Remember to update them with your settings." -ForegroundColor Green
    }
    
    "6" {
        Write-Host "Exiting..." -ForegroundColor Yellow
        exit 0
    }
    
    default {
        Write-Host "Invalid choice!" -ForegroundColor Red
        exit 1
    }
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Next Steps" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "1. Create .env files (if not done): .\setup.ps1 and choose option 5"
Write-Host "2. Set up PostgreSQL database (see README.md)"
Write-Host "3. Update .env files with your database credentials"
Write-Host "4. Start services using start-services.ps1 or manually"
Write-Host ""
Write-Host "For detailed instructions, see README.md" -ForegroundColor Yellow
Write-Host ""
