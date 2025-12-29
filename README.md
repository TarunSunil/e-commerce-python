# E-Commerce Management System

A full-stack e-commerce management system built with FastAPI (Python), PostgreSQL, and React.

## Features

### Backend (FastAPI + PostgreSQL)
- **User Authentication**: JWT-based authentication with secure password hashing
- **Product Management**: Full CRUD operations for products with category support
- **Category Management**: Organize products into categories
- **Shopping Cart**: Add, update, and remove items from cart
- **Order Management**: Place orders, view order history, and track order status
- **Admin Panel**: Admin users can manage products, categories, and orders
- **RESTful API**: Well-documented API with automatic OpenAPI documentation

### Frontend (React)
- **Responsive Design**: Mobile-friendly user interface
- **User Authentication**: Login and registration pages
- **Product Browsing**: Browse products by category with filtering
- **Shopping Cart**: Interactive cart with quantity management
- **Checkout Process**: Simple and secure checkout flow
- **Order History**: View past orders and their status
- **Admin Dashboard**: Manage products and orders (admin only)

## Technology Stack

### Backend
- **FastAPI**: Modern Python web framework for building APIs
- **PostgreSQL**: Robust relational database
- **SQLAlchemy**: SQL toolkit and ORM
- **Alembic**: Database migration tool
- **Pydantic**: Data validation using Python type annotations
- **JWT**: Secure authentication tokens
- **Passlib**: Password hashing library

### Frontend
- **React**: JavaScript library for building user interfaces
- **React Router**: Navigation and routing
- **Axios**: HTTP client for API calls
- **Context API**: State management for authentication and cart

## Prerequisites

- Python 3.11+
- Node.js 18+
- PostgreSQL 15+
- Docker & Docker Compose (optional)

## Quick Start

### Automated Setup with Docker (Recommended)

1. Clone the repository:
```bash
git clone https://github.com/TarunSunil/e-commerce-python.git
cd e-commerce-python
```

2. Run the quick start script:
```bash
./start.sh
```

This will:
- Build and start all services using Docker Compose
- Seed the database with sample data
- Display access URLs and default credentials

The application will be available at:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Documentation: http://localhost:8000/docs

### Automated Manual Setup

If you prefer not to use Docker:

```bash
./setup.sh
```

This will guide you through setting up the backend and frontend manually.

## Installation

### Option 1: Using Docker (Recommended)

1. Clone the repository:
```bash
git clone https://github.com/TarunSunil/e-commerce-python.git
cd e-commerce-python
```

2. Start all services using Docker Compose:
```bash
docker-compose up -d
```

3. Seed the database:
```bash
docker-compose exec backend python seed.py
```

4. The application will be available at:
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

### Option 2: Manual Installation

#### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file from the example:
```bash
cp .env.example .env
```

5. Update the `.env` file with your database credentials:
```
DATABASE_URL=postgresql://ecommerce_user:ecommerce_password@localhost:5432/ecommerce_db
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

6. Set up the PostgreSQL database:
```bash
# Create database
createdb ecommerce_db

# Or use psql
psql -U postgres
CREATE DATABASE ecommerce_db;
CREATE USER ecommerce_user WITH PASSWORD 'ecommerce_password';
GRANT ALL PRIVILEGES ON DATABASE ecommerce_db TO ecommerce_user;
\q
```

7. Run database migrations (tables will be created automatically):
```bash
python -c "from app.models.models import Base; from app.core.database import engine; Base.metadata.create_all(bind=engine)"
```

8. Seed the database with sample data:
```bash
python seed.py
```

9. Start the backend server:
```bash
uvicorn app.main:app --reload
```

The API will be available at http://localhost:8000

#### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Create a `.env` file:
```bash
echo "REACT_APP_API_URL=http://localhost:8000" > .env
```

4. Start the development server:
```bash
npm start
```

The frontend will be available at http://localhost:3000

## Default Admin Credentials

After seeding the database, you can login with:
- **Username**: `admin`
- **Password**: `admin123`

**Important**: Change these credentials in production!

## API Documentation

Once the backend is running, you can access:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## API Endpoints

### Authentication
- `POST /api/auth/register` - Register a new user
- `POST /api/auth/login` - Login and get access token
- `GET /api/auth/me` - Get current user info

### Products
- `GET /api/products` - Get all products
- `GET /api/products/{id}` - Get product by ID
- `POST /api/products` - Create product (admin only)
- `PUT /api/products/{id}` - Update product (admin only)
- `DELETE /api/products/{id}` - Delete product (admin only)

### Categories
- `GET /api/categories` - Get all categories
- `GET /api/categories/{id}` - Get category by ID
- `POST /api/categories` - Create category (admin only)
- `PUT /api/categories/{id}` - Update category (admin only)
- `DELETE /api/categories/{id}` - Delete category (admin only)

### Cart
- `GET /api/cart` - Get user's cart
- `POST /api/cart/items` - Add item to cart
- `PUT /api/cart/items/{id}` - Update cart item quantity
- `DELETE /api/cart/items/{id}` - Remove item from cart
- `DELETE /api/cart` - Clear cart

### Orders
- `GET /api/orders` - Get user's orders
- `GET /api/orders/{id}` - Get order by ID
- `POST /api/orders` - Create order from cart
- `GET /api/orders/admin/all` - Get all orders (admin only)
- `PUT /api/orders/{id}/status` - Update order status (admin only)

## Project Structure

```
e-commerce-python/
├── backend/
│   ├── app/
│   │   ├── api/           # API endpoints
│   │   │   ├── auth.py
│   │   │   ├── products.py
│   │   │   ├── categories.py
│   │   │   ├── cart.py
│   │   │   └── orders.py
│   │   ├── core/          # Core configuration
│   │   │   ├── config.py
│   │   │   ├── database.py
│   │   │   └── security.py
│   │   ├── crud/          # Database operations
│   │   │   └── crud.py
│   │   ├── models/        # Database models
│   │   │   └── models.py
│   │   ├── schemas/       # Pydantic schemas
│   │   │   └── schemas.py
│   │   └── main.py        # FastAPI application
│   ├── tests/             # Backend tests
│   ├── requirements.txt
│   ├── Dockerfile
│   └── seed.py           # Database seeding script
├── frontend/
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── components/    # React components
│   │   │   ├── Navbar.js
│   │   │   └── ProductCard.js
│   │   ├── context/       # React Context
│   │   │   ├── AuthContext.js
│   │   │   └── CartContext.js
│   │   ├── pages/         # Page components
│   │   │   ├── Home.js
│   │   │   ├── Login.js
│   │   │   ├── Register.js
│   │   │   ├── Cart.js
│   │   │   ├── Checkout.js
│   │   │   └── Orders.js
│   │   ├── services/      # API services
│   │   │   └── api.js
│   │   ├── App.js
│   │   └── index.js
│   ├── package.json
│   └── Dockerfile
├── docker-compose.yml
└── README.md
```

## Development

### Running Tests

Backend tests:
```bash
cd backend
pytest
```

Frontend tests:
```bash
cd frontend
npm test
```

### Database Migrations

To create a new migration:
```bash
cd backend
alembic revision --autogenerate -m "Description of changes"
alembic upgrade head
```

## Production Deployment

1. Update environment variables with production values
2. Set strong SECRET_KEY for JWT tokens
3. Use production-grade database credentials
4. Enable HTTPS/SSL
5. Set up proper CORS origins
6. Configure proper logging
7. Use production WSGI server (e.g., Gunicorn)
8. Set up reverse proxy (e.g., Nginx)

## Security Considerations

- All passwords are hashed using bcrypt
- JWT tokens are used for authentication
- CORS is configured to allow specific origins
- Input validation using Pydantic
- SQL injection protection via SQLAlchemy ORM
- XSS protection in React

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License.

## Support

For issues and questions, please open an issue on GitHub.

## Acknowledgments

- FastAPI for the excellent web framework
- React team for the powerful UI library
- PostgreSQL for the robust database