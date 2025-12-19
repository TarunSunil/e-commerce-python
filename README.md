# E-Commerce Management System

A full-stack e-commerce platform now running on FastAPI (Python), PostgreSQL, React TypeScript, and a Python recommendation microservice. Features modern UI with smooth animations, JWT authentication, product management, shopping cart, order processing, and content-based product recommendations.

## 🚀 Tech Stack

### Backend
- **Python 3.11** + **FastAPI**
- **SQLAlchemy 2 + Alembic** for data access and migrations
- **PostgreSQL** for relational storage
- **python-jose + passlib[bcrypt]** for JWT authentication and password hashing

### Frontend
- **React 18** with **TypeScript**
- **Vite** for fast development and building
- **Tailwind CSS** for modern, responsive styling
- **Framer Motion** for smooth animations and page transitions
- **React Router v6** for client-side routing
- **Axios** for API communication

### Recommender
- **Python 3.11** + **FastAPI**
- Content-based recommendation using category similarity
- Jaccard similarity for product matching

### DevOps
- **Docker** & **Docker Compose** for containerization
- **GitHub Actions** for CI/CD
- **Nginx** for frontend serving

## 📁 Project Structure

```
ecommerce-system/
├── backend/                 # FastAPI application (PostgreSQL)
│   ├── app/
│   │   ├── main.py         # FastAPI app wiring
│   │   ├── models/         # SQLAlchemy models
│   │   ├── schemas/        # Pydantic schemas
│   │   ├── services/       # Business logic
│   │   ├── routers/        # Route handlers
│   │   └── security.py     # JWT helpers
│   ├── requirements.txt
│   ├── Dockerfile
│   └── alembic/            # DB migrations
├── frontend/                # React TypeScript app
│   ├── src/
│   │   ├── components/     # Reusable UI components
│   │   ├── pages/          # Page components
│   │   ├── services/       # API services
│   │   ├── types/          # TypeScript types
│   │   └── App.tsx         # Main app with routing
│   └── package.json
├── recommender/             # Python FastAPI microservice
│   ├── app.py              # FastAPI application
│   ├── recommender.py      # Recommendation logic
│   └── requirements.txt
├── docker-compose.yml      # Local development setup
└── README.md
```

## 🛠️ Local Setup

### Prerequisites
- Node.js 20+
- Python 3.11+
- Docker & Docker Compose (recommended)
- PostgreSQL (if running services manually)

### Option 1: Docker Compose (Recommended)

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd E-commerce
   ```

2. **Start all services**
   ```bash
   docker-compose up -d
   ```

3. **Access the application**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8080/api
   - Recommender: http://localhost:8000
   - PostgreSQL: localhost:5432 (user `ecom_user` / password `ecom_pass`)

### Option 2: Manual Setup

#### Backend (FastAPI)
```bash
cd backend
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8080
```

#### Frontend
```bash
cd frontend
npm install
npm run dev
```

#### Recommender
```bash
cd recommender
pip install -r requirements.txt
uvicorn app:app --host 0.0.0.0 --port 8000
```

#### PostgreSQL
Ensure PostgreSQL is running on `localhost:5432` (or adjust `DATABASE_URL`); default local DSN: `postgresql+psycopg2://ecom_user:ecom_pass@localhost:5432/ecommerce`.

## 📡 API Endpoints

### Authentication
- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - Login and get JWT token

### Products
- `GET /api/products` - List products (with pagination, category filter, search)
  - Query params: `page`, `size`, `category`, `q`
- `GET /api/products/{id}` - Get product details
- `POST /api/products` - Create product (Admin only)
- `PUT /api/products/{id}` - Update product (Admin only)
- `DELETE /api/products/{id}` - Delete product (Admin only)

### Cart
- `POST /api/cart` - Add item to cart (requires auth)
- `GET /api/cart` - Get user's cart (requires auth)
- `GET /api/cart/total` - Get cart total (requires auth)
- `DELETE /api/cart/{productId}` - Remove item from cart (requires auth)
- `DELETE /api/cart` - Clear cart (requires auth)

### Orders
- `POST /api/orders` - Create order from cart (requires auth)
- `GET /api/orders/{userId}` - Get user's order history (requires auth)
- `GET /api/orders/order/{orderId}` - Get order details (requires auth)

### Recommendations
- `GET /api/recommend/{productId}` - Get product recommendations
- `GET /api/recommend/user/{userId}` - Get user-based recommendations (requires auth)

## 🎨 Frontend Features

### Pages
- **Home Page**: Product listing with search and category filters
- **Product Detail**: Individual product view with recommendations
- **Cart**: Shopping cart with quantity management
- **Checkout**: Order placement form
- **Login/Register**: Authentication pages
- **Admin Panel**: Product CRUD operations (Admin only)
- **Order History**: User's past orders

### Animations & UX
- Smooth page transitions using Framer Motion
- Animated product cards with hover effects
- Loading states and error handling
- Responsive mobile-first design
- Protected routes with authentication checks

## 🔐 Authentication

The system uses JWT (JSON Web Tokens) for authentication:

1. Register/Login to get a JWT token
2. Token is stored in `localStorage`
3. Token is automatically included in API requests via Axios interceptors
4. Protected routes check authentication status

### Admin Access
To create an admin user, you can either:
- Manually update the `users` table in PostgreSQL to add `"ADMIN"` to the `roles` array for a user
- Or modify the registration service to assign admin role for specific emails

## 🤖 Recommendation System

The recommender uses **content-based filtering**:

1. **Product-based recommendations**: Finds similar products based on category overlap (Jaccard similarity)
2. **User-based recommendations**: Suggests products matching user preferences or popular items

### How it works:
- Extracts product categories
- Calculates similarity scores between products
- Returns top-N most similar products

## 🐳 Docker Deployment

### Build images
```bash
docker-compose build
```

### Run services
```bash
docker-compose up -d
```

### View logs
```bash
docker-compose logs -f [service-name]
```

### Stop services
```bash
docker-compose down
```

## 🚢 Production Deployment

### Frontend (Vercel)
1. Connect your GitHub repository to Vercel
2. Set build command: `cd frontend && npm install && npm run build`
3. Set output directory: `frontend/dist`
4. Add environment variable: `VITE_API_URL=https://your-backend-url/api`

### Backend (Render/Railway/Heroku)
1. Set up MongoDB Atlas (cloud MongoDB)
2. Configure environment variables:
   - `SPRING_DATA_MONGODB_URI`: MongoDB connection string
   - `JWT_SECRET`: Strong secret key (min 256 bits)
3. Deploy using Docker or build directly

### Recommender (Render/Railway)
1. Set environment variable: `BACKEND_URL=https://your-backend-url/api`
2. Deploy as Python service

## 📊 Metrics to Collect (Future)

For production monitoring, consider tracking:
- API latency (avg/P95) for product listing and search
- Auth success rate
- Error rate for critical endpoints
- Recommender coverage (how often recommendations returned)
- Business metrics: Add-to-cart rate, checkout success rate

## 🧪 Testing

### Backend
```bash
cd backend
mvn test
```

### Frontend
```bash
cd frontend
npm run lint
npm test  # If test suite is added
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📝 License

This project is open source and available under the MIT License.

## 👤 Author

Tarun Sunil

## 🙏 Acknowledgments

- Reference implementation: [Ecommerce-Cart-System](https://github.com/Radhz16/Ecommerce-Cart-System)
- Built with modern best practices and improved UI/UX


