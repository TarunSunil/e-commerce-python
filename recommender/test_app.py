import requests
import time

print("Waiting for server to be ready...")
time.sleep(2)

try:
    print("Testing /health endpoint...")
    response = requests.get('http://localhost:8000/health', timeout=5)
    print(f"✓ Status: {response.status_code}")
    print(f"✓ Response: {response.json()}")
    print("\n✓ Health check passed!")
    
    # Test docs endpoint
    print("\nTesting /docs endpoint...")
    response = requests.get('http://localhost:8000/docs', timeout=5)
    print(f"✓ Docs endpoint accessible: {response.status_code}")
    
except requests.exceptions.ConnectionError:
    print("✗ Error: Could not connect to server at http://localhost:8000")
    print("  Make sure the server is running: python app.py")
except Exception as e:
    print(f"✗ Error: {e}")
