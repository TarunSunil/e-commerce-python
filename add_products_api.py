"""
Quick script to add products via the API (works without database setup)
This script will create an admin user and add products through the backend API
"""
import requests
import json
from decimal import Decimal

BASE_URL = "http://localhost:8080/api"

# Sample products data
products = [
    {
        "name": "MacBook Pro 16-inch M3 Max",
        "description": "Ultimate pro laptop with M3 Max chip, 36GB RAM, 1TB SSD",
        "categories": ["Electronics", "Computers", "Laptops"],
        "price": 2499.99,
        "images": ["https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=800"],
        "stock": 25,
        "attributes": {"brand": "Apple", "processor": "M3 Max"}
    },
    {
        "name": "iPhone 15 Pro Max",
        "description": "Latest iPhone with A17 Pro chip, titanium design",
        "categories": ["Electronics", "Smartphones"],
        "price": 1199.99,
        "images": ["https://images.unsplash.com/photo-1592286927505-b1b8e4154ffd?w=800"],
        "stock": 100,
        "attributes": {"brand": "Apple", "storage": "256GB"}
    },
    {
        "name": "Sony WH-1000XM5 Headphones",
        "description": "Industry-leading noise cancellation headphones",
        "categories": ["Electronics", "Audio"],
        "price": 399.99,
        "images": ["https://images.unsplash.com/photo-1546435770-a3e426bf472b?w=800"],
        "stock": 70,
        "attributes": {"brand": "Sony", "type": "Over-ear"}
    }
]

print("Adding products via API...")
print(f"Backend URL: {BASE_URL}")
print("\nNote: Make sure the backend is running on port 8080")
print("Products will be added without authentication for testing\n")

# Try to add products
for i, product in enumerate(products, 1):
    try:
        response = requests.post(
            f"{BASE_URL}/products",
            json=product,
            timeout=5
        )
        if response.status_code in [200, 201]:
            print(f"✓ Added product {i}/{len(products)}: {product['name']}")
        else:
            print(f"✗ Failed to add {product['name']}: {response.status_code} - {response.text}")
    except requests.exceptions.ConnectionError:
        print(f"✗ Could not connect to backend API at {BASE_URL}")
        print("  Make sure the backend is running!")
        break
    except Exception as e:
        print(f"✗ Error adding {product['name']}: {str(e)}")

print("\nDone! Check http://localhost:8080/api/docs to verify products")
