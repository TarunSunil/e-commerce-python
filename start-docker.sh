#!/bin/bash

echo "========================================"
echo "E-Commerce Docker Setup via WSL"
echo "========================================"
echo ""

# Get the Windows path and convert to WSL path
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

echo "Working directory: $(pwd)"
echo ""

# Stop any existing containers
echo "Stopping existing containers..."
docker-compose down 2>/dev/null

echo ""
echo "Building and starting containers..."
echo "This may take a few minutes on first run..."
echo ""

# Build and start containers
docker-compose up -d --build

if [ $? -eq 0 ]; then
    echo ""
    echo "========================================"
    echo "✓ All services started successfully!"
    echo "========================================"
    echo ""
    echo "Service URLs:"
    echo "  Frontend:     http://localhost:5173"
    echo "  Backend:      http://localhost:8080/api"
    echo "  Backend Docs: http://localhost:8080/api/docs"
    echo "  Recommender:  http://localhost:8000/docs"
    echo "  PostgreSQL:   localhost:5432"
    echo ""
    echo "To view logs:  docker-compose logs -f"
    echo "To stop:       docker-compose down"
    echo ""
    echo "Waiting for services to be ready..."
    sleep 5
    
    # Add products
    echo ""
    echo "Adding 100 sample products..."
    docker exec ecommerce-backend python seed_products.py
    
    if [ $? -eq 0 ]; then
        echo ""
        echo "✓ Products added successfully!"
        echo ""
        echo "Open your browser to: http://localhost:5173"
    fi
else
    echo ""
    echo "✗ Failed to start containers"
    echo "Check the error messages above"
fi
