import os
import sys
import pandas as pd
import numpy as np
import pickle

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report


# 1. Load dataset
csv_path = os.path.join("dataset", "student_depression.csv")
df = pd.read_csv(csv_path)

# Helper: try to resolve if the file is just a pointer to another CSV path
def try_follow_pointer(df):
    # If single-column file that contains a path to the real CSV, try to read it
    if df.shape[1] == 1:
        # Case A: value exists as first row (no header)
        if df.shape[0] >= 1:
            first = str(df.iloc[0, 0]).strip()
            first_stripped = first.strip('"').strip("'")
            if os.path.exists(first_stripped):
                try:
                    return pd.read_csv(first_stripped)
                except Exception:
                    return df
        # Case B: file has a single column name that is actually a path (header-only)
        if df.shape[0] == 0:
            possible_path = str(df.columns[0]).strip()
            possible_path_stripped = possible_path.strip('"').strip("'")
            if os.path.exists(possible_path_stripped):
                try:
                    return pd.read_csv(possible_path_stripped)
                except Exception:
                    return df
    return df

# Attempt pointer-following once
df = try_follow_pointer(df)

# 2. Find target column (be tolerant to variations)
target_col = None
if "Depression_Level" in df.columns:
    target_col = "Depression_Level"
else:
    for col in df.columns:
        if "depress" in str(col).lower():
            target_col = col
            break

if target_col is None:
    print("ERROR: Could not find a target column containing 'depress'.")
    print("Available columns:", list(df.columns))
    sys.exit(1)

# If dataset is empty, provide a clear diagnostic and exit
if df.shape[0] == 0:
    print("ERROR: Loaded dataset is empty (0 rows).")
    print("Original CSV path:", csv_path)
    print("Available columns:", list(df.columns))
    print("First lines (if any):")
    try:
        print(df.head(10).to_string(index=False))
    except Exception:
        pass
    sys.exit(1)

# 3. Encode target label
le = LabelEncoder()
df[target_col] = le.fit_transform(df[target_col])

# 4. Separate features & target
X = df.drop(columns=[target_col])
y = df[target_col]

# Save original feature names (before one-hot encoding) so runtime can map form inputs
import json
original_features = X.columns.tolist()
with open("model/original_features.json", "w", encoding="utf-8") as f:
    json.dump(original_features, f)

# Ensure feature matrix is numeric: one-hot encode categorical columns
X = pd.get_dummies(X, drop_first=True)
X = X.fillna(0)

# Sanity checks
if y.nunique() < 2:
    print("ERROR: Target has fewer than 2 classes:", list(y.unique()))
    sys.exit(1)

# 4. Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 5. Hyperparameter tuning
params = {
    "n_estimators": [100, 200],
    "max_depth": [None, 10, 20],
    "min_samples_split": [2, 5],
    "min_samples_leaf": [1, 2]
}

rf = RandomForestClassifier(random_state=42)

grid = GridSearchCV(
    rf,
    params,
    cv=5,
    scoring="accuracy",
    n_jobs=-1
)

try:
    grid.fit(X_train, y_train)
except Exception as e:
    print("ERROR during model fitting:\n", str(e))
    print("X_train shape:", X_train.shape)
    print("Example X_train dtypes:\n", X_train.dtypes.head(20))
    sys.exit(1)

best_model = grid.best_estimator_

# 6. Evaluation
predictions = best_model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, predictions))
print(classification_report(y_test, predictions))

# 7. Save model + encoder
pickle.dump(best_model, open("model/rf_model.pkl", "wb"))
pickle.dump(le, open("model/label_encoder.pkl", "wb"))
# 8. Save feature column list used for training so runtime can align inputs
import json
feature_cols = X.columns.tolist()
with open("model/feature_columns.json", "w", encoding="utf-8") as f:
    json.dump(feature_cols, f)
