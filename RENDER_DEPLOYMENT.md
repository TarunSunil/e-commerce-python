# Render Deployment Guide - Backend & Database

## Backend Deployment to Render

### Step 1: Create Render Account
1. Go to https://render.com
2. Sign up with GitHub account (recommended)

### Step 2: Create PostgreSQL Database
1. In Render Dashboard, click **"New +"** → **"PostgreSQL"**
2. Configure:
   - **Name:** `ecommerce-postgres`
   - **Database:** `ecommerce`
   - **User:** `ecom_user`
   - **Region:** Choose closest to you (e.g., `us-east`)
3. Click **"Create Database"**
4. Wait ~2-3 minutes for database to initialize
5. Copy the **Internal Database URL** (you'll need this)

### Step 3: Deploy Backend Service
1. In Render Dashboard, click **"New +"** → **"Web Service"**
2. Select your GitHub repo: `e-commerce-python`
3. Configure:
   - **Name:** `ecommerce-backend`
   - **Root Directory:** `backend`
   - **Runtime:** Python
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn app.main:app --host 0.0.0.0 --port 8080`
   - **Region:** Same as database
   - **Plan:** Free (or upgrade if needed)

### Step 4: Add Environment Variables

In the **Environment** section, add these variables:

```
DATABASE_URL=postgresql://ecom_user:PASSWORD@HOST:5432/ecommerce
JWT_SECRET=your-secret-key-change-in-production-min-256-bits
CORS_ORIGINS=https://e-commerce-python.vercel.app,http://localhost:3000
RECOMMENDER_URL=http://recommender:8000
```

**Where to find DATABASE_URL:**
- From the PostgreSQL database you created in Step 2
- Format: `postgresql://USER:PASSWORD@HOST:PORT/DATABASE`

### Step 5: Deploy

1. Click **"Create Web Service"**
2. Render will automatically build and deploy
3. Wait ~5-10 minutes for deployment to complete
4. Once live, you'll get a URL like: `https://ecommerce-backend.onrender.com`

---

## Step 6: Update Frontend to Use Backend

Once backend is deployed, update your Vercel environment:

1. Go to Vercel Dashboard → Your Project → **Settings** → **Environment Variables**
2. Update `VITE_API_URL`:
   - **Old:** `http://localhost:8080/api`
   - **New:** `https://ecommerce-backend.onrender.com/api` (replace with your actual URL)
3. Click **"Save"**
4. Vercel will auto-redeploy with the new backend URL

---

## Step 7: Deploy Recommender (Optional)

If you want to deploy the recommender service:

1. Create another **Web Service** on Render
2. **Root Directory:** `recommender`
3. **Start Command:** `uvicorn app:app --host 0.0.0.0 --port 8000`
4. **Environment Variables:**
   ```
   BACKEND_URL=https://ecommerce-backend.onrender.com/api
   ```
5. Deploy and get URL like: `https://ecommerce-recommender.onrender.com`

---

## Testing Your Deployment

Once everything is deployed:

1. Go to: `https://e-commerce-python.vercel.app`
2. You should see your frontend
3. Try logging in or browsing products (API calls will go to your Render backend)
4. Check API docs: `https://ecommerce-backend.onrender.com/api/docs`

---

## Troubleshooting

**Backend deployment fails:**
- Check `backend/requirements.txt` exists
- Check `backend/app/main.py` exists
- View logs in Render dashboard

**Frontend can't connect to backend (CORS error):**
- Backend's `CORS_ORIGINS` must include your Vercel URL
- Make sure `VITE_API_URL` is set correctly in Vercel

**Database connection fails:**
- Double-check `DATABASE_URL` environment variable
- Ensure PostgreSQL service is running
- Check credentials are correct

---

## Summary

| Service | Platform | URL |
|---------|----------|-----|
| Frontend | Vercel | `https://e-commerce-python.vercel.app` |
| Backend API | Render | `https://ecommerce-backend.onrender.com` |
| Database | Render | PostgreSQL (internal) |
| Recommender | Render | `https://ecommerce-recommender.onrender.com` (optional) |

All services will be fully functional and accessible online!
