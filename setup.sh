#!/bin/bash

echo "=========================================="
echo "E-Commerce System - Manual Setup Script"
echo "=========================================="
echo ""

# Check prerequisites
echo "Checking prerequisites..."

if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.11 or higher."
    exit 1
fi

if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed. Please install Node.js 18 or higher."
    exit 1
fi

if ! command -v psql &> /dev/null; then
    echo "⚠️  PostgreSQL client not found. Make sure PostgreSQL is installed."
fi

echo "✅ Prerequisites check completed"
echo ""

# Setup Backend
echo "=========================================="
echo "Setting up Backend..."
echo "=========================================="
cd backend

echo "📦 Creating Python virtual environment..."
python3 -m venv venv

echo "🔧 Activating virtual environment..."
source venv/bin/activate || . venv/bin/activate

echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

echo "📝 Setting up environment variables..."
if [ ! -f .env ]; then
    cp .env.example .env
    echo "✅ .env file created. Please update it with your database credentials."
else
    echo "ℹ️  .env file already exists"
fi

echo ""
echo "⚠️  IMPORTANT: Make sure PostgreSQL is running and create the database:"
echo "   createdb ecommerce_db"
echo "   OR"
echo "   psql -U postgres -c 'CREATE DATABASE ecommerce_db;'"
echo ""
read -p "Press Enter once you've created the database..."

echo "🌱 Seeding database..."
python seed.py

cd ..

# Setup Frontend
echo ""
echo "=========================================="
echo "Setting up Frontend..."
echo "=========================================="
cd frontend

echo "📦 Installing Node.js dependencies..."
npm install

echo "📝 Setting up environment variables..."
echo "REACT_APP_API_URL=http://localhost:8000" > .env

cd ..

echo ""
echo "=========================================="
echo "✅ Setup Complete!"
echo "=========================================="
echo ""
echo "To start the application:"
echo ""
echo "1. Start the backend (in one terminal):"
echo "   cd backend"
echo "   source venv/bin/activate  # or . venv/bin/activate"
echo "   uvicorn app.main:app --reload"
echo ""
echo "2. Start the frontend (in another terminal):"
echo "   cd frontend"
echo "   npm start"
echo ""
echo "📱 Application URLs:"
echo "   Frontend: http://localhost:3000"
echo "   Backend API: http://localhost:8000"
echo "   API Docs: http://localhost:8000/docs"
echo ""
echo "👤 Default Admin Credentials:"
echo "   Username: admin"
echo "   Password: admin123"
echo ""
