import json
import pickle
import pandas as pd
import numpy as np
import os

mdir = os.path.join("model")
with open(os.path.join(mdir, "feature_columns.json"), "r", encoding="utf-8") as f:
    FEATURE_COLS = json.load(f)
with open(os.path.join(mdir, "original_features.json"), "r", encoding="utf-8") as f:
    ORIGINAL_FEATURES = json.load(f)

model = pickle.load(open(os.path.join(mdir, "rf_model.pkl"), "rb"))
encoder = pickle.load(open(os.path.join(mdir, "label_encoder.pkl"), "rb"))

print("Label encoder classes:", list(encoder.classes_))
print("Num feature columns expected:", len(FEATURE_COLS))

# Build several test cases varying Academic Pressure, Work Pressure, Financial Stress, Study Satisfaction
base = {k: 0 for k in ORIGINAL_FEATURES}
# set defaults for numeric fields that exist
for k in ["id", "Age", "CGPA", "Work/Study Hours"]:
    if k in base:
        base[k] = 20 if k=="Age" else 1.0

cases = []
# low-stress case
c1 = base.copy()
c1.update({"Academic Pressure": 1, "Work Pressure": 1, "Study Satisfaction": 5, "Job Satisfaction": 5, "Financial Stress": 1, "Gender": "Female"})
cases.append(("low_stress", c1))
# moderate
c2 = base.copy()
c2.update({"Academic Pressure": 3, "Work Pressure": 3, "Study Satisfaction": 3, "Job Satisfaction": 3, "Financial Stress": 3, "Gender": "Male"})
cases.append(("moderate", c2))
# high
c3 = base.copy()
c3.update({"Academic Pressure": 5, "Work Pressure": 5, "Study Satisfaction": 1, "Job Satisfaction": 1, "Financial Stress": 5, "Gender": "Male"})
cases.append(("high_stress", c3))

for name, case in cases:
    df_orig = pd.DataFrame([case])
    df_d = pd.get_dummies(df_orig, drop_first=True)
    X_in = df_d.reindex(columns=FEATURE_COLS, fill_value=0)
    print("\nCase:", name)
    print("Input nonzero columns:", [c for c, v in X_in.iloc[0].items() if v != 0][:30])
    try:
        probs = model.predict_proba(X_in)
        pred = model.predict(X_in)
        print("Probs:", probs)
        print("Pred:", pred, "Decoded:", encoder.inverse_transform(pred))
    except Exception as e:
        print("Model error:", e)
        print("X_in shape:", X_in.shape)
        print(X_in.head(1).to_string())

print("Done.")
