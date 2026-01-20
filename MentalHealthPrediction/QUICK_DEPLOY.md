# 🚀 Quick Deployment Guide

## Fastest Way: Render.com (5 minutes)

### 1️⃣ Push to GitHub
```bash
cd MentalHealthPrediction
git init
git add .
git commit -m "Deploy"
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

### 2️⃣ Deploy on Render
1. Go to https://render.com → Sign up
2. New + → Web Service
3. Connect GitHub repo
4. Settings:
   - Build: `pip install -r requirements.txt`
   - Start: `gunicorn app:app`
5. Add Environment Variable:
   - Key: `SECRET_KEY`
   - Value: Generate with: `python -c "import secrets; print(secrets.token_hex(32))"`
6. Create Web Service
7. Wait 5-10 minutes
8. Done! Your app is live 🎉

---

## Files Created for You ✅

- ✅ `Procfile` - Tells Render how to run your app
- ✅ `.gitignore` - Excludes unnecessary files
- ✅ `requirements.txt` - Updated with gunicorn
- ✅ `app.py` - Updated to use environment variables
- ✅ `DEPLOYMENT_GUIDE.md` - Detailed guide
- ✅ `DEPLOY_STEPS.md` - Step-by-step instructions

---

## Generate Secret Key

Run this command:
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

Copy the output and use it as your `SECRET_KEY` environment variable.

---

## Your App Will Be Live At:

`https://your-app-name.onrender.com`

---

## Need More Details?

See `DEPLOY_STEPS.md` for complete instructions!
