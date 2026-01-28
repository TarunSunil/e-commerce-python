# Database Setup Helper Script
# This script helps you set up the PostgreSQL database

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "PostgreSQL Database Setup" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "This script will help you create the database for the e-commerce app." -ForegroundColor Yellow
Write-Host ""

# Check if psql is available
try {
    $pgVersion = psql --version 2>&1
    Write-Host "✓ PostgreSQL found: $pgVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ psql command not found!" -ForegroundColor Red
    Write-Host ""
    Write-Host "Please install PostgreSQL or add it to your PATH:" -ForegroundColor Yellow
    Write-Host "  Typical location: C:\Program Files\PostgreSQL\15\bin" -ForegroundColor Gray
    Write-Host ""
    exit 1
}

Write-Host ""
Write-Host "Default settings:" -ForegroundColor Cyan
Write-Host "  Database name: ecommerce" -ForegroundColor Gray
Write-Host "  Username:      ecom_user" -ForegroundColor Gray
Write-Host "  Password:      ecom_pass" -ForegroundColor Gray
Write-Host "  Host:          localhost" -ForegroundColor Gray
Write-Host "  Port:          5432" -ForegroundColor Gray
Write-Host ""

$useDefaults = Read-Host "Use default settings? (y/n) [y]"
if ($useDefaults -eq '' -or $useDefaults -eq 'y') {
    $dbName = "ecommerce"
    $dbUser = "ecom_user"
    $dbPass = "ecom_pass"
} else {
    $dbName = Read-Host "Enter database name [ecommerce]"
    if ($dbName -eq '') { $dbName = "ecommerce" }
    
    $dbUser = Read-Host "Enter database username [ecom_user]"
    if ($dbUser -eq '') { $dbUser = "ecom_user" }
    
    $dbPass = Read-Host "Enter database password [ecom_pass]" -AsSecureString
    $dbPass = [Runtime.InteropServices.Marshal]::PtrToStringAuto(
        [Runtime.InteropServices.Marshal]::SecureStringToBSTR($dbPass))
    if ($dbPass -eq '') { $dbPass = "ecom_pass" }
}

Write-Host ""
Write-Host "Will create:" -ForegroundColor Yellow
Write-Host "  Database: $dbName" -ForegroundColor Gray
Write-Host "  User:     $dbUser" -ForegroundColor Gray
Write-Host ""

$confirm = Read-Host "Proceed? (y/n) [y]"
if ($confirm -eq 'n') {
    Write-Host "Cancelled." -ForegroundColor Yellow
    exit 0
}

Write-Host ""
Write-Host "Creating database..." -ForegroundColor Cyan
Write-Host "You'll be prompted for the PostgreSQL superuser (postgres) password." -ForegroundColor Yellow
Write-Host ""

# Create SQL commands
$sqlCommands = @"
CREATE DATABASE $dbName;
CREATE USER $dbUser WITH PASSWORD '$dbPass';
GRANT ALL PRIVILEGES ON DATABASE $dbName TO $dbUser;
"@

$sqlCommands2 = @"
GRANT ALL ON SCHEMA public TO $dbUser;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO $dbUser;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON SEQUENCES TO $dbUser;
"@

# Save to temporary file
$tempFile = "$env:TEMP\ecommerce_setup.sql"
$sqlCommands | Out-File -FilePath $tempFile -Encoding UTF8

# Execute SQL
Write-Host "Executing SQL commands..." -ForegroundColor Cyan
psql -U postgres -f $tempFile

if ($LASTEXITCODE -eq 0) {
    # Now connect to the new database and grant additional permissions
    Write-Host "Setting schema permissions..." -ForegroundColor Cyan
    $tempFile2 = "$env:TEMP\ecommerce_schema.sql"
    $sqlCommands2 | Out-File -FilePath $tempFile2 -Encoding UTF8
    psql -U postgres -d $dbName -f $tempFile2
}

# Clean up
Remove-Item $tempFile -ErrorAction SilentlyContinue
Remove-Item $tempFile2 -ErrorAction SilentlyContinue

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Green
    Write-Host "✓ Database setup complete!" -ForegroundColor Green
    Write-Host "========================================" -ForegroundColor Green
    Write-Host ""
    Write-Host "Next steps:" -ForegroundColor Yellow
    Write-Host "1. Update backend\.env with these credentials:" -ForegroundColor Gray
    Write-Host "   DATABASE_URL=postgresql+psycopg2://${dbUser}:${dbPass}@localhost:5432/${dbName}" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "2. Start the application:" -ForegroundColor Gray
    Write-Host "   .\run-app.ps1 manual" -ForegroundColor Cyan
    Write-Host ""
} else {
    Write-Host ""
    Write-Host "✗ Database setup failed!" -ForegroundColor Red
    Write-Host ""
    Write-Host "Common issues:" -ForegroundColor Yellow
    Write-Host "  - Wrong postgres password" -ForegroundColor Gray
    Write-Host "  - PostgreSQL service not running" -ForegroundColor Gray
    Write-Host "  - Database already exists (delete it first)" -ForegroundColor Gray
    Write-Host ""
    Write-Host "To delete existing database, run as postgres user:" -ForegroundColor Gray
    Write-Host "  psql -U postgres -c ""DROP DATABASE IF EXISTS $dbName;""" -ForegroundColor Cyan
    Write-Host "  psql -U postgres -c ""DROP USER IF EXISTS $dbUser;""" -ForegroundColor Cyan
    Write-Host ""
}

Write-Host ""
Write-Host "Press any key to exit..." -ForegroundColor Gray
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
