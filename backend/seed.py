"""
Seed script to populate the database with initial data
"""
from sqlalchemy.orm import Session
from app.core.database import SessionLocal, engine
from app.models.models import Base, User, Category, Product
from app.core.security import get_password_hash


def create_admin_user(db: Session):
    admin = db.query(User).filter(User.username == "admin").first()
    if not admin:
        admin = User(
            email="admin@example.com",
            username="admin",
            full_name="Admin User",
            hashed_password=get_password_hash("admin123"),
            is_admin=True,
            is_active=True
        )
        db.add(admin)
        db.commit()
        print("Admin user created: username=admin, password=admin123")
    else:
        print("Admin user already exists")


def create_categories(db: Session):
    categories = [
        {"name": "Electronics", "description": "Electronic devices and gadgets"},
        {"name": "Clothing", "description": "Fashion and apparel"},
        {"name": "Books", "description": "Books and publications"},
        {"name": "Home & Garden", "description": "Home and garden products"},
        {"name": "Sports", "description": "Sports equipment and accessories"},
    ]
    
    for cat_data in categories:
        existing = db.query(Category).filter(Category.name == cat_data["name"]).first()
        if not existing:
            category = Category(**cat_data)
            db.add(category)
    
    db.commit()
    print(f"Categories created")


def create_sample_products(db: Session):
    # Get categories
    electronics = db.query(Category).filter(Category.name == "Electronics").first()
    clothing = db.query(Category).filter(Category.name == "Clothing").first()
    books = db.query(Category).filter(Category.name == "Books").first()
    
    products = [
        {
            "name": "Laptop",
            "description": "High-performance laptop for work and gaming",
            "price": 999.99,
            "stock": 50,
            "category_id": electronics.id if electronics else None,
            "image_url": "https://via.placeholder.com/300x300?text=Laptop"
        },
        {
            "name": "Smartphone",
            "description": "Latest smartphone with advanced features",
            "price": 699.99,
            "stock": 100,
            "category_id": electronics.id if electronics else None,
            "image_url": "https://via.placeholder.com/300x300?text=Smartphone"
        },
        {
            "name": "Wireless Headphones",
            "description": "Noise-cancelling wireless headphones",
            "price": 199.99,
            "stock": 75,
            "category_id": electronics.id if electronics else None,
            "image_url": "https://via.placeholder.com/300x300?text=Headphones"
        },
        {
            "name": "T-Shirt",
            "description": "Comfortable cotton t-shirt",
            "price": 19.99,
            "stock": 200,
            "category_id": clothing.id if clothing else None,
            "image_url": "https://via.placeholder.com/300x300?text=T-Shirt"
        },
        {
            "name": "Jeans",
            "description": "Classic denim jeans",
            "price": 49.99,
            "stock": 150,
            "category_id": clothing.id if clothing else None,
            "image_url": "https://via.placeholder.com/300x300?text=Jeans"
        },
        {
            "name": "Python Programming Book",
            "description": "Comprehensive guide to Python programming",
            "price": 39.99,
            "stock": 80,
            "category_id": books.id if books else None,
            "image_url": "https://via.placeholder.com/300x300?text=Python+Book"
        },
    ]
    
    for prod_data in products:
        existing = db.query(Product).filter(Product.name == prod_data["name"]).first()
        if not existing:
            product = Product(**prod_data)
            db.add(product)
    
    db.commit()
    print(f"Sample products created")


def seed_database():
    # Create tables
    Base.metadata.create_all(bind=engine)
    
    # Create database session
    db = SessionLocal()
    
    try:
        print("Starting database seeding...")
        create_admin_user(db)
        create_categories(db)
        create_sample_products(db)
        print("Database seeding completed successfully!")
    except Exception as e:
        print(f"Error seeding database: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    seed_database()
