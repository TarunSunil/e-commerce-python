# Simple PostgreSQL Database Setup Script
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "PostgreSQL Database Setup" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if psql is available
try {
    $pgVersion = psql --version 2>&1
    Write-Host "✓ PostgreSQL found: $pgVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ psql command not found!" -ForegroundColor Red
    Write-Host "Please install PostgreSQL or add it to your PATH" -ForegroundColor Yellow
    exit 1
}

Write-Host ""
Write-Host "This will create:" -ForegroundColor Yellow
Write-Host "  Database: ecommerce" -ForegroundColor Gray
Write-Host "  User:     ecom_user" -ForegroundColor Gray
Write-Host "  Password: ecom_pass" -ForegroundColor Gray
Write-Host ""

$confirm = Read-Host "Proceed with default settings? (y/n) [y]"
if ($confirm -eq 'n') {
    Write-Host "Cancelled." -ForegroundColor Yellow
    exit 0
}

Write-Host ""
Write-Host "Creating database..." -ForegroundColor Cyan
Write-Host "You'll be prompted for the PostgreSQL superuser (postgres) password." -ForegroundColor Yellow
Write-Host ""

# Create database
Write-Host "Step 1: Creating database 'ecommerce'..." -ForegroundColor Cyan
psql -U postgres -c "CREATE DATABASE ecommerce;"

if ($LASTEXITCODE -ne 0) {
    Write-Host "Note: Database might already exist, continuing..." -ForegroundColor Yellow
}

# Create user
Write-Host "Step 2: Creating user ecom_user..." -ForegroundColor Cyan
$createUserCmd = "CREATE USER ecom_user WITH PASSWORD ''ecom_pass'';"
psql -U postgres -c $createUserCmd

if ($LASTEXITCODE -ne 0) {
    Write-Host "Note: User might already exist, continuing..." -ForegroundColor Yellow
}

# Grant privileges
Write-Host "Step 3: Granting privileges..." -ForegroundColor Cyan
psql -U postgres -c "GRANT ALL PRIVILEGES ON DATABASE ecommerce TO ecom_user;"
psql -U postgres -d ecommerce -c "GRANT ALL ON SCHEMA public TO ecom_user;"
psql -U postgres -d ecommerce -c "ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO ecom_user;"
psql -U postgres -d ecommerce -c "ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON SEQUENCES TO ecom_user;"

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "✓ Database setup complete!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "Database connection string:" -ForegroundColor Yellow
Write-Host "  postgresql+psycopg2://ecom_user:ecom_pass@localhost:5432/ecommerce" -ForegroundColor Cyan
Write-Host ""
Write-Host "This is already configured in backend\.env" -ForegroundColor Green
Write-Host ""
Write-Host "Next step: Add products by running:" -ForegroundColor Yellow
Write-Host "  cd backend" -ForegroundColor Cyan
Write-Host "  .\venv\Scripts\Activate.ps1" -ForegroundColor Cyan
Write-Host "  python seed_products.py" -ForegroundColor Cyan
Write-Host ""
