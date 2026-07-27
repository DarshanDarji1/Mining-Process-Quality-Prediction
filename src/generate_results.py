import pandas as pd
import matplotlib.pyplot as plt
import joblib

from pathlib import Path

from sklearn.model_selection import train_test_split

print("=" * 60)
print("GENERATING MODEL RESULTS")
print("=" * 60)

# -----------------------------------------------------
# Project Paths
# -----------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
MODEL_DIR = BASE_DIR / "models"
OUTPUT_DIR = BASE_DIR / "outputs"
IMAGE_DIR = BASE_DIR / "images"

INPUT_FILE = DATA_DIR / "MiningProcess_Processed.csv"

MODEL_FILE = MODEL_DIR / "mining_model.pkl"

RESULT_FILE = OUTPUT_DIR / "model_results.csv"


# -----------------------------------------------------
# Load Dataset
# -----------------------------------------------------

print("\nLoading Processed Dataset...")

df = pd.read_csv(INPUT_FILE)

print("Dataset Loaded Successfully.")

# Prepare Features and Target
X = df.drop(columns=[
    "% Silica Concentrate",
    "% Iron Concentrate",
    "date",
    "Weekday"
])

y = df["% Silica Concentrate"]

# Same split used during training
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# -----------------------------------------------------
# Load Saved Model
# -----------------------------------------------------

print("\nLoading Saved Model...")

model = joblib.load(MODEL_FILE)

print("Model Loaded Successfully.")

# -----------------------------------------------------
# Load Model Results
# -----------------------------------------------------

print("\nLoading Model Results...")

results_df = pd.read_csv(RESULT_FILE)

print(results_df)


# -----------------------------------------------------
# Make Predictions
# -----------------------------------------------------

print("\nGenerating Predictions...")

predictions = model.predict(X_test)

# -----------------------------------------------------
# Model Comparison Graph
# -----------------------------------------------------

print("Creating Model Comparison Graph...")

plt.figure(figsize=(8,5))

plt.bar(
    results_df["Model"],
    results_df["R2 Score"]
)

plt.title("Model Comparison (R² Score)")
plt.ylabel("R² Score")

plt.tight_layout()

comparison_file = IMAGE_DIR / "07_model_comparison.png"

plt.savefig(comparison_file)

plt.close()

# -----------------------------------------------------
# Actual vs Predicted Graph
# -----------------------------------------------------

print("Creating Actual vs Predicted Graph...")

sample_size = min(5000, len(y_test))

actual = y_test.iloc[:sample_size]
predicted = predictions[:sample_size]

plt.figure(figsize=(7,7))

plt.scatter(
    actual,
    predicted,
    alpha=0.4
)

min_value = min(actual.min(), predicted.min())
max_value = max(actual.max(), predicted.max())

plt.plot(
    [min_value, max_value],
    [min_value, max_value],
    "r--",
    linewidth=2
)

plt.xlabel("Actual Silica Concentrate")
plt.ylabel("Predicted Silica Concentrate")
plt.title("Actual vs Predicted")

plt.tight_layout()

prediction_file = IMAGE_DIR / "08_actual_vs_predicted.png"

plt.savefig(prediction_file)

plt.close()

print("\nGraphs Generated Successfully.")

print(comparison_file)
print(prediction_file)