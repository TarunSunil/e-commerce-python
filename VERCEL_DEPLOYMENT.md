# Vercel Deployment Guide for E-commerce Frontend

## Quick Start - Deploy Frontend to Vercel

### Prerequisites
- GitHub account (you have: https://github.com/TarunSunil/e-commerce-python)
- Vercel account (free at https://vercel.com)

### Step 1: Push Latest Code to GitHub
```bash
git add .
git commit -m "Prepare for Vercel deployment"
git push origin main
```

### Step 2: Connect to Vercel

1. Go to https://vercel.com/dashboard
2. Click **"Add New..."** → **"Project"**
3. Select your GitHub repository: `e-commerce-python`
4. Click **"Import"**

### Step 3: Configure Project Settings

**Root Directory:** Leave blank (Vercel will auto-detect)

**Build Command:** Already configured in `vercel.json`
```
cd frontend && npm run build
```

**Output Directory:** Already configured in `vercel.json`
```
frontend/dist
```

### Step 4: Add Environment Variables

In Vercel Dashboard:
1. Go to **Settings** → **Environment Variables**
2. Add variable:
   - **Name:** `VITE_API_URL`
   - **Value:** Your backend API URL (e.g., `https://your-backend.onrender.com/api`)
   - **Select:** Production, Preview, Development

3. Click **"Save"**

### Step 5: Deploy

Click **"Deploy"** button in Vercel dashboard.

**Your frontend will be live at:** `https://<your-project>.vercel.app`

---

## After Frontend Deployment

### Option 1: Keep Backend Locally
- Frontend talks to your local backend running on `http://localhost:8080`
- Backend URL: `http://localhost:8080/api`
- Add to Vercel env: `VITE_API_URL=http://localhost:8080/api`
- ⚠️ Note: CORS might block this - frontend and backend need to be same origin or CORS enabled

### Option 2: Deploy Backend to Render (Recommended)
See `RENDER_DEPLOYMENT.md` for full stack deployment guide.

---

## Troubleshooting

**Build fails with "dependencies not found":**
- Check `frontend/package.json` is correct
- Check `frontend/node_modules` exists locally
- Vercel should auto-install, but you can trigger rebuild

**API calls fail (CORS error):**
- Backend CORS is not allowing requests from Vercel domain
- Update backend's `CORS_ORIGINS` env variable to include Vercel URL
- Or enable all origins in development: `CORS_ORIGINS=*`

**Cannot find module errors:**
- Make sure you pushed all files to GitHub
- Check that paths in imports are correct

---

## Next Steps

After frontend is deployed:
1. Note your Vercel URL
2. Update backend CORS settings to allow requests from your Vercel domain
3. Set `VITE_API_URL` in Vercel env to your backend URL
4. Redeploy frontend

**For full-stack on Render, see:** `RENDER_DEPLOYMENT.md`
