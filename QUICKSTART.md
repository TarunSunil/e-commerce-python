# 🚀 Quick Start Guide

**Complete beginner? Start here!** This is a simplified version of the full [README.md](README.md).

## 📝 What You Need

1. **Python 3.11+** - [Download](https://www.python.org/downloads/)
2. **Node.js 18+** - [Download](https://nodejs.org/)
3. **PostgreSQL 14+** - [Download](https://www.postgresql.org/download/)

## ⚡ Super Quick Setup (5 Steps)

### Step 1: Install Prerequisites
Install Python, Node.js, and PostgreSQL from the links above. ✅ Check "Add to PATH" during installation!

### Step 2: Set Up Database
Run this command in PowerShell:
```powershell
.\setup-database.ps1
```
Follow the prompts (just press Enter to use defaults). ✅

### Step 3: Install Dependencies
Run this command:
```powershell
.\setup.ps1
```
Choose option **1** (Full Setup). ✅

### Step 4: Create Configuration Files
Run this command:
```powershell
.\setup.ps1
```
Choose option **5** (Create .env files). ✅

### Step 5: Start Everything
Run this command:
```powershell
.\run-app.ps1 manual
```
✅ Three windows will open - keep them running!

### Step 6: Open the App
Open your browser and go to: **http://localhost:5173** 🎉

---

## 🎯 Daily Usage (After Setup)

Every time you want to run the app:

```powershell
.\run-app.ps1 manual
```

That's it! Three windows open automatically with all services.

---

## 🐳 Using Docker Instead (Easier but needs Docker)

1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop/)
2. Run: `.\run-app.ps1 docker`
3. Done! Everything runs in Docker.

---

## 🆘 Something Broke?

### Problem: "Command not found"
**Fix**: Reinstall the missing tool (Python/Node/PostgreSQL) and check "Add to PATH"

### Problem: "Port already in use"
**Fix**: Another program is using that port. Restart your computer or change ports in `.env` files.

### Problem: "Cannot connect to database"
**Fix**: 
1. Check PostgreSQL is running (search "Services" in Windows)
2. Re-run `.\setup-database.ps1`

### Problem: "Module not found" errors
**Fix**: Re-run `.\setup.ps1` and choose option 1

### Problem: Frontend shows errors
**Fix**: 
1. Make sure backend is running (check the window)
2. Go to http://localhost:8080/api/docs to verify

---

## 📚 Want More Details?

Read the full [README.md](README.md) for:
- Detailed explanations
- Manual setup instructions
- Architecture overview
- Security best practices
- Deployment guides

---

## 🎓 Learning Path

**Brand new to coding?** Follow this order:

1. ✅ Get it running (this guide)
2. 📖 Read [README.md](README.md) to understand how it works
3. 🔍 Explore [PROJECT_SUMMARY.txt](PROJECT_SUMMARY.txt) for architecture details
4. 🛠️ Read [FIXES_SUMMARY.md](FIXES_SUMMARY.md) to learn about code quality
5. 🎯 Start making small changes to learn!

---

## 🎁 Available Scripts

| Script | What It Does |
|--------|-------------|
| `.\setup.ps1` | Install dependencies for all services |
| `.\setup-database.ps1` | Create PostgreSQL database |
| `.\run-app.ps1 manual` | Start all services manually |
| `.\run-app.ps1 docker` | Start all services with Docker |

---

## ✨ What This App Does

- 🛍️ Browse products
- 🛒 Add items to cart
- 💳 Place orders
- 📦 View order history
- 🤖 AI product recommendations
- 👤 User accounts (register/login)
- 🔐 Secure authentication

---

**Need help? Check [README.md](README.md) for troubleshooting!**

*Last Updated: January 2026*
