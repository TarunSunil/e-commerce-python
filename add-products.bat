@echo off
echo ========================================
echo Adding 100 Products to Database
echo ========================================
echo.

cd backend
call venv\Scripts\activate.bat
python seed_products.py
pause
