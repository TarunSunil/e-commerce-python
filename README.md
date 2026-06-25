# E-Commerce Platform

> Full-stack e-commerce application with AI-powered product recommendations, JWT authentication, Redis session caching, and a three-service Docker architecture.

[![FastAPI](https://img.shields.io/badge/FastAPI-backend-009688?style=flat-square&logo=fastapi&logoColor=white&labelColor=0f0f0f)](https://fastapi.tiangolo.com)
[![React](https://img.shields.io/badge/React-frontend-61DAFB?style=flat-square&logo=react&logoColor=black&labelColor=0f0f0f)](https://react.dev)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-database-4169E1?style=flat-square&logo=postgresql&logoColor=white&labelColor=0f0f0f)](https://postgresql.org)
[![Redis](https://img.shields.io/badge/Redis-cache-DC382D?style=flat-square&logo=redis&logoColor=white&labelColor=0f0f0f)](https://redis.io)
[![Docker](https://img.shields.io/badge/Docker-compose-2496ED?style=flat-square&logo=docker&logoColor=white&labelColor=0f0f0f)](https://docker.com)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat-square&logo=python&logoColor=white&labelColor=0f0f0f)](https://python.org)

---

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
