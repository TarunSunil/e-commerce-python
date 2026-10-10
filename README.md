# E-Commerce Application

A demonstration e-commerce platform with a React frontend, FastAPI backend, PostgreSQL database, and an optional content-based recommender.

The current build is not enabled for real orders. Inventory is seeded demonstration data, card details are not collected, and seller, tax, shipping, returns, and payment settings remain placeholders until professionally confirmed.

## 🏗️ Architecture

This application consists of **3 separate services**:

1. **Backend API** (FastAPI) - Port 8080
   - Handles authentication, products, cart, orders
   - PostgreSQL database for data storage
   
2. **Recommender Service** (FastAPI) - Port 8000
   - AI-powered product recommendations using machine learning
   - Fetches product data from Backend API
   
3. **Frontend** (React + Vite) - Port 5173
   - User interface for browsing, shopping, and checkout
   - Communicates with Backend API

## 📋 Prerequisites

Before starting, ensure you have these installed on your computer:

- **Python 3.11 or higher** - [Download here](https://www.python.org/downloads/)
  - During installation, check "Add Python to PATH"
  - Verify: Open PowerShell and run `python --version`
  
- **Node.js 18 or higher** - [Download here](https://nodejs.org/)
  - Verify: Run `node --version` and `npm --version`
  
- **PostgreSQL 14 or higher** - [Download here](https://www.postgresql.org/download/)
  - Remember the password you set during installation!
  - Verify: Run `psql --version`

- **Git** (optional but recommended) - [Download here](https://git-scm.com/)

## 🚀 Step-by-Step Setup Guide (For Beginners)

### Step 1: Set Up PostgreSQL Database

1. **Open PostgreSQL command line** (Search for "SQL Shell (psql)" in Windows Start menu)

2. **Login** with the password you set during PostgreSQL installation
   - Press Enter for defaults (localhost, 5432, postgres user)
   - Enter your password when prompted

3. **Create the database:**
   ```sql
   CREATE DATABASE ecommerce;
   ```

4. **Create a user for the application:**
   ```sql
   CREATE USER ecom_user WITH PASSWORD 'ecom_pass';
   ```

5. **Grant permissions:**
   ```sql
   GRANT ALL PRIVILEGES ON DATABASE ecommerce TO ecom_user;
   ```

6. **Exit psql:**
   ```sql
   \q
   ```

### Step 2: Set Up Backend API

1. **Open PowerShell** and navigate to the project:
   ```powershell
   cd D:\code\E-commerce\backend
   ```

2. **Create a Python virtual environment:**
   ```powershell
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```
   
   > **Note**: If you get an error about execution policy, run:
   > ```powershell
   > Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   > ```

4. **Install Python dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

5. **Create environment configuration file:**
   - Create a file named `.env` in the `backend` folder
   - Copy this content (adjust if you used different database credentials):
   ```
   DATABASE_URL=postgresql+psycopg2://ecom_user:ecom_pass@localhost:5432/ecommerce
   JWT_SECRET=<generate a secret of at least 32 characters>
   CORS_ORIGINS=["http://localhost:5173","http://localhost:3000"]
   RECOMMENDER_URL=http://localhost:8000
   ```

6. **Run database migrations and start the Backend API:**
   ```powershell
   python -m alembic upgrade head
   uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload
   ```

7. **Verify it's working:**
   - Open your browser and go to: http://localhost:8080/api/docs
   - You should see the FastAPI documentation page!

> **Keep this PowerShell window open** - the backend must stay running!

### Step 3: Set Up Recommender Service

1. **Open a NEW PowerShell window** (don't close the backend one!)

2. **Navigate to recommender folder:**
   ```powershell
   cd D:\code\E-commerce\recommender
   ```

3. **Create a Python virtual environment:**
   ```powershell
   python -m venv venv
   ```

4. **Activate the virtual environment:**
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

5. **Install Python dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

6. **Create environment configuration file:**
   - Create a file named `.env` in the `recommender` folder
   - Add this content:
   ```
   BACKEND_URL=http://localhost:8080/api
   ```

7. **Start the Recommender Service:**
   ```powershell
   uvicorn app:app --host 0.0.0.0 --port 8000 --reload
   ```

8. **Verify it's working:**
   - Open browser: http://localhost:8000/docs
   - You should see the Recommender API documentation!

> **Keep this PowerShell window open too!**

### Step 4: Set Up Frontend

1. **Open a THIRD PowerShell window**

2. **Navigate to frontend folder:**
   ```powershell
   cd D:\code\E-commerce\frontend
   ```

3. **Install Node.js dependencies:**
   ```powershell
   npm install
   ```
   
   > This might take a few minutes - it's downloading packages!

4. **Create environment configuration:**
   - Create a file named `.env` in the `frontend` folder
   - Add this content:
   ```
   VITE_API_URL=http://localhost:8080/api
   ```

5. **Start the Frontend development server:**
   ```powershell
   npm run dev
   ```

6. **Open the application:**
   - Your browser should automatically open
   - If not, go to: http://localhost:5173
   - You should see the e-commerce homepage! 🎉

### Step 5: Test the Application
# E-Commerce Platform

> Full-stack e-commerce application with AI-powered product recommendations, JWT authentication, Redis session caching, and a three-service Docker architecture.

[![FastAPI](https://img.shields.io/badge/FastAPI-backend-009688?style=flat-square&logo=fastapi&logoColor=white&labelColor=0f0f0f)](https://fastapi.tiangolo.com)
[![React](https://img.shields.io/badge/React-frontend-61DAFB?style=flat-square&logo=react&logoColor=black&labelColor=0f0f0f)](https://react.dev)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-database-4169E1?style=flat-square&logo=postgresql&logoColor=white&labelColor=0f0f0f)](https://postgresql.org)
[![Redis](https://img.shields.io/badge/Redis-cache-DC382D?style=flat-square&logo=redis&logoColor=white&labelColor=0f0f0f)](https://redis.io)
[![Docker](https://img.shields.io/badge/Docker-compose-2496ED?style=flat-square&logo=docker&logoColor=white&labelColor=0f0f0f)](https://docker.com)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat-square&logo=python&logoColor=white&labelColor=0f0f0f)](https://python.org)

---

2. **Start Backend** (in PowerShell):
   ```powershell
   cd D:\code\E-commerce\backend
   .\venv\Scripts\Activate.ps1
   python -m alembic upgrade head
   uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload
   ```
## Architecture

Three independent services, orchestrated with Docker Compose:

```
┌─────────────────────────────────────────────────────────┐
│                        Client                           │
│              React + Vite  (port 5173)                  │
└────────────────────┬────────────────────────────────────┘
                     │ REST
          ┌──────────▼──────────┐
          │   Backend API        │  FastAPI · port 8080
          │   Auth · Products    │  PostgreSQL · Redis
          │   Cart · Orders      │
          └──────────┬──────────┘
                     │ internal HTTP
          ┌──────────▼──────────┐
          │  Recommender Service │  FastAPI · port 8000
          │  ML recommendations  │  scikit-learn
          └─────────────────────┘
```

If a database was created by an older version using
`Base.metadata.create_all`, back it up first and run
`python -m alembic stamp head` once. New databases must use
`python -m alembic upgrade head`.

## 🐳 Alternative: Docker Setup (Advanced)
| Service | Port | Tech |
|---|---|---|
| Frontend | 5173 | React, Vite, Axios |
| Backend API | 8080 | FastAPI, PostgreSQL, Redis, JWT |
| Recommender | 8000 | FastAPI, scikit-learn, collaborative filtering |

---

## Features

**Backend**
- JWT authentication with access + refresh token rotation
- Product catalogue with category filtering, search, and pagination
- Shopping cart with Redis-backed session persistence
- Order management with status tracking
- Redis caching layer for product listings and user sessions

**Recommender Service**
- Collaborative filtering model trained on purchase history
- Content-based fallback for cold-start users
- Fetches live product data from the backend API
- Recommendations served per-user at checkout and on the homepage

**Frontend**
- Product browsing, search, and filtering
- Cart with real-time price calculation
- Checkout flow with order confirmation
- User account with order history

---

## Quick start (Docker)

```bash
git clone https://github.com/TarunSunil/e-commerce-python.git
cd e-commerce-python

cp .env.example .env   # fill in DATABASE_URL, JWT_SECRET, REDIS_URL

docker compose up --build
```

| Service | URL |
|---|---|
| Frontend | http://localhost:5173 |
| Backend API | http://localhost:8080 |
| API Docs (Swagger) | http://localhost:8080/docs |
| Recommender | http://localhost:8000 |

---

## Manual setup (without Docker)

### Prerequisites

- Python 3.11+
- Node.js 18+
- PostgreSQL 14+
- Redis 7+

### Database

```sql
CREATE DATABASE ecommerce;
CREATE USER ecom_user WITH PASSWORD 'ecom_pass';
GRANT ALL PRIVILEGES ON DATABASE ecommerce TO ecom_user;
```

### Backend API

```bash
cd backend
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env   # set DATABASE_URL, REDIS_URL, JWT_SECRET
uvicorn main:app --reload --port 8080
```

### Recommender Service

```bash
cd recommender
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

---

## Environment variables

```env
# Backend
DATABASE_URL=postgresql://ecom_user:ecom_pass@localhost:5432/ecommerce
REDIS_URL=redis://localhost:6379
JWT_SECRET=your_jwt_secret
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Recommender
BACKEND_API_URL=http://localhost:8080

# Frontend
VITE_API_BASE_URL=http://localhost:8080
```

---

## API reference

Full interactive docs at `/docs` (Swagger UI) and `/redoc` when the backend is running.

Key endpoints:

```
POST   /auth/register        Register new user
POST   /auth/login           Login → JWT tokens
GET    /products             List products (paginated)
GET    /products/{id}        Product detail
POST   /cart/add             Add item to cart
GET    /cart                 Get cart (Redis-backed)
POST   /orders               Place order
GET    /orders               Order history
GET    /recommendations/{user_id}   ML recommendations
```
