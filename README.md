# E-Commerce Application

A full-stack e-commerce platform with React frontend, FastAPI backend, and AI-powered product recommendations.

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
   JWT_SECRET=your-super-secret-jwt-key-min-32-characters-long-please
   CORS_ORIGINS=["http://localhost:5173","http://localhost:3000"]
   RECOMMENDER_URL=http://localhost:8000
   ```

6. **Start the Backend API:**
   ```powershell
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

1. **Register a new account:**
   - Click "Register" in the navigation
   - Create your account

2. **Browse products:**
   - Go back to homepage
   - You should see product listings

3. **Add to cart:**
   - Click on a product
   - Add it to your cart

4. **Checkout:**
   - View your cart
   - Proceed to checkout

## 🎯 Quick Start (After Initial Setup)

Once you've completed the setup above, to run the application again:

1. **Start PostgreSQL** (should auto-start with Windows, or start manually)

2. **Start Backend** (in PowerShell):
   ```powershell
   cd D:\code\E-commerce\backend
   .\venv\Scripts\Activate.ps1
   uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload
   ```

3. **Start Recommender** (in new PowerShell):
   ```powershell
   cd D:\code\E-commerce\recommender
   .\venv\Scripts\Activate.ps1
   uvicorn app:app --host 0.0.0.0 --port 8000 --reload
   ```

4. **Start Frontend** (in new PowerShell):
   ```powershell
   cd D:\code\E-commerce\frontend
   npm run dev
   ```

## 🐳 Alternative: Docker Setup (Advanced)

If you prefer using Docker (easier but requires Docker Desktop):

1. **Install Docker Desktop** - [Download here](https://www.docker.com/products/docker-desktop/)

2. **Run with Docker Compose:**
   ```powershell
   docker-compose up --build
   ```

3. **Access:**
   - Frontend: http://localhost:5173
   - Backend: http://localhost:8080
   - Recommender: http://localhost:8000

## 📝 API Documentation

Once services are running:

- **Backend API Docs**: http://localhost:8080/api/docs
- **Recommender API Docs**: http://localhost:8000/docs

Both provide interactive documentation where you can test API endpoints!

## 🔑 Default Admin Account

After first startup, you can create an admin account through the API:

1. Go to: http://localhost:8080/api/docs
2. Find `/api/auth/register` endpoint
3. Click "Try it out"
4. Modify the JSON to include admin role:
   ```json
   {
     "email": "admin@example.com",
     "password": "admin123",
     "name": "Admin User"
   }
   ```

Then manually update the database to add admin role, or modify the registration code.

## 🛠️ Common Issues & Solutions

### Issue: "python: command not found"
**Solution**: Python not in PATH. Reinstall Python and check "Add to PATH" during installation.

### Issue: "Cannot activate virtual environment"
**Solution**: PowerShell execution policy issue. Run:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Issue: Backend shows "Connection refused" to database
**Solution**: 
- Check PostgreSQL is running: `services.msc` → find PostgreSQL
- Verify database credentials in `backend/.env`
- Ensure database `ecommerce` was created

### Issue: Port already in use
**Solution**: Another service is using that port. Either:
- Stop the other service
- Change the port in code and `.env` files

### Issue: Frontend shows network error
**Solution**: 
- Verify backend is running (http://localhost:8080/api/docs should load)
- Check `VITE_API_URL` in `frontend/.env`
- Check browser console for CORS errors

### Issue: No products showing
**Solution**: 
- Database might be empty
- Import seed data from `products.json` or create products via API
- Check browser console for errors

### Issue: Recommendations not working
**Solution**:
- Verify recommender service is running (http://localhost:8000/docs)
- Check `RECOMMENDER_URL` in `backend/.env`
- Ensure numpy and scikit-learn are installed in recommender

## 📂 Project Structure

```
E-commerce/
├── backend/              # FastAPI backend application
│   ├── app/
│   │   ├── models/      # Database models (User, Product, Cart, Order)
│   │   ├── routers/     # API endpoints (auth, products, cart, orders)
│   │   ├── services/    # Business logic
│   │   ├── schemas/     # Pydantic schemas for validation
│   │   ├── main.py      # FastAPI app entry point
│   │   ├── config.py    # Configuration settings
│   │   └── database.py  # Database connection
│   ├── alembic/         # Database migrations
│   ├── requirements.txt
│   └── .env             # Environment variables (create this!)
│
├── recommender/          # AI recommendation service
│   ├── app.py           # FastAPI app for recommendations
│   ├── recommender.py   # ML recommendation logic
│   ├── requirements.txt
│   └── .env             # Environment variables (create this!)
│
├── frontend/             # React frontend application
│   ├── src/
│   │   ├── components/  # Reusable UI components
│   │   ├── pages/       # Page components (Home, Cart, Checkout)
│   │   ├── services/    # API client services
│   │   ├── types/       # TypeScript type definitions
│   │   └── App.tsx      # Main app component
│   ├── package.json
│   └── .env             # Environment variables (create this!)
│
└── README.md            # This file!
```

## 🔐 Security Notes

⚠️ **Important for Production:**

1. Change `JWT_SECRET` in `backend/.env` to a strong, random value (32+ characters)
2. Use environment variables, never commit `.env` files to Git
3. Change database password from default `ecom_pass`
4. Enable HTTPS in production
5. Set `ENV=production` when deploying

## 🧪 Testing

Run tests (when implemented):

**Backend:**
```powershell
cd backend
pytest
```

**Frontend:**
```powershell
cd frontend
npm test
```

**Recommender:**
```powershell
cd recommender
pytest test_app.py
```

## 📊 Database Migrations (Advanced)

The app currently creates tables automatically. For production, use Alembic migrations:

1. **Generate initial migration:**
   ```powershell
   cd backend
   alembic revision --autogenerate -m "Initial migration"
   ```

2. **Apply migration:**
   ```powershell
   alembic upgrade head
   ```

## 🚢 Deployment

See deployment guides:
- [Render Deployment](RENDER_DEPLOYMENT.md) - Deploy backend to Render
- [Vercel Deployment](VERCEL_DEPLOYMENT.md) - Deploy frontend to Vercel

## 📖 Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [React Documentation](https://react.dev/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Vite Documentation](https://vitejs.dev/)

## 💡 Features

- ✅ User authentication (register, login, JWT tokens)
- ✅ Product browsing and search
- ✅ Shopping cart management
- ✅ Order placement and history
- ✅ AI-powered product recommendations
- ✅ Responsive UI with Tailwind CSS
- ✅ Admin product management (via API)

## 🤝 Need Help?

If you're stuck:

1. Check the "Common Issues & Solutions" section above
2. Verify all 3 services are running (backend, recommender, frontend)
3. Check the browser console for JavaScript errors (F12 → Console)
4. Check PowerShell windows for Python error messages
5. Ensure all `.env` files are created correctly

## 📝 License

This project is for educational purposes.

---

**Happy Coding! 🚀**

*Last Updated: January 2026*
