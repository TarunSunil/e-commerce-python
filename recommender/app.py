from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import requests
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from recommender import ContentBasedRecommender

app = FastAPI(title="E-Commerce Recommender Service")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Backend API URL (should be configurable via environment variable)
BACKEND_URL = "http://localhost:8080/api"

class Product(BaseModel):
    id: str
    name: str
    description: str
    categories: List[str]
    price: float
    images: List[str]
    stock: int
    attributes: dict

recommender = ContentBasedRecommender()

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/recommend/{product_id}")
async def recommend_by_product(product_id: str, limit: int = 5):
    """
    Get product recommendations based on a product ID.
    Fetches product from backend and returns similar products.
    """
    try:
        # Fetch product from backend
        response = requests.get(f"{BACKEND_URL}/products/{product_id}")
        if response.status_code != 200:
            raise HTTPException(status_code=404, detail="Product not found")
        
        product = response.json()
        
        # Fetch all products for recommendation
        all_products_response = requests.get(f"{BACKEND_URL}/products?page=0&size=100")
        if all_products_response.status_code != 200:
            raise HTTPException(status_code=500, detail="Failed to fetch products")
        
        all_products = all_products_response.json()
        
        # Get recommendations
        recommendations = recommender.recommend_by_product(product, all_products, limit)
        
        return recommendations
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/recommend/user/{user_id}")
async def recommend_by_user(user_id: str, limit: int = 5):
    """
    Get product recommendations based on user preferences.
    """
    try:
        # Fetch user from backend (would need auth token in production)
        # For now, we'll fetch all products and use a simple popularity-based approach
        all_products_response = requests.get(f"{BACKEND_URL}/products?page=0&size=100")
        if all_products_response.status_code != 200:
            raise HTTPException(status_code=500, detail="Failed to fetch products")
        
        all_products = all_products_response.json()
        
        # Simple popularity-based recommendation (by stock as proxy)
        recommendations = sorted(all_products, key=lambda x: x.get('stock', 0), reverse=True)[:limit]
        
        return recommendations
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


