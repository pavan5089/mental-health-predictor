# 🚀 Deploy to Render - Complete Guide

## Step-by-Step Instructions to Deploy Your App on Render

---

## PREREQUISITES

✅ Your code must be on GitHub first!
- If not done yet, follow `SIMPLE_GUIDE.md` to push to GitHub

---

## STEP 1: Push Code to GitHub (If Not Done)

### Quick Commands:
```bash
cd C:\Users\pavan\OneDrive\Desktop\finalproject\MentalHealthPrediction

git init
git add .
git commit -m "Ready for Render deployment"

# Add your GitHub repository (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/mental-health-predictor.git
git branch -M main
git push -u origin main
```

---

## STEP 2: Sign Up for Render

1. Go to **https://render.com**
2. Click **"Get Started for Free"**
3. Sign up with **GitHub** (recommended - easier!)
   - Click "Sign up with GitHub"
   - Authorize Render to access your GitHub
4. Or sign up with email if you prefer

---

## STEP 3: Create Web Service on Render

### 3.1 Start New Service
1. After logging in, click **"New +"** button (top right)
2. Click **"Web Service"**

### 3.2 Connect Repository
1. You'll see "Connect a repository"
2. If you signed up with GitHub, you'll see your repositories
3. **Select**: `mental-health-predictor` (or your repo name)
4. Click **"Connect"**

### 3.3 Configure Settings

Fill in these settings:

**Basic Settings:**
- **Name**: `mental-health-predictor` (or your choice)
- **Environment**: Select **"Python 3"**
- **Region**: Choose closest to you (e.g., "Oregon (US West)")
- **Branch**: `main` (should be auto-selected)

**Build & Deploy:**
- **Root Directory**: Leave **empty** (or type `MentalHealthPrediction` if your app is in a subfolder)
- **Build Command**: 
  ```
  pip install -r requirements.txt
  ```
- **Start Command**: 
  ```
  gunicorn app:app
  ```

**Plan:**
- Select **"Free"** (or paid for better performance)

### 3.4 Add Environment Variables

1. Scroll down to **"Environment Variables"** section
2. Click **"Add Environment Variable"**
3. Add this variable:
   - **Key**: `SECRET_KEY`
   - **Value**: Generate a secret key (see below)

#### Generate Secret Key:

**Option 1: Using Python**
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

**Option 2: Using Online Tool**
- Go to: https://randomkeygen.com
- Copy a "CodeIgniter Encryption Keys" (64 characters)

**Paste the generated key** as the value for `SECRET_KEY`

### 3.5 Create Web Service

1. Scroll down
2. Click **"Create Web Service"** button
3. Wait 5-10 minutes for deployment

---

## STEP 4: Monitor Deployment

1. You'll see a **"Logs"** tab
2. Watch the build process:
   - ✅ Installing dependencies
   - ✅ Building application
   - ✅ Starting service
3. When you see **"Your service is live"** → Success! 🎉

---

## STEP 5: Access Your App

1. Once deployed, you'll see your app URL:
   - Example: `https://mental-health-predictor.onrender.com`
2. Click the URL or copy it
3. Your app is now live! 🚀

---

## STEP 6: Test Your Deployed App

Test these features:
- [ ] Homepage loads
- [ ] Sign up works
- [ ] Login works
- [ ] Dashboard displays
- [ ] Assessment form works
- [ ] Prediction works
- [ ] History page works

---

## TROUBLESHOOTING

### Issue 1: Build Failed

**Check:**
- Go to "Logs" tab
- Look for error messages
- Common issues:
  - Missing dependency → Add to `requirements.txt`
  - Wrong Python version → Check `runtime.txt`
  - Build command error → Verify command is correct

**Fix:**
- Update `requirements.txt`
- Commit and push changes
- Render will auto-redeploy

---

### Issue 2: App Crashes on Startup

**Check Logs:**
- Click "Logs" tab
- Look for Python errors

**Common Causes:**
- Missing `SECRET_KEY` environment variable
- Database path issues
- Model files not found

**Fix:**
- Verify `SECRET_KEY` is set
- Check file paths in `app.py`
- Ensure all files are in GitHub

---

### Issue 3: Static Files Not Loading

**Fix:**
- Verify `static/` folder is in repository
- Check CSS/JS file paths in templates
- Clear browser cache

---

### Issue 4: Database Errors

**Fix:**
- Render creates `instance/` folder automatically
- Database will be created on first run
- If issues persist, check file permissions

---

### Issue 5: Model Files Not Found

**Fix:**
- Ensure `model/` folder is committed to GitHub
- Check that all `.pkl` files are uploaded
- Verify paths in `app.py` are correct

---

## UPDATING YOUR APP

After making changes:

1. **Make changes locally**
2. **Test locally**: `python app.py`
3. **Commit changes**:
   ```bash
   git add .
   git commit -m "Updated feature"
   git push origin main
   ```
4. **Render auto-deploys** (or manually trigger in dashboard)

---

## RENDER DASHBOARD FEATURES

### Useful Tabs:
- **Logs**: View application logs
- **Metrics**: Monitor performance
- **Events**: See deployment history
- **Settings**: Update configuration
- **Environment**: Manage environment variables

---

## FREE TIER LIMITATIONS

Render Free tier:
- ✅ Free forever
- ⚠️ Spins down after 15 minutes of inactivity
- ⚠️ First request after spin-down takes ~30 seconds
- ⚠️ 750 hours/month free

**Upgrade to paid** for:
- Always-on service
- Faster response times
- More resources

---

## CUSTOM DOMAIN (Optional)

1. Go to your service → **Settings**
2. Scroll to **"Custom Domains"**
3. Add your domain
4. Update DNS records as instructed
5. Wait for SSL certificate (automatic)

---

## MONITORING

### Check Health:
- Dashboard → Your Service → **Metrics**
- View:
  - Response times
  - Request count
  - Error rate
  - CPU/Memory usage

### View Logs:
- Click **"Logs"** tab
- Real-time application logs
- Useful for debugging

---

## SECURITY CHECKLIST

✅ **Done:**
- Secret key uses environment variable
- .gitignore excludes sensitive files
- HTTPS enabled automatically

⚠️ **Remember:**
- Never commit `.env` files
- Use strong passwords
- Keep dependencies updated
- Monitor logs regularly

---

## QUICK REFERENCE

### Your App URL:
```
https://your-app-name.onrender.com
```

### Update App:
```bash
git add .
git commit -m "Update"
git push origin main
```

### View Logs:
- Render Dashboard → Your Service → Logs

### Restart Service:
- Render Dashboard → Your Service → Manual Deploy → Clear build cache & deploy

---

## COMPLETE CHECKLIST

Before deploying:
- [ ] Code is on GitHub
- [ ] All files committed
- [ ] requirements.txt updated
- [ ] Procfile created
- [ ] .gitignore working
- [ ] Secret key ready

After deploying:
- [ ] App is accessible
- [ ] All features work
- [ ] No errors in logs
- [ ] Environment variables set
- [ ] Test all pages

---

## SUPPORT

- **Render Docs**: https://render.com/docs
- **Render Support**: https://render.com/docs/support
- **Community**: https://community.render.com

---

## SUCCESS! 🎉

Your Mental Health Predictor app is now live on Render!

**Next Steps:**
- Share your app URL with others
- Monitor performance
- Make updates as needed
- Consider upgrading for production use

---

**Your app URL will be:**
`https://mental-health-predictor.onrender.com`

(Replace `mental-health-predictor` with your actual service name)
