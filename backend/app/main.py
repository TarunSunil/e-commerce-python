from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api import auth, products, categories, cart, orders
from .core.database import engine, Base

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="E-Commerce API",
    description="A comprehensive e-commerce management system API",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],  # React dev servers
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(products.router, prefix="/api/products", tags=["Products"])
app.include_router(categories.router, prefix="/api/categories", tags=["Categories"])
app.include_router(cart.router, prefix="/api/cart", tags=["Cart"])
app.include_router(orders.router, prefix="/api/orders", tags=["Orders"])


@app.get("/")
def root():
    return {"message": "Welcome to E-Commerce API"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
