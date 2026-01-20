# Step-by-Step Deployment Instructions

## Quick Start: Deploy to Render (Easiest Method)

### Prerequisites
- GitHub account (free)
- Render account (free tier available)
- Your project code ready

---

## STEP 1: Prepare Your Code

### 1.1 Update Secret Key
✅ Already done! The app now uses environment variables.

### 1.2 Test Locally First
```bash
# Make sure everything works locally
cd MentalHealthPrediction
python app.py
# Visit http://127.0.0.1:5000 and test all features
```

### 1.3 Generate a Strong Secret Key
```python
# Run this in Python to generate a secret key:
import secrets
print(secrets.token_hex(32))
```
**Save this key** - you'll need it later!

---

## STEP 2: Push to GitHub

### 2.1 Initialize Git (if not already done)
```bash
cd MentalHealthPrediction
git init
```

### 2.2 Create .gitignore
✅ Already created! It excludes unnecessary files.

### 2.3 Add and Commit Files
```bash
git add .
git commit -m "Ready for deployment"
```

### 2.4 Create GitHub Repository
1. Go to https://github.com
2. Click "New repository"
3. Name it: `mental-health-predictor` (or your choice)
4. **Don't** initialize with README
5. Click "Create repository"

### 2.5 Push to GitHub
```bash
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git branch -M main
git push -u origin main
```
Replace `YOUR_USERNAME` and `YOUR_REPO_NAME` with your actual GitHub username and repository name.

---

## STEP 3: Deploy on Render

### 3.1 Sign Up/Login
1. Go to https://render.com
2. Sign up with GitHub (recommended) or email
3. Verify your email if needed

### 3.2 Create New Web Service
1. Click **"New +"** button (top right)
2. Select **"Web Service"**
3. Click **"Connect account"** if prompted
4. Select your GitHub repository: `mental-health-predictor`

### 3.3 Configure Settings
Fill in the form:

- **Name**: `mental-health-predictor` (or your choice)
- **Environment**: `Python 3`
- **Region**: Choose closest to you
- **Branch**: `main`
- **Root Directory**: Leave empty (or `MentalHealthPrediction` if your app is in a subfolder)
- **Build Command**: 
  ```
  pip install -r requirements.txt
  ```
- **Start Command**: 
  ```
  gunicorn app:app
  ```
- **Plan**: Select **Free** (or paid for better performance)

### 3.4 Add Environment Variables
Click **"Advanced"** → **"Add Environment Variable"**:

- **Key**: `SECRET_KEY`
- **Value**: Paste the secret key you generated in Step 1.3

Click **"Add"**

### 3.5 Deploy
1. Click **"Create Web Service"** at the bottom
2. Wait 5-10 minutes for deployment
3. Watch the build logs - it will show progress

### 3.6 Access Your App
Once deployed, you'll see:
- **Status**: Live ✅
- **URL**: `https://mental-health-predictor.onrender.com` (or your custom name)

Click the URL to open your app!

---

## STEP 4: Verify Deployment

### Test These Features:
- [ ] Homepage loads
- [ ] Sign up works
- [ ] Login works
- [ ] Dashboard displays
- [ ] Assessment form works
- [ ] Prediction works
- [ ] History page works
- [ ] All navigation links work

---

## STEP 5: Troubleshooting

### If deployment fails:

1. **Check Build Logs**
   - Click on your service in Render dashboard
   - Go to "Logs" tab
   - Look for error messages

2. **Common Issues:**

   **Issue**: "Module not found"
   - **Fix**: Add missing package to `requirements.txt`

   **Issue**: "No module named gunicorn"
   - **Fix**: Already added to requirements.txt ✅

   **Issue**: "Database error"
   - **Fix**: Ensure `instance/` folder exists (it will be created automatically)

   **Issue**: "Model files not found"
   - **Fix**: Ensure `model/` folder and all `.pkl` files are committed to git

3. **Redeploy**
   - Make fixes
   - Commit and push to GitHub
   - Render will auto-deploy (or click "Manual Deploy")

---

## Alternative: Deploy to Railway (Even Easier!)

### Steps:
1. Go to https://railway.app
2. Sign up with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select your repository
5. Railway auto-detects Flask!
6. Add environment variable: `SECRET_KEY`
7. Done! Your app is live.

Railway automatically:
- Detects Python/Flask
- Installs dependencies
- Runs your app
- Provides HTTPS URL

---

## Alternative: Deploy to PythonAnywhere

### Steps:
1. Sign up at https://www.pythonanywhere.com
2. Go to "Files" tab
3. Upload your project folder
4. Go to "Web" tab → "Add a new web app"
5. Choose Flask, Python 3.10
6. Set working directory: `/home/YOUR_USERNAME/mental-health-predictor`
7. Update WSGI file:
   ```python
   import sys
   path = '/home/YOUR_USERNAME/mental-health-predictor'
   if path not in sys.path:
       sys.path.append(path)
   
   from app import app as application
   ```
8. Set environment variable in "Web" → "Environment variables"
9. Reload web app

---

## Post-Deployment Checklist

- [ ] App is accessible via URL
- [ ] All features work
- [ ] Database creates successfully
- [ ] Static files load (CSS, images)
- [ ] Forms submit correctly
- [ ] User authentication works
- [ ] Predictions work
- [ ] No errors in logs

---

## Updating Your Deployed App

### To update after making changes:

1. **Make changes locally**
2. **Test locally**
3. **Commit changes:**
   ```bash
   git add .
   git commit -m "Description of changes"
   git push origin main
   ```
4. **Render/Railway auto-deploys** (or manually trigger)

---

## Custom Domain (Optional)

### Render:
1. Go to your service → Settings
2. Scroll to "Custom Domains"
3. Add your domain
4. Update DNS records as instructed

### Railway:
1. Go to project → Settings → Domains
2. Add custom domain
3. Follow DNS setup instructions

---

## Monitoring & Maintenance

### Check Logs Regularly:
- Render: Dashboard → Your Service → Logs
- Railway: Project → Deployments → View Logs

### Monitor:
- Uptime
- Response times
- Error rates
- Resource usage

---

## Security Reminders

✅ **Done:**
- Secret key uses environment variable
- .gitignore excludes sensitive files

⚠️ **Remember:**
- Never commit `.env` files
- Use strong passwords
- Keep dependencies updated
- Monitor for security updates

---

## Need Help?

- **Render Docs**: https://render.com/docs
- **Railway Docs**: https://docs.railway.app
- **Flask Docs**: https://flask.palletsprojects.com
- **GitHub Issues**: Check your repository issues

---

## Quick Reference Commands

```bash
# Generate secret key
python -c "import secrets; print(secrets.token_hex(32))"

# Test locally
python app.py

# Git commands
git add .
git commit -m "Your message"
git push origin main

# Check requirements
pip freeze > requirements.txt
```

---

**Congratulations! Your app is now live! 🎉**
