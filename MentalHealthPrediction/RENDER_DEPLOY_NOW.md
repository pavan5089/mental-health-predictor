# 🚀 Deploy to Render - Your Code is on GitHub!

## Step-by-Step: Deploy Your App on Render (Code Already on GitHub)

---

## ✅ YOU'RE HERE:
- ✅ Code is on GitHub
- ✅ Ready to deploy on Render

---

## STEP 1: Sign Up on Render (2 minutes)

1. **Go to**: https://render.com
2. **Click**: "Get Started for Free" button
3. **Sign up with GitHub** (recommended - easiest way!)
   - Click "Sign up with GitHub"
   - Authorize Render to access your GitHub account
   - This automatically connects your repositories

**OR** sign up with email if you prefer

---

## STEP 2: Create New Web Service (3 minutes)

### 2.1 Start Creating Service
1. After logging in, you'll see the Render dashboard
2. Click the **"New +"** button (top right corner)
3. Click **"Web Service"** from the dropdown

### 2.2 Connect Your Repository
1. You'll see "Connect a repository" section
2. If you signed up with GitHub, you'll see a list of your repositories
3. **Find and select**: `mental-health-predictor` (or whatever you named your repo)
4. If you don't see it, click "Configure account" to grant access
5. Click **"Connect"** button

---

## STEP 3: Configure Your Service (5 minutes)

Fill in these settings exactly:

### Basic Settings:
- **Name**: `mental-health-predictor` (or your choice - this becomes part of your URL)
- **Environment**: Select **"Python 3"** from dropdown
- **Region**: Choose closest to you (e.g., "Oregon (US West)" or "Frankfurt (EU Central)")
- **Branch**: Should auto-select `main` (if not, select it)

### Build & Deploy Settings:
- **Root Directory**: 
  - Leave **EMPTY** if your app files are in the root of the repo
  - OR type `MentalHealthPrediction` if your app is in a subfolder
  
- **Build Command**: 
  ```
  pip install -r requirements.txt
  ```
  (Copy and paste this exactly)

- **Start Command**: 
  ```
  gunicorn app:app
  ```
  (Copy and paste this exactly)

### Plan:
- Select **"Free"** (or paid if you want better performance)

---

## STEP 4: Add Environment Variable - SECRET_KEY (2 minutes)

### 4.1 Generate Secret Key

**Open Command Prompt** and run:
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

**Copy the output** (it will look like: `a1b2c3d4e5f6...` - long string of characters)

### 4.2 Add to Render

1. Scroll down to **"Environment Variables"** section
2. Click **"Add Environment Variable"** button
3. Fill in:
   - **Key**: `SECRET_KEY` (exactly like this)
   - **Value**: Paste the secret key you just generated
4. Click **"Add"** or press Enter

---

## STEP 5: Deploy! (Wait 5-10 minutes)

1. Scroll to the bottom of the page
2. Click **"Create Web Service"** button
3. **Wait for deployment** - you'll see a progress screen

### What Happens:
- ✅ Render installs dependencies
- ✅ Builds your application
- ✅ Starts your service
- ✅ Your app goes live!

### Watch the Logs:
- Click on **"Logs"** tab to see what's happening
- You'll see messages like:
  - "Installing dependencies..."
  - "Building application..."
  - "Starting service..."
  - "Your service is live at https://..."

---

## STEP 6: Access Your Live App! 🎉

1. Once deployment completes, you'll see:
   - **Status**: "Live" ✅
   - **URL**: `https://mental-health-predictor.onrender.com` (or your service name)

2. **Click the URL** or copy it
3. **Your app is now live on the internet!** 🚀

---

## STEP 7: Test Your Deployed App

Test these features to make sure everything works:

- [ ] Homepage loads correctly
- [ ] Sign up page works
- [ ] Login works
- [ ] Dashboard displays
- [ ] Assessment form loads
- [ ] Prediction works
- [ ] History page works
- [ ] All navigation links work

---

## 📋 QUICK REFERENCE

### Your App URL Format:
```
https://your-service-name.onrender.com
```

### Generate Secret Key:
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

### Update Your App Later:
```bash
git add .
git commit -m "Update"
git push origin main
```
(Render will automatically redeploy!)

---

## ❓ TROUBLESHOOTING

### Problem: Build Failed

**Solution:**
1. Click on **"Logs"** tab
2. Look for error messages (usually in red)
3. Common issues:
   - Missing package → Add to `requirements.txt`
   - Wrong command → Check Build/Start commands
   - Python version → Check `runtime.txt`

**Fix:**
- Update `requirements.txt` if needed
- Commit and push changes
- Render will auto-redeploy

---

### Problem: App Crashes on Startup

**Check:**
1. Go to **"Logs"** tab
2. Look for Python errors

**Common Causes:**
- Missing `SECRET_KEY` → Make sure it's set in Environment Variables
- File path issues → Check paths in `app.py`
- Missing model files → Ensure all files are in GitHub

**Fix:**
- Verify `SECRET_KEY` is set correctly
- Check that all files are committed to GitHub
- Review error messages in logs

---

### Problem: "Service Unavailable" or Slow Loading

**This is normal on Free tier:**
- Free tier spins down after 15 minutes of inactivity
- First request after spin-down takes ~30 seconds
- This is expected behavior

**Solution:**
- Wait 30 seconds for first load
- Or upgrade to paid plan for always-on service

---

### Problem: Static Files (CSS) Not Loading

**Fix:**
1. Verify `static/` folder is in your GitHub repo
2. Check file paths in templates
3. Clear browser cache (Ctrl+F5)

---

## 🔄 UPDATING YOUR APP

After making changes to your code:

1. **Make changes locally**
2. **Test locally**: `python app.py`
3. **Commit and push**:
   ```bash
   git add .
   git commit -m "Description of changes"
   git push origin main
   ```
4. **Render automatically redeploys** (or manually trigger in dashboard)

---

## 📊 MONITORING YOUR APP

### View Logs:
- Dashboard → Your Service → **"Logs"** tab
- Real-time application logs
- Useful for debugging

### View Metrics:
- Dashboard → Your Service → **"Metrics"** tab
- See:
  - Response times
  - Request count
  - Error rate
  - Resource usage

### Restart Service:
- Dashboard → Your Service → **"Manual Deploy"**
- Useful if app gets stuck

---

## ✅ DEPLOYMENT CHECKLIST

Before deploying:
- [x] Code is on GitHub ✅
- [ ] Render account created
- [ ] Web service created
- [ ] Settings configured correctly
- [ ] SECRET_KEY environment variable added
- [ ] Service deployed successfully
- [ ] App is accessible via URL
- [ ] All features tested

---

## 🎉 SUCCESS!

Your Mental Health Predictor app is now live on Render!

**Your app URL:**
```
https://mental-health-predictor.onrender.com
```

(Replace with your actual service name)

---

## 📚 NEED MORE HELP?

- **Render Docs**: https://render.com/docs
- **Render Support**: https://render.com/docs/support
- **Check Logs**: Always check logs first for errors

---

## 🚀 NEXT STEPS

1. ✅ Share your app URL with others
2. ✅ Test all features
3. ✅ Monitor performance
4. ✅ Make updates as needed
5. ✅ Consider custom domain (optional)

---

**Congratulations! Your app is now live on the internet! 🎊**
