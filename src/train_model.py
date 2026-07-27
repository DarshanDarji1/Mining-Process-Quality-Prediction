from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt

from pathlib import Path

from sklearn.model_selection import train_test_split

print("=" * 60)
print("MODEL TRAINING")
print("=" * 60)

# -----------------------------------------------------
# Project Paths
# -----------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"

MODEL_DIR = BASE_DIR / "models"

OUTPUT_DIR = BASE_DIR / "outputs"

OUTPUT_DIR.mkdir(exist_ok=True)

MODEL_DIR.mkdir(exist_ok=True)

INPUT_FILE = DATA_DIR / "MiningProcess_Processed.csv"

# -----------------------------------------------------
# Load Dataset
# -----------------------------------------------------

print("\nLoading Dataset...")

df = pd.read_csv(INPUT_FILE)

# Use a representative sample for deployment
df = df.sample(n=100000, random_state=42)

print("Dataset Loaded Successfully.")

print(f"\nRows : {df.shape[0]}")
print(f"Columns : {df.shape[1]}")

print("\nColumns")

print(df.columns.tolist())


# -----------------------------------------------------
# Prepare Features and Target
# -----------------------------------------------------

print("\nPreparing Features and Target...")

# Target Variable
y = df["% Silica Concentrate"]

# Features
X = df.drop(columns=[
    "% Silica Concentrate",
    "% Iron Concentrate",
    "date",
    "Weekday"
])

print("\nFeature Matrix Shape :", X.shape)
print("Target Shape :", y.shape)

print("\nFeature Columns")

print(X.columns.tolist())

# -----------------------------------------------------
# Train Test Split
# -----------------------------------------------------

print("\nSplitting Dataset...")

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("\nTraining Samples :", len(X_train))
print("Testing Samples :", len(X_test))

print("\nData Preparation Completed.")


# -----------------------------------------------------
# Model Training
# -----------------------------------------------------

print("\nTraining Machine Learning Models...")

models = {
    "Linear Regression": LinearRegression(),
    "Decision Tree": DecisionTreeRegressor(random_state=42),
    "XGBoost": XGBRegressor(
    n_estimators=200,
    max_depth=6,
    learning_rate=0.1,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42,
    n_jobs=-1
)
}

results = []

best_model = None
best_score = float("-inf")
best_model_name = ""

for name, model in models.items():

    print(f"\nTraining {name}...")

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)

    rmse = np.sqrt(mean_squared_error(y_test, predictions))

    r2 = r2_score(y_test, predictions)

    print(f"MAE  : {mae:.4f}")
    print(f"RMSE : {rmse:.4f}")
    print(f"R²   : {r2:.4f}")

    results.append({
        "Model": name,
        "MAE": mae,
        "RMSE": rmse,
        "R2 Score": r2
    })

    if r2 > best_score:
        best_score = r2
        best_model = model
        best_model_name = name

print("\n" + "=" * 60)
print("BEST MODEL")
print("=" * 60)

print(f"Model : {best_model_name}")
print(f"R² Score : {best_score:.4f}")

# -----------------------------------------------------
# Save Best Model
# -----------------------------------------------------

print("\nSaving Best Model...")

model_path = MODEL_DIR / "mining_model.pkl"

joblib.dump(best_model, model_path)

print("\nFeature Importance")

importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": best_model.feature_importances_
})

importance = importance.sort_values("Importance", ascending=False)

print(importance)

print("Model Saved Successfully.")

# -----------------------------------------------------
# Save Model Results
# -----------------------------------------------------

print("\nSaving Model Results...")

results_df = pd.DataFrame(results)

results_file = OUTPUT_DIR / "model_results.csv"

results_df.to_csv(results_file, index=False)

print("Model Results Saved Successfully.")

print("\nFiles Created")

print(model_path)

print(results_file)

