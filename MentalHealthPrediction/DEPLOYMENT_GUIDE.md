# Deployment Guide for Mental Health Predictor

This guide will help you deploy your Flask application to a cloud platform.

## Option 1: Deploy to Render (Recommended - Free Tier Available)

### Step 1: Prepare Your Project

1. **Update Secret Key** - Use environment variables for security
2. **Create Procfile** - Tells Render how to run your app
3. **Update requirements.txt** - Ensure all dependencies are listed

### Step 2: Create GitHub Repository

1. Go to [GitHub](https://github.com) and create a new repository
2. Initialize git in your project folder:
   ```bash
   cd MentalHealthPrediction
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   git push -u origin main
   ```

### Step 3: Deploy on Render

1. Go to [Render.com](https://render.com) and sign up/login
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Configure:
   - **Name**: mental-health-predictor (or your choice)
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Plan**: Free (or paid)
5. Add Environment Variables:
   - `SECRET_KEY`: Generate a random secret key
6. Click "Create Web Service"
7. Wait for deployment (5-10 minutes)

### Step 4: Access Your App

Your app will be available at: `https://your-app-name.onrender.com`

---

## Option 2: Deploy to Railway (Alternative)

### Steps:

1. Go to [Railway.app](https://railway.app) and sign up
2. Click "New Project" → "Deploy from GitHub repo"
3. Connect your repository
4. Railway auto-detects Flask and deploys
5. Add environment variable: `SECRET_KEY`
6. Your app will be live automatically!

---

## Option 3: Deploy to PythonAnywhere (Beginner Friendly)

### Steps:

1. Go to [PythonAnywhere.com](https://www.pythonanywhere.com)
2. Create a free account
3. Go to "Files" tab and upload your project
4. Go to "Web" tab → "Add a new web app"
5. Choose Flask and Python version
6. Set working directory to your project folder
7. Update WSGI file to point to your app
8. Reload web app

---

## Option 4: Deploy to Heroku (Classic Option)

### Steps:

1. Install Heroku CLI from [heroku.com](https://devcenter.heroku.com/articles/heroku-cli)
2. Login: `heroku login`
3. Create app: `heroku create your-app-name`
4. Set config vars: `heroku config:set SECRET_KEY=your-secret-key`
5. Deploy: `git push heroku main`
6. Open: `heroku open`

---

## Important Files Needed for Deployment

### 1. Procfile (for Render/Heroku)
```
web: gunicorn app:app
```

### 2. runtime.txt (optional - specify Python version)
```
python-3.11.0
```

### 3. .gitignore (to exclude unnecessary files)
```
__pycache__/
*.pyc
*.db
instance/
venv/
.env
*.log
```

### 4. Update app.py to use environment variables
```python
import os
SECRET_KEY = os.environ.get('SECRET_KEY', 'fallback-key-for-development')
```

---

## Pre-Deployment Checklist

- [ ] Update SECRET_KEY to use environment variable
- [ ] Test all features locally
- [ ] Ensure all dependencies in requirements.txt
- [ ] Create Procfile
- [ ] Create .gitignore
- [ ] Push code to GitHub
- [ ] Set environment variables on hosting platform
- [ ] Test deployed application

---

## Common Issues & Solutions

### Issue 1: App crashes on startup
- **Solution**: Check logs, ensure all dependencies are in requirements.txt

### Issue 2: Database not working
- **Solution**: Ensure instance folder is created, database path is correct

### Issue 3: Static files not loading
- **Solution**: Check static folder path, ensure files are committed to git

### Issue 4: Model files not found
- **Solution**: Ensure model folder and all .pkl files are in repository

---

## Post-Deployment

1. Test all features
2. Monitor logs for errors
3. Set up custom domain (optional)
4. Enable HTTPS (usually automatic)
5. Set up monitoring/analytics (optional)

---

## Security Notes

- Never commit SECRET_KEY to git
- Use environment variables for sensitive data
- Enable HTTPS in production
- Regularly update dependencies
- Use strong passwords for admin accounts

---

## Need Help?

- Check platform-specific documentation
- Review application logs
- Test locally first before deploying
- Use platform's support/community forums
