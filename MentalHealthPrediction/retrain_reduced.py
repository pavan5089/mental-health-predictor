import os
import sys
import json
import pickle
import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report

# Load dataset (reuse pointer logic)
csv_path = os.path.join("dataset", "student_depression.csv")
df = pd.read_csv(csv_path)

# follow pointer if needed
if df.shape[1] == 1:
    first = str(df.columns[0]).strip()
    if os.path.exists(first):
        df = pd.read_csv(first)

# locate target
target_col = None
for c in df.columns:
    if 'depress' in str(c).lower():
        target_col = c
        break
if target_col is None:
    print('Could not find target column containing "depress"')
    sys.exit(1)

# label encode target
le = LabelEncoder()
df[target_col] = le.fit_transform(df[target_col])

# Selected visible features (matching the current form)
selected = [
    "Gender",
    "Age",
    "Academic Pressure",
    "Work Pressure",
    "CGPA",
    "Study Satisfaction",
    "Sleep Duration",
    "Degree",
    "Work/Study Hours",
    "Financial Stress",
    "Family History of Mental Illness",
]

missing = [c for c in selected if c not in df.columns]
if missing:
    print("Warning: some selected features not in dataset:", missing)

X = df[[c for c in selected if c in df.columns]].copy()
y = df[target_col]

# one-hot encode categorical & fill
X = pd.get_dummies(X, drop_first=True)
X = X.fillna(0)

# Save original and feature columns
os.makedirs('model', exist_ok=True)
with open('model/original_features.json', 'w', encoding='utf-8') as f:
    json.dump(selected, f)
with open('model/feature_columns.json', 'w', encoding='utf-8') as f:
    json.dump(X.columns.tolist(), f)

# train/test split
if X.shape[0] == 0:
    print('No training rows found after filtering features. Abort.')
    sys.exit(1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# model with class_weight to handle imbalance
rf = RandomForestClassifier(random_state=42, class_weight='balanced')
params = {'n_estimators':[100,200], 'max_depth':[None, 10, 20]}
grid = GridSearchCV(rf, params, cv=3, scoring='accuracy', n_jobs=-1)

print('Training reduced model...')
grid.fit(X_train, y_train)
best = grid.best_estimator_

preds = best.predict(X_test)
print('Accuracy:', accuracy_score(y_test, preds))
print(classification_report(y_test, preds))

# save model + encoder
pickle.dump(best, open('model/rf_model.pkl', 'wb'))
pickle.dump(le, open('model/label_encoder.pkl', 'wb'))
print('Saved model to model/rf_model.pkl')

# quick sanity: print feature count
print('Feature columns used:', len(X.columns))
