from flask import Flask, render_template, request, redirect, url_for, flash
import numpy as np
import pickle
import json
import pandas as pd
import os
import time
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from models import db, User

app = Flask(__name__)
# Use environment variable for SECRET_KEY in production, fallback for development
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key-change-in-production')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(BASE_DIR, "instance", "users.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Paths for model artifacts (relative to this file's directory)
MODEL_PATH = os.path.join(BASE_DIR, 'model', 'rf_model.pkl')
ENCODER_PATH = os.path.join(BASE_DIR, 'model', 'label_encoder.pkl')
FEATURES_PATH = os.path.join(BASE_DIR, 'model', 'feature_columns.json')
ORIG_PATH = os.path.join(BASE_DIR, 'model', 'original_features.json')

# Globals to hold loaded artifacts and mtimes
model = None
encoder = None
FEATURE_COLS = []
ORIGINAL_FEATURES = []
_mtimes = {}

def load_model_files(force=False):
    global model, encoder, FEATURE_COLS, ORIGINAL_FEATURES, _mtimes
    paths = [MODEL_PATH, ENCODER_PATH, FEATURES_PATH, ORIG_PATH]
    changed = force
    for p in paths:
        try:
            m = os.path.getmtime(p)
        except Exception:
            m = None
        if p not in _mtimes or (_mtimes[p] is None and m is not None) or (m is not None and m != _mtimes.get(p)):
            changed = True
        _mtimes[p] = m
    if not changed and model is not None:
        return
    # reload
    try:
        if os.path.exists(MODEL_PATH):
            with open(MODEL_PATH, 'rb') as f:
                model = pickle.load(f)
            print(f'Model loaded from {MODEL_PATH}')
        else:
            print(f'Warning: Model file not found at {MODEL_PATH}')
            model = None
            
        if os.path.exists(ENCODER_PATH):
            with open(ENCODER_PATH, 'rb') as f:
                encoder = pickle.load(f)
            print(f'Encoder loaded from {ENCODER_PATH}')
        else:
            print(f'Warning: Encoder file not found at {ENCODER_PATH}')
            encoder = None
            
        if os.path.exists(FEATURES_PATH):
            with open(FEATURES_PATH, 'r', encoding='utf-8') as f:
                FEATURE_COLS = json.load(f)
            print(f'Feature columns loaded from {FEATURES_PATH}')
        else:
            print(f'Warning: Feature columns file not found at {FEATURES_PATH}')
            FEATURE_COLS = []
            
        if os.path.exists(ORIG_PATH):
            with open(ORIG_PATH, 'r', encoding='utf-8') as f:
                ORIGINAL_FEATURES = json.load(f)
            print(f'Original features loaded from {ORIG_PATH}')
        else:
            print(f'Warning: Original features file not found at {ORIG_PATH}')
            ORIGINAL_FEATURES = []
            
        if model and encoder and FEATURE_COLS and ORIGINAL_FEATURES:
            print('All model artifacts loaded successfully')
        else:
            print('Warning: Some model artifacts are missing')
    except Exception as e:
        print(f'Error loading model artifacts: {e}')
        import traceback
        traceback.print_exc()

with app.app_context():
    db.create_all()

# Initial load
load_model_files(force=True)

# Try to import shap; if unavailable we'll fall back to importance proxy
try:
    import shap
    SHAP_AVAILABLE = True
except Exception:
    SHAP_AVAILABLE = False


@app.route("/")
def home():
    if current_user.is_authenticated:
        return render_template("index.html")
    else:
        return redirect(url_for('signup'))


@app.route("/history")
@login_required
def history():
    rows = []
    try:
        with open(os.path.join(BASE_DIR, 'data', 'history.csv'), 'r', encoding='utf-8') as f:
            next(f)  # skip header
            for line in f:
                parts = line.strip().split(',', 4)
                if len(parts) == 5 and parts[0] == str(current_user.id):
                    ts = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(parts[1]))) if parts[1].isdigit() else parts[1]
                    prob = float(parts[2]) if parts[2] != '' else None
                    rows.append((ts, prob, parts[3], parts[4]))
    except Exception as e:
        print('History read error:', e)
    rows = list(reversed(rows))[:50]
    return render_template('history.html', rows=rows)


@app.route("/predict", methods=["POST"])
@login_required
def predict():
    # Reload model files if they were updated on disk (auto-reload after retrain)
    load_model_files()

    # Build an input row using ORIGINAL_FEATURES (pre-one-hot) and then one-hot encode
    orig_row = {c: 0 for c in ORIGINAL_FEATURES}

    # Sensible defaults for removed inputs
    defaults = {
        "id": 1,
        "City": "Unknown",
        "Profession": "Other",
        "Job Satisfaction": 3,
        "Dietary Habits": "Moderate",
        "Have you ever had suicidal thoughts ?": "No"
    }
    for k, v in defaults.items():
        if k in orig_row:
            orig_row[k] = v

    for key, val in request.form.items():
        if key in orig_row:
            # try to parse numeric values, otherwise keep as string for categorical
            try:
                orig_row[key] = float(val)
            except Exception:
                orig_row[key] = val

    df_orig = pd.DataFrame([orig_row])
    
    # Separate numeric and categorical columns
    numeric_cols = []
    categorical_cols = []
    
    for col in df_orig.columns:
        if pd.api.types.is_numeric_dtype(df_orig[col]):
            numeric_cols.append(col)
        else:
            categorical_cols.append(col)
    
    # Process categorical columns with get_dummies
    df_dummied_list = []
    
    if numeric_cols:
        df_dummied_list.append(df_orig[numeric_cols])
    
    if categorical_cols:
        try:
            df_categorical = pd.get_dummies(df_orig[categorical_cols], drop_first=True)
            if not df_categorical.empty:
                df_dummied_list.append(df_categorical)
        except Exception as e:
            print(f'Error in get_dummies: {e}')
            # If get_dummies fails, try without drop_first
            try:
                df_categorical = pd.get_dummies(df_orig[categorical_cols], drop_first=False)
                if not df_categorical.empty:
                    df_dummied_list.append(df_categorical)
            except Exception as e2:
                print(f'Error in get_dummies (without drop_first): {e2}')
    
    # Combine all DataFrames
    if df_dummied_list:
        df_dummied = pd.concat(df_dummied_list, axis=1)
    else:
        # Fallback: create empty DataFrame with feature columns
        df_dummied = pd.DataFrame(columns=FEATURE_COLS)
    
    # Reindex to the exact columns used during training
    X_input = df_dummied.reindex(columns=FEATURE_COLS, fill_value=0)

    # Validate that model and encoder are loaded
    if model is None:
        flash('Error: Model not loaded. Please ensure model files exist in the model directory.')
        return redirect(url_for('home'))
    
    if encoder is None:
        flash('Error: Label encoder not loaded. Please ensure encoder file exists in the model directory.')
        return redirect(url_for('home'))
    
    if not FEATURE_COLS:
        flash('Error: Feature columns not loaded. Please ensure feature_columns.json exists in the model directory.')
        return redirect(url_for('home'))

    # Predict (get probabilities and predicted class)
    try:
        probs = model.predict_proba(X_input)[0]
    except Exception as e:
        print(f'Error in predict_proba: {e}')
        probs = None

    try:
        pred = model.predict(X_input)
        result = encoder.inverse_transform(pred)[0]
    except Exception as e:
        flash(f'Error making prediction: {str(e)}')
        return redirect(url_for('home'))

    # determine positive-class index (class representing 'at risk' = 1)
    try:
        pos_index = list(encoder.classes_).index(1)
    except Exception:
        pos_index = 1 if len(encoder.classes_) > 1 else 0
    prob_pos = float(probs[pos_index]) if probs is not None else None

    # Log the input vector and probability for debugging
    print("Constructed input (nonzero):", [c for c, v in X_input.iloc[0].items() if v != 0][:60])
    print("Predicted probs:", probs)

    # Map model result to human-friendly risk levels
    def map_to_risk(res):
        # try numeric mapping first
        try:
            r = int(res)
            mapping = {0: "Low Risk", 1: "Moderate Risk", 2: "High Risk"}
            return mapping.get(r, f"Risk Level {r}")
        except Exception:
            s = str(res).lower()
            if "low" in s:
                return "Low Risk"
            if "moder" in s:
                return "Moderate Risk"
            if "high" in s or "severe" in s:
                return "High Risk"
            return "Unknown Risk"

    # Map risk by probability if available (better UX)
    if prob_pos is not None:
        if prob_pos < 0.33:
            risk_label = "Low Risk"
        elif prob_pos < 0.66:
            risk_label = "Moderate Risk"
        else:
            risk_label = "High Risk"
    else:
        risk_label = map_to_risk(result)

    awareness_msgs = {
        "Low Risk": "You appear to be at low risk. Keep maintaining healthy routines, sleep, and social support. If anything changes, check in with a trusted person.",
        "Moderate Risk": "You may be experiencing noticeable symptoms. Consider talking to a friend, family member, or a counselor. If available, contact your school's mental health services.",
        "High Risk": "You may be at high risk. If you are in immediate danger call emergency services. Reach out to a mental health professional or crisis line right away."
    }

    awareness = awareness_msgs.get(risk_label, "If you're unsure what this means, consider consulting a health professional.")

    # Compute local explanations (top contributors)
    top_contribs = []
    try:
        if SHAP_AVAILABLE:
            explainer = shap.TreeExplainer(model)
            sv = explainer.shap_values(X_input)
            # shap returns a list for multiclass; for binary take index for positive class
            if isinstance(sv, list) and len(sv) > 1:
                local_shap = sv[1][0]
            else:
                local_shap = sv[0][0]
            abs_idx = list(np.argsort(-np.abs(local_shap)))
            for i in abs_idx[:6]:
                top_contribs.append((FEATURE_COLS[i], float(local_shap[i])))
        else:
            # fallback: use model.feature_importances_ * feature value as proxy
            fi = getattr(model, 'feature_importances_', None)
            if fi is not None:
                proxy = (X_input.values[0] * fi)
                idx = list(np.argsort(-np.abs(proxy)))
                for i in idx[:6]:
                    if X_input.values[0][i] != 0:
                        top_contribs.append((FEATURE_COLS[i], float(proxy[i])))
    except Exception as e:
        print('Explainability error:', e)

    # Append anonymized entry to history log
    try:
        os.makedirs(os.path.join(BASE_DIR, 'data'), exist_ok=True)
        summary = ','.join([f"{k}={v}" for k, v in list(orig_row.items()) if k in ['Academic Pressure','Work Pressure','Study Satisfaction','Financial Stress']])
        with open(os.path.join(BASE_DIR, 'data', 'history.csv'), 'a', encoding='utf-8') as hf:
            hf.write(f"{current_user.id},{int(time.time())},{prob_pos if prob_pos is not None else ''},{risk_label},{summary}\n")
    except Exception as e:
        print('History log error:', e)

    return render_template("result.html", prediction=result, risk_label=risk_label, awareness=awareness, probability=prob_pos, contributions=top_contribs, inputs=orig_row)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        if User.query.filter_by(username=username).first():
            flash('Username already exists')
            return redirect(url_for('signup'))
        if User.query.filter_by(email=email).first():
            flash('Email already exists')
            return redirect(url_for('signup'))
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        flash('Account created successfully')
        return redirect(url_for('login'))
    return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('dashboard'))
        flash('Invalid username or password')
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/resources')
@login_required
def resources():
    return render_template('resources.html')

@app.route('/settings')
@login_required
def settings():
    return render_template('settings.html')

@app.route('/dashboard')
@login_required
def dashboard():
    # Fetch recent predictions for the user
    recent_predictions = []
    try:
        with open(os.path.join(BASE_DIR, 'data', 'history.csv'), 'r', encoding='utf-8') as f:
            next(f)  # skip header
            for line in f:
                parts = line.strip().split(',', 4)
                if len(parts) == 5 and parts[0] == str(current_user.id):
                    ts = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(parts[1]))) if parts[1].isdigit() else parts[1]
                    prob = float(parts[2]) if parts[2] != '' else None
                    risk = parts[3]
                    summary = parts[4] if len(parts) > 4 else ''
                    recent_predictions.append({
                        'timestamp': ts,
                        'probability': prob,
                        'risk': risk,
                        'summary': summary
                    })
    except Exception as e:
        print('Dashboard history error:', e)
    # Reverse to get most recent first, then take last 5
    recent_predictions.reverse()
    recent_predictions = recent_predictions[-5:] if len(recent_predictions) > 5 else recent_predictions
    return render_template('dashboard.html', recent_predictions=recent_predictions)


if __name__ == "__main__":
    app.run(debug=True)
