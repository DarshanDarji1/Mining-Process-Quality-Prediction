import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# ==========================================================
# Mining Process Quality Prediction
# Exploratory Data Analysis (EDA)
# ==========================================================

print("=" * 60)
print("EXPLORATORY DATA ANALYSIS")
print("=" * 60)

# ----------------------------------------------------------
# Project Paths
# ----------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"

IMAGE_DIR = BASE_DIR / "images"

INPUT_FILE = DATA_DIR / "MiningProcess_Processed.csv"

IMAGE_DIR.mkdir(exist_ok=True)

# ----------------------------------------------------------
# Load Dataset
# ----------------------------------------------------------

print("\nLoading Processed Dataset...")

df = pd.read_csv(INPUT_FILE)

print("Dataset Loaded Successfully.")

print(f"\nRows : {df.shape[0]}")
print(f"Columns : {df.shape[1]}")

print("\nColumn Names")

print(df.columns.tolist())


# ----------------------------------------------------------
# Target Distribution
# ----------------------------------------------------------

print("\nCreating Target Distribution...")

plt.figure(figsize=(10,6))

sns.histplot(df["% Silica Concentrate"], bins=30, kde=True)

plt.title("Distribution of % Silica Concentrate")

plt.xlabel("% Silica Concentrate")

plt.ylabel("Frequency")

plt.tight_layout()

plt.savefig(IMAGE_DIR / "01_target_distribution.png")

plt.close()

# ----------------------------------------------------------
# Correlation Heatmap
# ----------------------------------------------------------

print("Creating Correlation Heatmap...")

numeric_df = df.select_dtypes(include=np.number)

plt.figure(figsize=(18,12))

sns.heatmap(
    numeric_df.corr(),
    cmap="coolwarm",
    linewidths=0.5
)

plt.title("Correlation Heatmap")

plt.tight_layout()

plt.savefig(IMAGE_DIR / "02_correlation_heatmap.png")

plt.close()

# ----------------------------------------------------------
# Histograms
# ----------------------------------------------------------

print("Creating Histograms...")

numeric_df.hist(
    figsize=(18,18),
    bins=30
)

plt.tight_layout()

plt.savefig(IMAGE_DIR / "03_feature_histograms.png")

plt.close()

print("\nPart 2 Completed.")


# ----------------------------------------------------------
# Boxplots
# ----------------------------------------------------------

print("Creating Boxplots...")

plt.figure(figsize=(20,12))

numeric_df.plot(
    kind="box",
    subplots=True,
    layout=(6,5),
    figsize=(20,20),
    sharex=False,
    sharey=False
)

plt.tight_layout()

plt.savefig(IMAGE_DIR / "04_boxplots.png")

plt.close("all")

# ----------------------------------------------------------
# Correlation with Target
# ----------------------------------------------------------

print("Creating Target Correlation...")

target_corr = numeric_df.corr()["% Silica Concentrate"].sort_values()

plt.figure(figsize=(10,8))

target_corr.plot(kind="barh")

plt.title("Correlation with % Silica Concentrate")

plt.tight_layout()

plt.savefig(IMAGE_DIR / "05_target_correlation.png")

plt.close()

# ----------------------------------------------------------
# Pairplot (Sample)
# ----------------------------------------------------------

print("Creating Pairplot...")

sample_df = df.sample(100, random_state=42)

pair_columns = [
    "% Iron Feed",
    "% Silica Feed",
    "% Iron Concentrate",
    "% Silica Concentrate"
]

sns.pairplot(sample_df[pair_columns])

plt.savefig(IMAGE_DIR / "06_pairplot.png")

plt.close("all")

print("\nAll graphs generated successfully.")