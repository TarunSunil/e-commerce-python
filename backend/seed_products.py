"""
Seed script to populate the database with 100 sample products
Run this script: python seed_products.py
"""
import sys
from pathlib import Path

# Add parent directory to path
sys.path.append(str(Path(__file__).parent))

from sqlalchemy.orm import Session
from app.database import SessionLocal, engine, Base
from app.models.product import Product
from decimal import Decimal
import random

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)

def create_products(db: Session):
    """Create 100 diverse products across multiple categories"""
    
    products_data = [
        # Electronics - Laptops & Computers (15 products)
        {
            "name": "MacBook Pro 16-inch M3 Max",
            "description": "Ultimate pro laptop with M3 Max chip, 36GB RAM, 1TB SSD. Perfect for developers and creators.",
            "categories": ["Electronics", "Computers", "Laptops"],
            "price": Decimal("2499.99"),
            "images": ["https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=800"],
            "stock": 25,
            "attributes": {"brand": "Apple", "processor": "M3 Max", "ram": "36GB", "storage": "1TB SSD", "screen": "16-inch Liquid Retina"}
        },
        {
            "name": "Dell XPS 15 OLED",
            "description": "Premium Windows laptop with 13th Gen Intel Core i7, stunning 4K OLED display.",
            "categories": ["Electronics", "Computers", "Laptops"],
            "price": Decimal("1899.99"),
            "images": ["https://images.unsplash.com/photo-1593642632823-8f785ba67e45?w=800"],
            "stock": 30,
            "attributes": {"brand": "Dell", "processor": "Intel i7-13700H", "ram": "32GB", "storage": "1TB SSD", "screen": "15.6-inch 4K OLED"}
        },
        {
            "name": "Lenovo ThinkPad X1 Carbon",
            "description": "Business ultrabook with legendary keyboard, 12th Gen Intel, all-day battery life.",
            "categories": ["Electronics", "Computers", "Laptops", "Business"],
            "price": Decimal("1549.99"),
            "images": ["https://images.unsplash.com/photo-1588872657578-7efd1f1555ed?w=800"],
            "stock": 40,
            "attributes": {"brand": "Lenovo", "processor": "Intel i7-1260P", "ram": "16GB", "storage": "512GB SSD", "weight": "2.48 lbs"}
        },
        {
            "name": "ASUS ROG Zephyrus G14",
            "description": "Compact gaming laptop with AMD Ryzen 9, RTX 4060, 14-inch QHD display.",
            "categories": ["Electronics", "Computers", "Laptops", "Gaming"],
            "price": Decimal("1699.99"),
            "images": ["https://images.unsplash.com/photo-1603302576837-37561b2e2302?w=800"],
            "stock": 20,
            "attributes": {"brand": "ASUS", "processor": "AMD Ryzen 9 7940HS", "gpu": "RTX 4060", "ram": "16GB", "storage": "1TB SSD"}
        },
        {
            "name": "HP Pavilion 15 Student Edition",
            "description": "Affordable laptop perfect for students, with Intel Core i5 and long battery life.",
            "categories": ["Electronics", "Computers", "Laptops"],
            "price": Decimal("649.99"),
            "images": ["https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=800"],
            "stock": 50,
            "attributes": {"brand": "HP", "processor": "Intel i5-1235U", "ram": "8GB", "storage": "256GB SSD"}
        },
        
        # Smartphones (15 products)
        {
            "name": "iPhone 15 Pro Max",
            "description": "Latest iPhone with A17 Pro chip, titanium design, advanced camera system.",
            "categories": ["Electronics", "Smartphones", "Mobile"],
            "price": Decimal("1199.99"),
            "images": ["https://images.unsplash.com/photo-1592286927505-b1b8e4154ffd?w=800"],
            "stock": 100,
            "attributes": {"brand": "Apple", "storage": "256GB", "screen": "6.7-inch", "camera": "48MP", "5G": True}
        },
        {
            "name": "Samsung Galaxy S24 Ultra",
            "description": "Premium Android flagship with S Pen, 200MP camera, stunning display.",
            "categories": ["Electronics", "Smartphones", "Mobile"],
            "price": Decimal("1299.99"),
            "images": ["https://images.unsplash.com/photo-1610945415295-d9bbf067e59c?w=800"],
            "stock": 80,
            "attributes": {"brand": "Samsung", "storage": "512GB", "screen": "6.8-inch Dynamic AMOLED", "camera": "200MP"}
        },
        {
            "name": "Google Pixel 8 Pro",
            "description": "Pure Android experience with amazing AI features and camera magic.",
            "categories": ["Electronics", "Smartphones", "Mobile"],
            "price": Decimal("999.99"),
            "images": ["https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=800"],
            "stock": 60,
            "attributes": {"brand": "Google", "storage": "256GB", "screen": "6.7-inch", "camera": "50MP", "AI": "Google Tensor G3"}
        },
        {
            "name": "OnePlus 12",
            "description": "Flagship killer with Snapdragon 8 Gen 3, 100W fast charging.",
            "categories": ["Electronics", "Smartphones", "Mobile"],
            "price": Decimal("799.99"),
            "images": ["https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=800"],
            "stock": 45,
            "attributes": {"brand": "OnePlus", "storage": "256GB", "screen": "6.82-inch", "charging": "100W"}
        },
        {
            "name": "Xiaomi 13 Pro",
            "description": "Value flagship with Leica cameras, gorgeous display, fast performance.",
            "categories": ["Electronics", "Smartphones", "Mobile"],
            "price": Decimal("699.99"),
            "images": ["https://images.unsplash.com/photo-1585060544812-6b45742d762f?w=800"],
            "stock": 55,
            "attributes": {"brand": "Xiaomi", "storage": "256GB", "screen": "6.73-inch", "camera": "Leica optics"}
        },
        
        # Tablets (5 products)
        {
            "name": "iPad Pro 12.9-inch M2",
            "description": "Most powerful iPad with M2 chip, Liquid Retina XDR display, Apple Pencil support.",
            "categories": ["Electronics", "Tablets", "Mobile"],
            "price": Decimal("1099.99"),
            "images": ["https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=800"],
            "stock": 35,
            "attributes": {"brand": "Apple", "storage": "256GB", "screen": "12.9-inch", "chip": "M2"}
        },
        {
            "name": "Samsung Galaxy Tab S9 Ultra",
            "description": "Massive 14.6-inch AMOLED display, S Pen included, desktop-like experience.",
            "categories": ["Electronics", "Tablets", "Mobile"],
            "price": Decimal("1199.99"),
            "images": ["https://images.unsplash.com/photo-1561154464-82e9adf32764?w=800"],
            "stock": 25,
            "attributes": {"brand": "Samsung", "storage": "512GB", "screen": "14.6-inch AMOLED"}
        },
        {
            "name": "Microsoft Surface Pro 9",
            "description": "2-in-1 tablet/laptop with Windows 11, Intel or ARM processor options.",
            "categories": ["Electronics", "Tablets", "Computers"],
            "price": Decimal("999.99"),
            "images": ["https://images.unsplash.com/photo-1587614382346-4ec70e388b28?w=800"],
            "stock": 30,
            "attributes": {"brand": "Microsoft", "storage": "256GB", "screen": "13-inch PixelSense"}
        },
        
        # Headphones & Audio (10 products)
        {
            "name": "Sony WH-1000XM5",
            "description": "Industry-leading noise cancellation, exceptional sound quality, 30-hour battery.",
            "categories": ["Electronics", "Audio", "Headphones"],
            "price": Decimal("399.99"),
            "images": ["https://images.unsplash.com/photo-1546435770-a3e426bf472b?w=800"],
            "stock": 70,
            "attributes": {"brand": "Sony", "type": "Over-ear", "wireless": True, "ANC": True, "battery": "30 hours"}
        },
        {
            "name": "Apple AirPods Pro (2nd Gen)",
            "description": "Premium wireless earbuds with adaptive audio, transparency mode, USB-C charging.",
            "categories": ["Electronics", "Audio", "Earbuds"],
            "price": Decimal("249.99"),
            "images": ["https://images.unsplash.com/photo-1606841837239-c5a1a4a07af7?w=800"],
            "stock": 150,
            "attributes": {"brand": "Apple", "type": "In-ear", "wireless": True, "ANC": True, "MagSafe": True}
        },
        {
            "name": "Bose QuietComfort Ultra",
            "description": "Spatial audio, world-class comfort, CustomTune technology for perfect sound.",
            "categories": ["Electronics", "Audio", "Headphones"],
            "price": Decimal("429.99"),
            "images": ["https://images.unsplash.com/photo-1484704849700-f032a568e944?w=800"],
            "stock": 40,
            "attributes": {"brand": "Bose", "type": "Over-ear", "wireless": True, "ANC": True}
        },
        {
            "name": "JBL Charge 5",
            "description": "Portable Bluetooth speaker with powerful bass, waterproof, 20-hour battery.",
            "categories": ["Electronics", "Audio", "Speakers"],
            "price": Decimal("179.99"),
            "images": ["https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=800"],
            "stock": 90,
            "attributes": {"brand": "JBL", "type": "Portable speaker", "waterproof": "IP67", "battery": "20 hours"}
        },
        {
            "name": "Sennheiser HD 660S2",
            "description": "Audiophile open-back headphones with natural sound signature.",
            "categories": ["Electronics", "Audio", "Headphones", "Audiophile"],
            "price": Decimal("599.99"),
            "images": ["https://images.unsplash.com/photo-1545127398-14699f92334b?w=800"],
            "stock": 20,
            "attributes": {"brand": "Sennheiser", "type": "Open-back", "impedance": "150Ω"}
        },
        
        # Smart Home (10 products)
        {
            "name": "Amazon Echo Show 10",
            "description": "Smart display that moves with you, Alexa built-in, video calls.",
            "categories": ["Electronics", "Smart Home", "Voice Assistants"],
            "price": Decimal("249.99"),
            "images": ["https://images.unsplash.com/photo-1518444065439-e933c06ce9cd?w=800"],
            "stock": 45,
            "attributes": {"brand": "Amazon", "screen": "10.1-inch", "voice": "Alexa", "camera": "13MP"}
        },
        {
            "name": "Google Nest Hub Max",
            "description": "Large smart display with Google Assistant, security camera features.",
            "categories": ["Electronics", "Smart Home", "Voice Assistants"],
            "price": Decimal("229.99"),
            "images": ["https://images.unsplash.com/photo-1558089687-5e5d5b78ca1c?w=800"],
            "stock": 50,
            "attributes": {"brand": "Google", "screen": "10-inch", "voice": "Google Assistant"}
        },
        {
            "name": "Philips Hue Starter Kit",
            "description": "Smart lighting system with 4 color bulbs and bridge, app-controlled.",
            "categories": ["Electronics", "Smart Home", "Lighting"],
            "price": Decimal("199.99"),
            "images": ["https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800"],
            "stock": 60,
            "attributes": {"brand": "Philips", "bulbs": "4", "colors": "16 million", "voice": "Alexa, Google, Siri"}
        },
        {
            "name": "Ring Video Doorbell Pro 2",
            "description": "HD+ video doorbell with advanced motion detection, 3D radar.",
            "categories": ["Electronics", "Smart Home", "Security"],
            "price": Decimal("279.99"),
            "images": ["https://images.unsplash.com/photo-1558002038-1055907df827?w=800"],
            "stock": 65,
            "attributes": {"brand": "Ring", "video": "1536p HD+", "field_of_view": "150°"}
        },
        {
            "name": "Nest Learning Thermostat",
            "description": "Smart thermostat that learns your schedule, saves energy automatically.",
            "categories": ["Electronics", "Smart Home", "Climate"],
            "price": Decimal("249.99"),
            "images": ["https://images.unsplash.com/photo-1545259741-2ea3ebf61fa3?w=800"],
            "stock": 40,
            "attributes": {"brand": "Google Nest", "display": "2.08-inch", "energy_saving": True}
        },
        
        # Clothing - Men (15 products)
        {
            "name": "Levi's 501 Original Jeans",
            "description": "Classic straight-fit jeans, button fly, iconic American style.",
            "categories": ["Clothing", "Men", "Jeans"],
            "price": Decimal("69.99"),
            "images": ["https://images.unsplash.com/photo-1542272604-787c3835535d?w=800"],
            "stock": 200,
            "attributes": {"brand": "Levi's", "fit": "Straight", "material": "100% Cotton"}
        },
        {
            "name": "Nike Air Max 270",
            "description": "Iconic sneakers with Max Air cushioning, breathable mesh upper.",
            "categories": ["Clothing", "Men", "Shoes", "Sneakers"],
            "price": Decimal("159.99"),
            "images": ["https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=800"],
            "stock": 120,
            "attributes": {"brand": "Nike", "type": "Running/Casual", "cushioning": "Max Air"}
        },
        {
            "name": "Ralph Lauren Oxford Shirt",
            "description": "Classic button-down shirt in premium cotton, perfect for any occasion.",
            "categories": ["Clothing", "Men", "Shirts"],
            "price": Decimal("89.99"),
            "images": ["https://images.unsplash.com/photo-1602810318383-e386cc2a3ccf?w=800"],
            "stock": 150,
            "attributes": {"brand": "Ralph Lauren", "material": "Cotton", "fit": "Classic"}
        },
        {
            "name": "The North Face Fleece Jacket",
            "description": "Warm fleece jacket for outdoor activities, breathable and lightweight.",
            "categories": ["Clothing", "Men", "Jackets", "Outdoor"],
            "price": Decimal("129.99"),
            "images": ["https://images.unsplash.com/photo-1591047139829-d91aecb6caea?w=800"],
            "stock": 80,
            "attributes": {"brand": "The North Face", "material": "Fleece", "weather": "All-season"}
        },
        {
            "name": "Champion Reverse Weave Hoodie",
            "description": "Premium heavyweight hoodie with iconic C logo, ultra-comfortable.",
            "categories": ["Clothing", "Men", "Hoodies"],
            "price": Decimal("64.99"),
            "images": ["https://images.unsplash.com/photo-1556821840-3a63f95609a7?w=800"],
            "stock": 100,
            "attributes": {"brand": "Champion", "weight": "Heavyweight", "material": "Cotton blend"}
        },
        
        # Clothing - Women (15 products)
        {
            "name": "Lululemon Align Leggings",
            "description": "Buttery-soft yoga pants with four-way stretch, high-rise fit.",
            "categories": ["Clothing", "Women", "Activewear", "Leggings"],
            "price": Decimal("98.99"),
            "images": ["https://images.unsplash.com/photo-1506629082955-511b1aa562c8?w=800"],
            "stock": 180,
            "attributes": {"brand": "Lululemon", "fabric": "Nulu", "rise": "High-rise", "length": "28-inch"}
        },
        {
            "name": "Zara Floral Midi Dress",
            "description": "Elegant midi dress with floral print, perfect for summer occasions.",
            "categories": ["Clothing", "Women", "Dresses"],
            "price": Decimal("79.99"),
            "images": ["https://images.unsplash.com/photo-1595777457583-95e059d581b8?w=800"],
            "stock": 90,
            "attributes": {"brand": "Zara", "length": "Midi", "pattern": "Floral", "season": "Spring/Summer"}
        },
        {
            "name": "Everlane Cashmere Sweater",
            "description": "Luxurious 100% cashmere sweater, minimalist design, ultra-soft.",
            "categories": ["Clothing", "Women", "Sweaters"],
            "price": Decimal("149.99"),
            "images": ["https://images.unsplash.com/photo-1434389677669-e08b4cac3105?w=800"],
            "stock": 60,
            "attributes": {"brand": "Everlane", "material": "100% Cashmere", "care": "Hand wash"}
        },
        {
            "name": "Adidas Ultraboost 22 Women",
            "description": "Premium running shoes with responsive Boost cushioning.",
            "categories": ["Clothing", "Women", "Shoes", "Running"],
            "price": Decimal("189.99"),
            "images": ["https://images.unsplash.com/photo-1539185441755-769473a23570?w=800"],
            "stock": 100,
            "attributes": {"brand": "Adidas", "type": "Running", "cushioning": "Boost", "support": "Neutral"}
        },
        {
            "name": "Mango Leather Jacket",
            "description": "Classic leather biker jacket, soft lambskin, timeless style.",
            "categories": ["Clothing", "Women", "Jackets", "Leather"],
            "price": Decimal("299.99"),
            "images": ["https://images.unsplash.com/photo-1551028719-00167b16eac5?w=800"],
            "stock": 45,
            "attributes": {"brand": "Mango", "material": "Lambskin leather", "style": "Biker"}
        },
        
        # Home & Kitchen (15 products)
        {
            "name": "Instant Pot Duo Plus 9-in-1",
            "description": "Multi-functional pressure cooker, slow cooker, rice cooker, and more.",
            "categories": ["Home", "Kitchen", "Appliances"],
            "price": Decimal("119.99"),
            "images": ["https://images.unsplash.com/photo-1585515320310-259814833e62?w=800"],
            "stock": 75,
            "attributes": {"brand": "Instant Pot", "capacity": "6 quarts", "functions": "9-in-1"}
        },
        {
            "name": "KitchenAid Stand Mixer",
            "description": "Professional 5-quart stand mixer with 10 speeds, includes attachments.",
            "categories": ["Home", "Kitchen", "Appliances", "Baking"],
            "price": Decimal("379.99"),
            "images": ["https://images.unsplash.com/photo-1578269174936-2709b6aeb913?w=800"],
            "stock": 50,
            "attributes": {"brand": "KitchenAid", "capacity": "5 quarts", "power": "325W", "speeds": "10"}
        },
        {
            "name": "Ninja Air Fryer",
            "description": "Large capacity air fryer with crisp technology, healthier cooking.",
            "categories": ["Home", "Kitchen", "Appliances"],
            "price": Decimal("129.99"),
            "images": ["https://images.unsplash.com/photo-1600084576091-6c31acd10723?w=800"],
            "stock": 95,
            "attributes": {"brand": "Ninja", "capacity": "5.5 quarts", "temp_range": "105-400°F"}
        },
        {
            "name": "Nespresso Vertuo Coffee Maker",
            "description": "Premium coffee and espresso machine with Centrifusion technology.",
            "categories": ["Home", "Kitchen", "Coffee"],
            "price": Decimal("199.99"),
            "images": ["https://images.unsplash.com/photo-1517668808822-9ebb02f2a0e6?w=800"],
            "stock": 60,
            "attributes": {"brand": "Nespresso", "type": "Pod-based", "sizes": "5 cup sizes"}
        },
        {
            "name": "All-Clad Stainless Steel Cookware Set",
            "description": "Professional-grade 10-piece cookware set, dishwasher safe.",
            "categories": ["Home", "Kitchen", "Cookware"],
            "price": Decimal("699.99"),
            "images": ["https://images.unsplash.com/photo-1556911220-bff31c812dba?w=800"],
            "stock": 30,
            "attributes": {"brand": "All-Clad", "pieces": "10", "material": "Stainless steel"}
        },
        
        # Furniture (10 products)
        {
            "name": "Herman Miller Aeron Chair",
            "description": "Ergonomic office chair with posture support, adjustable everything.",
            "categories": ["Home", "Furniture", "Office"],
            "price": Decimal("1445.00"),
            "images": ["https://images.unsplash.com/photo-1580480055273-228ff5388ef8?w=800"],
            "stock": 20,
            "attributes": {"brand": "Herman Miller", "type": "Office chair", "adjustable": "Full"}
        },
        {
            "name": "IKEA MALM Bed Frame",
            "description": "Modern bed frame with storage drawers, queen size, easy assembly.",
            "categories": ["Home", "Furniture", "Bedroom"],
            "price": Decimal("349.99"),
            "images": ["https://images.unsplash.com/photo-1505693416388-ac5ce068fe85?w=800"],
            "stock": 35,
            "attributes": {"brand": "IKEA", "size": "Queen", "storage": "4 drawers"}
        },
        {
            "name": "West Elm Mid-Century Sofa",
            "description": "Stylish 3-seater sofa with clean lines, comfortable cushions.",
            "categories": ["Home", "Furniture", "Living Room"],
            "price": Decimal("1299.00"),
            "images": ["https://images.unsplash.com/photo-1555041469-a586c61ea9bc?w=800"],
            "stock": 15,
            "attributes": {"brand": "West Elm", "seats": "3", "style": "Mid-century modern"}
        },
        {
            "name": "Pottery Barn Dining Table",
            "description": "Solid wood dining table seats 6-8, timeless farmhouse style.",
            "categories": ["Home", "Furniture", "Dining"],
            "price": Decimal("899.00"),
            "images": ["https://images.unsplash.com/photo-1617806118233-18e1de247200?w=800"],
            "stock": 25,
            "attributes": {"brand": "Pottery Barn", "material": "Solid wood", "seats": "6-8"}
        },
        {
            "name": "Wayfair Standing Desk",
            "description": "Electric height-adjustable desk, 60-inch, programmable presets.",
            "categories": ["Home", "Furniture", "Office"],
            "price": Decimal("499.99"),
            "images": ["https://images.unsplash.com/photo-1595515106969-1ce29566ff1c?w=800"],
            "stock": 40,
            "attributes": {"brand": "Wayfair", "size": "60x30 inches", "height_range": "28-48 inches"}
        },
        
        # Books (5 products)
        {
            "name": "Atomic Habits by James Clear",
            "description": "Bestselling guide to building good habits and breaking bad ones.",
            "categories": ["Books", "Self-Help", "Non-Fiction"],
            "price": Decimal("16.99"),
            "images": ["https://images.unsplash.com/photo-1544947950-fa07a98d237f?w=800"],
            "stock": 500,
            "attributes": {"author": "James Clear", "pages": "320", "format": "Paperback"}
        },
        {
            "name": "The Midnight Library by Matt Haig",
            "description": "Heartwarming novel about second chances and infinite possibilities.",
            "categories": ["Books", "Fiction", "Contemporary"],
            "price": Decimal("14.99"),
            "images": ["https://images.unsplash.com/photo-1512820790803-83ca734da794?w=800"],
            "stock": 300,
            "attributes": {"author": "Matt Haig", "pages": "304", "format": "Paperback"}
        },
        {
            "name": "Sapiens by Yuval Noah Harari",
            "description": "Brief history of humankind, from Stone Age to modern age.",
            "categories": ["Books", "History", "Non-Fiction"],
            "price": Decimal("18.99"),
            "images": ["https://images.unsplash.com/photo-1457369804613-52c61a468e7d?w=800"],
            "stock": 250,
            "attributes": {"author": "Yuval Noah Harari", "pages": "512", "format": "Paperback"}
        },
        
        # Sports & Outdoors (10 products)
        {
            "name": "Peloton Bike+",
            "description": "Premium exercise bike with rotating screen, live and on-demand classes.",
            "categories": ["Sports", "Fitness", "Exercise Equipment"],
            "price": Decimal("2495.00"),
            "images": ["https://images.unsplash.com/photo-1517836357463-d25dfeac3438?w=800"],
            "stock": 15,
            "attributes": {"brand": "Peloton", "screen": "23.8-inch rotating", "resistance": "Automatic"}
        },
        {
            "name": "Yeti Rambler Tumbler 30oz",
            "description": "Insulated stainless steel tumbler keeps drinks cold/hot for hours.",
            "categories": ["Sports", "Outdoor", "Drinkware"],
            "price": Decimal("39.99"),
            "images": ["https://images.unsplash.com/photo-1602143407151-7111542de6e8?w=800"],
            "stock": 200,
            "attributes": {"brand": "Yeti", "capacity": "30oz", "material": "Stainless steel", "insulated": True}
        },
        {
            "name": "Coleman Sundome Camping Tent",
            "description": "4-person tent with WeatherTec system, easy setup.",
            "categories": ["Sports", "Outdoor", "Camping"],
            "price": Decimal("89.99"),
            "images": ["https://images.unsplash.com/photo-1504280390367-361c6d9f38f4?w=800"],
            "stock": 45,
            "attributes": {"brand": "Coleman", "capacity": "4 person", "seasons": "3-season"}
        },
        {
            "name": "Wilson Evolution Basketball",
            "description": "Official size basketball with superior grip and durability.",
            "categories": ["Sports", "Basketball", "Equipment"],
            "price": Decimal("69.99"),
            "images": ["https://images.unsplash.com/photo-1546519638-68e109498ffc?w=800"],
            "stock": 120,
            "attributes": {"brand": "Wilson", "size": "Official (29.5 inches)", "material": "Composite leather"}
        },
        {
            "name": "Spalding NBA Basketball Hoop",
            "description": "Adjustable height portable basketball system, weather-resistant.",
            "categories": ["Sports", "Basketball", "Equipment"],
            "price": Decimal("499.99"),
            "images": ["https://images.unsplash.com/photo-1515523110800-9415d13b84a8?w=800"],
            "stock": 25,
            "attributes": {"brand": "Spalding", "adjustment": "7.5-10 feet", "backboard": "54-inch acrylic"}
        },
        
        # Beauty & Personal Care (5 products)
        {
            "name": "Dyson Supersonic Hair Dryer",
            "description": "Fast-drying hair dryer with intelligent heat control, magnetic attachments.",
            "categories": ["Beauty", "Hair Care", "Electronics"],
            "price": Decimal("429.99"),
            "images": ["https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?w=800"],
            "stock": 40,
            "attributes": {"brand": "Dyson", "heat_control": "Intelligent", "attachments": "5"}
        },
        {
            "name": "Fenty Beauty Pro Filt'r Foundation",
            "description": "Long-wear foundation with 50 shades, soft-matte finish.",
            "categories": ["Beauty", "Makeup", "Foundation"],
            "price": Decimal("39.99"),
            "images": ["https://images.unsplash.com/photo-1596462502278-27bfdc403348?w=800"],
            "stock": 300,
            "attributes": {"brand": "Fenty Beauty", "shades": "50", "finish": "Soft-matte", "size": "32ml"}
        },
        {
            "name": "CeraVe Moisturizing Cream",
            "description": "Daily face and body moisturizer with hyaluronic acid and ceramides.",
            "categories": ["Beauty", "Skincare", "Moisturizers"],
            "price": Decimal("18.99"),
            "images": ["https://images.unsplash.com/photo-1556228841-75a0c4f1f4d8?w=800"],
            "stock": 400,
            "attributes": {"brand": "CeraVe", "size": "16oz", "skin_type": "All types"}
        },
        {
            "name": "Philips Sonicare DiamondClean",
            "description": "Premium electric toothbrush with 5 modes, wireless charging.",
            "categories": ["Beauty", "Personal Care", "Oral Care"],
            "price": Decimal("199.99"),
            "images": ["https://images.unsplash.com/photo-1607613009820-a29f7bb81c04?w=800"],
            "stock": 80,
            "attributes": {"brand": "Philips", "modes": "5", "battery": "2 weeks", "charging": "Wireless"}
        },
        
        # Additional 45 products to reach 100
        {
            "name": "Samsung Odyssey G9 Gaming Monitor",
            "description": "49-inch ultra-wide curved gaming monitor with 240Hz refresh rate.",
            "categories": ["Electronics", "Computers", "Gaming"],
            "price": Decimal("1299.99"),
            "images": ["https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=800"],
            "stock": 15,
            "attributes": {"brand": "Samsung", "size": "49-inch", "resolution": "5120x1440", "refresh_rate": "240Hz"}
        },
        {
            "name": "Logitech MX Master 3S",
            "description": "Premium wireless mouse with ultra-quiet clicks and 8K DPI sensor.",
            "categories": ["Electronics", "Computers", "Office"],
            "price": Decimal("99.99"),
            "images": ["https://images.unsplash.com/photo-1527814050087-3793815479db?w=800"],
            "stock": 200,
            "attributes": {"brand": "Logitech", "dpi": "8000", "battery": "70 days", "connectivity": "Bluetooth"}
        },
        {
            "name": "Keychron K8 Pro Mechanical Keyboard",
            "description": "Wireless hot-swappable mechanical keyboard with QMK/VIA support.",
            "categories": ["Electronics", "Computers", "Office"],
            "price": Decimal("109.99"),
            "images": ["https://images.unsplash.com/photo-1595225476474-87563907a212?w=800"],
            "stock": 100,
            "attributes": {"brand": "Keychron", "switches": "Hot-swappable", "layout": "TKL", "backlight": "RGB"}
        },
        {
            "name": "Canon EOS R6 Mark II",
            "description": "Full-frame mirrorless camera with 24MP sensor and 40fps burst.",
            "categories": ["Electronics", "Cameras"],
            "price": Decimal("2499.99"),
            "images": ["https://images.unsplash.com/photo-1606986628928-03176959efb9?w=800"],
            "stock": 20,
            "attributes": {"brand": "Canon", "sensor": "Full-frame 24MP", "video": "4K 60fps", "burst": "40fps"}
        },
        {
            "name": "Sony A7 IV",
            "description": "Versatile full-frame camera for both photos and video.",
            "categories": ["Electronics", "Cameras"],
            "price": Decimal("2498.00"),
            "images": ["https://images.unsplash.com/photo-1502920917128-1aa500764cbd?w=800"],
            "stock": 25,
            "attributes": {"brand": "Sony", "sensor": "Full-frame 33MP", "video": "4K 60fps", "stabilization": "5-axis"}
        },
        {
            "name": "DJI Mini 3 Pro",
            "description": "Lightweight drone with 4K HDR video and obstacle sensing.",
            "categories": ["Electronics", "Cameras", "Drones"],
            "price": Decimal("759.00"),
            "images": ["https://images.unsplash.com/photo-1473968512647-3e447244af8f?w=800"],
            "stock": 50,
            "attributes": {"brand": "DJI", "weight": "249g", "video": "4K 60fps", "flight_time": "34 minutes"}
        },
        {
            "name": "GoPro HERO 12 Black",
            "description": "Waterproof action camera with 5.3K video and HyperSmooth 6.0.",
            "categories": ["Electronics", "Cameras", "Action"],
            "price": Decimal("399.99"),
            "images": ["https://images.unsplash.com/photo-1585314062340-f1a5a7c9328d?w=800"],
            "stock": 80,
            "attributes": {"brand": "GoPro", "video": "5.3K 60fps", "waterproof": "10m", "stabilization": "HyperSmooth 6.0"}
        },
        {
            "name": "Instant Pot Duo Plus",
            "description": "9-in-1 pressure cooker with sous vide and sterilizer functions.",
            "categories": ["Home", "Kitchen", "Appliances"],
            "price": Decimal("119.99"),
            "images": ["https://images.unsplash.com/photo-1585515320310-259814833e62?w=800"],
            "stock": 150,
            "attributes": {"brand": "Instant Pot", "capacity": "6 quart", "functions": "9", "presets": "15"}
        },
        {
            "name": "Vitamix E310 Explorian",
            "description": "Professional-grade blender with 48oz container and variable speed.",
            "categories": ["Home", "Kitchen", "Appliances"],
            "price": Decimal("349.95"),
            "images": ["https://images.unsplash.com/photo-1570222094114-d054a817e56b?w=800"],
            "stock": 75,
            "attributes": {"brand": "Vitamix", "capacity": "48oz", "motor": "2HP", "warranty": "5 years"}
        },
        {
            "name": "Nespresso VertuoPlus",
            "description": "Single-serve coffee maker with barcode scanning technology.",
            "categories": ["Home", "Kitchen", "Coffee"],
            "price": Decimal("179.99"),
            "images": ["https://images.unsplash.com/photo-1517668808822-9ebb02f2a0e6?w=800"],
            "stock": 120,
            "attributes": {"brand": "Nespresso", "capacity": "40oz", "sizes": "5", "heating": "15-20 seconds"}
        },
        {
            "name": "All-Clad D3 Stainless Cookware Set",
            "description": "10-piece tri-ply stainless steel cookware set with lifetime warranty.",
            "categories": ["Home", "Kitchen", "Cookware"],
            "price": Decimal("699.95"),
            "images": ["https://images.unsplash.com/photo-1584990347449-39b4aa02cd1b?w=800"],
            "stock": 45,
            "attributes": {"brand": "All-Clad", "pieces": "10", "material": "Tri-ply stainless", "oven_safe": "600°F"}
        },
        {
            "name": "KitchenAid Stand Mixer",
            "description": "Classic 5-quart stand mixer with tilt-head design and 10 speeds.",
            "categories": ["Home", "Kitchen", "Baking"],
            "price": Decimal("429.99"),
            "images": ["https://images.unsplash.com/photo-1578269174936-2709b6aeb913?w=800"],
            "stock": 90,
            "attributes": {"brand": "KitchenAid", "capacity": "5 quart", "speeds": "10", "power": "325W"}
        },
        {
            "name": "Ninja Foodi Smart XL Grill",
            "description": "6-in-1 indoor grill with smart cook system and air fryer.",
            "categories": ["Home", "Kitchen", "Appliances"],
            "price": Decimal("299.99"),
            "images": ["https://images.unsplash.com/photo-1604762524889-f0c30e04b4c6?w=800"],
            "stock": 65,
            "attributes": {"brand": "Ninja", "functions": "6", "capacity": "4 servings", "temp": "500°F"}
        },
        {
            "name": "Hydro Flask 32oz Wide Mouth",
            "description": "Insulated stainless steel water bottle keeps drinks cold 24 hours.",
            "categories": ["Sports", "Outdoor", "Drinkware"],
            "price": Decimal("44.95"),
            "images": ["https://images.unsplash.com/photo-1602143407151-7111542de6e8?w=800"],
            "stock": 300,
            "attributes": {"brand": "Hydro Flask", "capacity": "32oz", "insulation": "TempShield", "material": "Stainless steel"}
        },
        {
            "name": "YETI Tundra 45 Cooler",
            "description": "Rotomolded cooler with 3 inches of PermaFrost insulation.",
            "categories": ["Sports", "Outdoor", "Camping"],
            "price": Decimal("325.00"),
            "images": ["https://images.unsplash.com/photo-1565026952422-ef46d9fb0e1d?w=800"],
            "stock": 40,
            "attributes": {"brand": "YETI", "capacity": "45 quart", "cans": "54", "ice_retention": "Up to 10 days"}
        },
        {
            "name": "Patagonia Down Sweater Jacket",
            "description": "Lightweight insulated jacket with 800-fill-power goose down.",
            "categories": ["Clothing", "Men", "Outdoor", "Jackets"],
            "price": Decimal("279.00"),
            "images": ["https://images.unsplash.com/photo-1591047139829-d91aecb6caea?w=800"],
            "stock": 85,
            "attributes": {"brand": "Patagonia", "insulation": "800-fill goose down", "weight": "13.6oz", "fabric": "100% Recycled Polyester"}
        },
        {
            "name": "Arc'teryx Beta AR Jacket",
            "description": "Waterproof breathable hardshell for all-mountain use.",
            "categories": ["Clothing", "Men", "Outdoor", "Jackets"],
            "price": Decimal("575.00"),
            "images": ["https://images.unsplash.com/photo-1551028719-00167b16eac5?w=800"],
            "stock": 55,
            "attributes": {"brand": "Arc'teryx", "membrane": "Gore-Tex Pro", "weight": "445g", "waterproof": "Yes"}
        },
        {
            "name": "Lululemon Define Jacket",
            "description": "Sleek athletic jacket with cottony-soft handfeel and shape retention.",
            "categories": ["Clothing", "Women", "Activewear"],
            "price": Decimal("128.00"),
            "images": ["https://images.unsplash.com/photo-1556821840-3a63f95609a7?w=800"],
            "stock": 120,
            "attributes": {"brand": "Lululemon", "fabric": "Lycra", "fit": "Slim", "features": "Thumbholes"}
        },
        {
            "name": "Lululemon Align Leggings 25\"",
            "description": "Ultra-soft Nulu fabric leggings for yoga and low-impact workouts.",
            "categories": ["Clothing", "Women", "Activewear", "Leggings"],
            "price": Decimal("98.00"),
            "images": ["https://images.unsplash.com/photo-1506629082955-511b1aa562c8?w=800"],
            "stock": 200,
            "attributes": {"brand": "Lululemon", "fabric": "Nulu", "rise": "High-rise", "length": "25 inches"}
        },
        {
            "name": "Nike Air Zoom Pegasus 40",
            "description": "Responsive running shoes with ReactX foam and Zoom Air units.",
            "categories": ["Sports", "Shoes", "Running"],
            "price": Decimal("139.99"),
            "images": ["https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=800"],
            "stock": 180,
            "attributes": {"brand": "Nike", "cushioning": "ReactX + Zoom Air", "weight": "10oz", "drop": "10mm"}
        },
        {
            "name": "Adidas Ultraboost Light",
            "description": "Lightweight running shoe with energy-returning Boost cushioning.",
            "categories": ["Sports", "Shoes", "Running"],
            "price": Decimal("190.00"),
            "images": ["https://images.unsplash.com/photo-1608231387042-66d1773070a5?w=800"],
            "stock": 160,
            "attributes": {"brand": "Adidas", "cushioning": "Boost", "weight": "8.8oz", "upper": "Primeknit+"}
        },
        {
            "name": "Hoka Clifton 9",
            "description": "Max-cushioned daily trainer with lightweight EVA foam.",
            "categories": ["Sports", "Shoes", "Running"],
            "price": Decimal("144.95"),
            "images": ["https://images.unsplash.com/photo-1460353581641-37baddab0fa2?w=800"],
            "stock": 140,
            "attributes": {"brand": "Hoka", "cushioning": "EVA foam", "weight": "8.7oz", "drop": "5mm"}
        },
        {
            "name": "Therabody Theragun PRO",
            "description": "Professional-grade percussive therapy device with OLED screen.",
            "categories": ["Sports", "Fitness", "Recovery"],
            "price": Decimal("599.00"),
            "images": ["https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=800"],
            "stock": 70,
            "attributes": {"brand": "Therabody", "amplitude": "16mm", "speeds": "5", "battery": "150 minutes"}
        },
        {
            "name": "Peloton Guide",
            "description": "AI-powered strength training system with movement tracking.",
            "categories": ["Sports", "Fitness", "Equipment"],
            "price": Decimal("295.00"),
            "images": ["https://images.unsplash.com/photo-1517836357463-d25dfeac3438?w=800"],
            "stock": 95,
            "attributes": {"brand": "Peloton", "camera": "Yes", "tracking": "Movement Tracker", "content": "Thousands of classes"}
        },
        {
            "name": "Manduka PRO Yoga Mat",
            "description": "Professional-grade yoga mat with lifetime guarantee and superior grip.",
            "categories": ["Sports", "Fitness", "Yoga"],
            "price": Decimal("126.00"),
            "images": ["https://images.unsplash.com/photo-1601925260368-ae2f83cf8b7f?w=800"],
            "stock": 180,
            "attributes": {"brand": "Manduka", "thickness": "6mm", "material": "PVC", "warranty": "Lifetime"}
        },
        {
            "name": "Bowflex SelectTech 552 Dumbbells",
            "description": "Adjustable dumbbells replace 15 sets, 5-52.5 lbs per dumbbell.",
            "categories": ["Sports", "Fitness", "Equipment"],
            "price": Decimal("399.00"),
            "images": ["https://images.unsplash.com/photo-1583454110551-21f2fa2afe61?w=800"],
            "stock": 60,
            "attributes": {"brand": "Bowflex", "weight_range": "5-52.5 lbs", "increments": "2.5 lbs", "sets": "15"}
        },
        {
            "name": "Herman Miller Aeron Chair",
            "description": "Ergonomic office chair with PostureFit support and 12-year warranty.",
            "categories": ["Home", "Office", "Furniture"],
            "price": Decimal("1495.00"),
            "images": ["https://images.unsplash.com/photo-1580480055273-228ff5388ef8?w=800"],
            "stock": 35,
            "attributes": {"brand": "Herman Miller", "size": "B (Medium)", "adjustments": "8", "warranty": "12 years"}
        },
        {
            "name": "Autonomous SmartDesk Pro",
            "description": "Electric standing desk with dual motors and programmable heights.",
            "categories": ["Home", "Office", "Furniture"],
            "price": Decimal("699.00"),
            "images": ["https://images.unsplash.com/photo-1595515106969-1ce29566ff1c?w=800"],
            "stock": 50,
            "attributes": {"brand": "Autonomous", "motors": "Dual", "height_range": "24.4-50.1 inches", "capacity": "300 lbs"}
        },
        {
            "name": "West Elm Mid-Century Sofa",
            "description": "Modern 82-inch sofa with tapered legs and plush cushions.",
            "categories": ["Home", "Furniture", "Living Room"],
            "price": Decimal("1299.00"),
            "images": ["https://images.unsplash.com/photo-1555041469-a586c61ea9bc?w=800"],
            "stock": 25,
            "attributes": {"brand": "West Elm", "size": "82 inches", "material": "Performance velvet", "style": "Mid-century"}
        },
        {
            "name": "Casper Wave Hybrid Mattress Queen",
            "description": "Luxury hybrid mattress with ergonomic gel pods and zoned support.",
            "categories": ["Home", "Furniture", "Bedroom"],
            "price": Decimal("1895.00"),
            "images": ["https://images.unsplash.com/photo-1505693416388-ac5ce068fe85?w=800"],
            "stock": 40,
            "attributes": {"brand": "Casper", "size": "Queen", "type": "Hybrid", "trial": "100 nights"}
        },
        {
            "name": "Philips Hue Starter Kit",
            "description": "Smart lighting system with 4 color bulbs and bridge.",
            "categories": ["Electronics", "Smart Home", "Lighting"],
            "price": Decimal("199.99"),
            "images": ["https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800"],
            "stock": 110,
            "attributes": {"brand": "Philips", "bulbs": "4", "colors": "16 million", "voice": "Alexa, Google, Siri"}
        },
        {
            "name": "Ring Video Doorbell Pro 2",
            "description": "HD+ video doorbell with 3D motion detection and bird's eye view.",
            "categories": ["Electronics", "Smart Home", "Security"],
            "price": Decimal("249.99"),
            "images": ["https://images.unsplash.com/photo-1558002038-1055907df827?w=800"],
            "stock": 130,
            "attributes": {"brand": "Ring", "resolution": "1536p HD+", "field_of_view": "150° vertical", "features": "3D Motion"}
        },
        {
            "name": "Anova Precision Cooker Pro",
            "description": "Professional sous vide circulator with 1200W heating element.",
            "categories": ["Home", "Kitchen", "Appliances"],
            "price": Decimal("399.00"),
            "images": ["https://images.unsplash.com/photo-1585515320310-259814833e62?w=800"],
            "stock": 85,
            "attributes": {"brand": "Anova", "power": "1200W", "capacity": "100 liters", "connectivity": "WiFi + Bluetooth"}
        },
        {
            "name": "Weber Genesis II E-335",
            "description": "Premium gas grill with 3 burners and 669 sq in cooking area.",
            "categories": ["Home", "Outdoor", "Grilling"],
            "price": Decimal("999.00"),
            "images": ["https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=800"],
            "stock": 30,
            "attributes": {"brand": "Weber", "burners": "3", "cooking_area": "669 sq in", "fuel": "Liquid Propane"}
        },
        {
            "name": "Dyson V15 Detect",
            "description": "Cordless vacuum with laser dust detection and LCD screen.",
            "categories": ["Home", "Appliances", "Cleaning"],
            "price": Decimal("749.99"),
            "images": ["https://images.unsplash.com/photo-1558317374-067fb5f30001?w=800"],
            "stock": 95,
            "attributes": {"brand": "Dyson", "runtime": "60 minutes", "bin": "0.2 gallons", "features": "Laser detection"}
        },
        {
            "name": "iRobot Roomba j7+",
            "description": "Self-emptying robot vacuum with AI obstacle avoidance.",
            "categories": ["Home", "Appliances", "Cleaning"],
            "price": Decimal("799.99"),
            "images": ["https://images.unsplash.com/photo-1558317374-067fb5f30001?w=800"],
            "stock": 75,
            "attributes": {"brand": "iRobot", "suction": "10x", "self_empty": "60 days", "mapping": "Smart Mapping"}
        },
        {
            "name": "Sonos Arc Soundbar",
            "description": "Premium soundbar with Dolby Atmos and voice control.",
            "categories": ["Electronics", "Audio", "Home Theater"],
            "price": Decimal("899.00"),
            "images": ["https://images.unsplash.com/photo-1545454675-3531b543be5d?w=800"],
            "stock": 65,
            "attributes": {"brand": "Sonos", "channels": "11.1", "dolby": "Atmos", "voice": "Alexa, Google"}
        },
        {
            "name": "Kindle Paperwhite Signature Edition",
            "description": "Premium e-reader with 6.8-inch display and wireless charging.",
            "categories": ["Electronics", "Books", "E-readers"],
            "price": Decimal("189.99"),
            "images": ["https://images.unsplash.com/photo-1592856093516-89a662ab3ea7?w=800"],
            "stock": 200,
            "attributes": {"brand": "Amazon", "screen": "6.8 inch", "storage": "32GB", "charging": "Wireless"}
        },
        {
            "name": "Bose QuietComfort Earbuds II",
            "description": "Premium wireless earbuds with personalized noise cancellation.",
            "categories": ["Electronics", "Audio", "Earbuds"],
            "price": Decimal("299.00"),
            "images": ["https://images.unsplash.com/photo-1590658268037-6bf12165a8df?w=800"],
            "stock": 140,
            "attributes": {"brand": "Bose", "anc": "Personalized", "battery": "6 hours + 18", "fit": "CustomTune"}
        },
        {
            "name": "Breville Barista Express",
            "description": "Espresso machine with built-in grinder and steam wand.",
            "categories": ["Home", "Kitchen", "Coffee"],
            "price": Decimal("699.95"),
            "images": ["https://images.unsplash.com/photo-1517668808822-9ebb02f2a0e6?w=800"],
            "stock": 55,
            "attributes": {"brand": "Breville", "grinder": "Conical burr", "boiler": "Thermocoil", "pressure": "15 bars"}
        },
        {
            "name": "Le Creuset Dutch Oven 5.5qt",
            "description": "Enameled cast iron Dutch oven for braising, baking, and roasting.",
            "categories": ["Home", "Kitchen", "Cookware"],
            "price": Decimal("379.95"),
            "images": ["https://images.unsplash.com/photo-1584990347449-39b4aa0cd1b?w=800"],
            "stock": 90,
            "attributes": {"brand": "Le Creuset", "capacity": "5.5 quart", "material": "Enameled cast iron", "oven_safe": "500°F"}
        },
        {
            "name": "Shun Classic Chef's Knife 8\"",
            "description": "VG-MAX Damascus steel chef's knife with pakkawood handle.",
            "categories": ["Home", "Kitchen", "Cutlery"],
            "price": Decimal("159.95"),
            "images": ["https://images.unsplash.com/photo-1593618998160-e34014e67546?w=800"],
            "stock": 110,
            "attributes": {"brand": "Shun", "blade": "VG-MAX Damascus", "length": "8 inches", "origin": "Japan"}
        },
        {
            "name": "Bose SoundLink Revolve+",
            "description": "360-degree portable Bluetooth speaker with 16-hour battery.",
            "categories": ["Electronics", "Audio", "Speakers"],
            "price": Decimal("329.00"),
            "images": ["https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=800"],
            "stock": 95,
            "attributes": {"brand": "Bose", "battery": "16 hours", "water_resistant": "IPX4", "features": "360-degree sound"}
        },
        {
            "name": "Fender Player Stratocaster",
            "description": "Classic electric guitar with alder body and maple neck.",
            "categories": ["Electronics", "Music", "Guitars"],
            "price": Decimal("849.99"),
            "images": ["https://images.unsplash.com/photo-1564186763535-ebb21ef5277f?w=800"],
            "stock": 35,
            "attributes": {"brand": "Fender", "body": "Alder", "pickups": "3 Single-Coil", "finish": "Gloss polyester"}
        },
        {
            "name": "Osprey Atmos AG 65 Backpack",
            "description": "Ventilated backpacking pack with Anti-Gravity suspension system.",
            "categories": ["Sports", "Outdoor", "Camping"],
            "price": Decimal("290.00"),
            "images": ["https://images.unsplash.com/photo-1622260614927-5b57f08c7d99?w=800"],
            "stock": 65,
            "attributes": {"brand": "Osprey", "capacity": "65 liters", "suspension": "Anti-Gravity AG", "warranty": "Lifetime"}
        },
    ]
    
    print(f"Creating {len(products_data)} products...")
    
    # Check if products already exist
    existing_count = db.query(Product).count()
    if existing_count > 0:
        print(f"Database already has {existing_count} products. Clearing and adding new ones...")
        db.query(Product).delete()
        db.commit()
        print("Cleared existing products.")
    
    # Create products
    created_count = 0
    for product_data in products_data:
        product = Product(**product_data)
        db.add(product)
        created_count += 1
    
    db.commit()
    print(f"✓ Successfully created {created_count} products!")
    
    # Print summary by category
    print("\nProducts by category:")
    categories = {}
    for product in db.query(Product).all():
        for cat in product.categories:
            categories[cat] = categories.get(cat, 0) + 1
    
    for category, count in sorted(categories.items()):
        print(f"  {category}: {count} products")
    
    print(f"\nTotal products in database: {db.query(Product).count()}")


if __name__ == "__main__":
    db = SessionLocal()
    try:
        create_products(db)
    finally:
        db.close()
