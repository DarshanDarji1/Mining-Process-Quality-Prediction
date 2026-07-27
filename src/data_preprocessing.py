# ==========================================================
# Mining Process Quality Prediction
# Data Preprocessing
# ==========================================================

import pandas as pd
import numpy as np
from pathlib import Path

print("=" * 60)
print("MINING PROCESS DATA PREPROCESSING")
print("=" * 60)

# ----------------------------------------------------------
# Project Paths
# ----------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"

INPUT_FILE = DATA_DIR / "MiningProcess_Flotation_Plant_Database.csv"

OUTPUT_FILE = DATA_DIR / "MiningProcess_Processed.csv"

# ----------------------------------------------------------
# Load Dataset
# ----------------------------------------------------------

print("\nLoading dataset...")

df = pd.read_csv(INPUT_FILE)

print("Dataset loaded successfully.")

# ----------------------------------------------------------
# Basic Information
# ----------------------------------------------------------

print("\nDataset Shape")
print(df.shape)

print("\nColumn Names")
print(df.columns.tolist())

print("\nData Types")
print(df.dtypes)

# ----------------------------------------------------------
# Missing Values
# ----------------------------------------------------------

print("\nMissing Values")

print(df.isnull().sum())

# ----------------------------------------------------------
# Duplicate Records
# ----------------------------------------------------------

duplicates = df.duplicated().sum()

print(f"\nDuplicate Rows : {duplicates}")

if duplicates > 0:
    df = df.drop_duplicates()
    print("Duplicate rows removed.")

# ----------------------------------------------------------
# Convert Date Column
# ----------------------------------------------------------

print("\nConverting Date Column...")

df["date"] = pd.to_datetime(df["date"])

# ----------------------------------------------------------
# Feature Engineering
# ----------------------------------------------------------

print("Creating Time Features...")

df["Year"] = df["date"].dt.year
df["Month"] = df["date"].dt.month
df["Day"] = df["date"].dt.day
df["Hour"] = df["date"].dt.hour
df["Weekday"] = df["date"].dt.day_name()

# ----------------------------------------------------------
# Check Numeric Columns
# ----------------------------------------------------------

numeric_cols = df.select_dtypes(include=np.number).columns

print("\nNumeric Columns")

print(numeric_cols)

# ----------------------------------------------------------
# Remove Negative Values
# ----------------------------------------------------------

for col in numeric_cols:
    df = df[df[col] >= 0]

print("\nNegative value check completed.")

# ----------------------------------------------------------
# Summary Statistics
# ----------------------------------------------------------

print("\nSummary Statistics")

print(df.describe())

# ----------------------------------------------------------
# Data Validation
# ----------------------------------------------------------

print("\n" + "=" * 60)
print("DATA VALIDATION")
print("=" * 60)

print(f"Rows      : {df.shape[0]}")
print(f"Columns   : {df.shape[1]}")

print("\nMissing Values")

missing = df.isnull().sum()

print(missing)

if missing.sum() == 0:
    print("\nNo Missing Values Found")
else:
    print("\nMissing values still exist.")

print("\nDuplicate Rows")

duplicates = df.duplicated().sum()

print(duplicates)

if duplicates == 0:
    print("No Duplicate Rows Found")
else:
    print("Duplicates still exist")

print("\nData Types")

print(df.dtypes)

print("\nValidation Completed Successfully.")

# ----------------------------------------------------------
# Save Processed Dataset
# ----------------------------------------------------------

df.to_csv(OUTPUT_FILE, index=False)

print("\nProcessed dataset saved successfully.")

print(OUTPUT_FILE)

print("=" * 60)
print("PREPROCESSING COMPLETED")
print("=" * 60)