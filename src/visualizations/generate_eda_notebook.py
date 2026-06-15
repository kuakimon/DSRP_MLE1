from pathlib import Path
import nbformat as nbf

# ==========================================
# CONFIGURACIÓN
# ==========================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

NOTEBOOK_DIR = PROJECT_ROOT / "notebooks"
NOTEBOOK_DIR.mkdir(exist_ok=True)

NOTEBOOK_PATH = NOTEBOOK_DIR / "01_eda.ipynb"

DATASET_PATH = "../data/raw/winequality-red.csv"

# ==========================================
# CREAR NOTEBOOK
# ==========================================

nb = nbf.v4.new_notebook()

cells = []

# ------------------------------------------
# TÍTULO
# ------------------------------------------

cells.append(
    nbf.v4.new_markdown_cell(
        """
# Wine Quality - Exploratory Data Analysis

Dataset utilizado para predecir la calidad del vino tinto.

**Target:** `quality`
"""
    )
)

# ------------------------------------------
# IMPORTS
# ------------------------------------------

cells.append(
    nbf.v4.new_code_cell(
        f"""import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

TARGET = "quality"

df = pd.read_csv("{DATASET_PATH}")

print(df.shape)

df.head()"""
    )
)

# ------------------------------------------
# DATASET OVERVIEW
# ------------------------------------------

cells.append(
    nbf.v4.new_markdown_cell(
        """## Dataset Overview"""
    )
)

cells.append(
    nbf.v4.new_code_cell(
        """print("Shape:")
print(df.shape)

print("\\nColumns:")
print(df.columns.tolist())

print("\\nData Types:")
display(df.dtypes)"""
    )
)

# ------------------------------------------
# MISSING VALUES
# ------------------------------------------

cells.append(
    nbf.v4.new_markdown_cell(
        """
## Missing Values
"""
    )
)

cells.append(
    nbf.v4.new_code_cell(
        """missing = pd.DataFrame({
    "missing_count": df.isnull().sum(),
    "missing_pct": df.isnull().mean() * 100
})

missing.sort_values(
    by="missing_count",
    ascending=False
)"""
    )
)

# ------------------------------------------
# DESCRIPTIVE STATS
# ------------------------------------------

cells.append(
    nbf.v4.new_markdown_cell(
        """## Descriptive Statistics"""
    )
)

cells.append(
    nbf.v4.new_code_cell(
        """df.describe().T"""
    )
)

# ------------------------------------------
# TARGET DISTRIBUTION
# ------------------------------------------

cells.append(
    nbf.v4.new_markdown_cell(
        """## Target Distribution"""
    )
)

cells.append(
    nbf.v4.new_code_cell(
        """plt.figure(figsize=(8,5))

sns.countplot(
    data=df,
    x=TARGET
)

plt.title("Distribution of Quality")
plt.show()"""
    )
)

# ------------------------------------------
# HISTOGRAMS
# ------------------------------------------

cells.append(
    nbf.v4.new_markdown_cell(
        """## Feature Distributions"""
    )
)

cells.append(
    nbf.v4.new_code_cell(
        """df.hist(
    figsize=(16,12),
    bins=30
)

plt.tight_layout()
plt.show()"""
    )
)

# ------------------------------------------
# CORRELATION MATRIX
# ------------------------------------------

cells.append(
    nbf.v4.new_markdown_cell(
        """## Correlation Matrix"""
    )
)

cells.append(
    nbf.v4.new_code_cell(
        """corr = df.corr(numeric_only=True)

plt.figure(figsize=(12,8))

sns.heatmap(
    corr,
    cmap="coolwarm",
    annot=True,
    fmt=".2f",
    center=0
)

plt.title("Correlation Matrix")
plt.show()"""
    )
)

# ------------------------------------------
# CORRELATION WITH TARGET
# ------------------------------------------

cells.append(
    nbf.v4.new_markdown_cell(
        """## Correlation with Target"""
    )
)

cells.append(
    nbf.v4.new_code_cell(
        """target_corr = (
    corr[TARGET]
    .sort_values(ascending=False)
)

target_corr"""
    )
)

cells.append(
    nbf.v4.new_code_cell(
        """plt.figure(figsize=(10,5))

target_corr.drop(TARGET).plot(
    kind="bar"
)

plt.title("Feature Correlation with Quality")
plt.ylabel("Correlation")

plt.show()"""
    )
)

# ------------------------------------------
# TOP FEATURES VS TARGET
# ------------------------------------------

cells.append(
    nbf.v4.new_markdown_cell(
        """## Top Features vs Target"""
    )
)

cells.append(
    nbf.v4.new_code_cell(
        """top_features = (
    target_corr
    .drop(TARGET)
    .abs()
    .sort_values(ascending=False)
    .head(5)
    .index
)

top_features"""
    )
)

cells.append(
    nbf.v4.new_code_cell(
        """for feature in top_features:

    plt.figure(figsize=(8,4))

    sns.boxplot(
        data=df,
        x=TARGET,
        y=feature
    )

    plt.title(f"{feature} vs {TARGET}")

    plt.show()"""
    )
)

# ------------------------------------------
# OUTLIERS
# ------------------------------------------

cells.append(
    nbf.v4.new_markdown_cell(
        """## Outlier Analysis"""
    )
)

cells.append(
    nbf.v4.new_code_cell(
        """numeric_cols = df.select_dtypes(
    include="number"
).columns

for col in numeric_cols:

    plt.figure(figsize=(8,2))

    sns.boxplot(
        x=df[col]
    )

    plt.title(col)

    plt.show()"""
    )
)

# # ------------------------------------------
# # CONCLUSIONES
# # ------------------------------------------

# cells.append(
#     nbf.v4.new_markdown_cell(
#         """## Conclusions

# Completar manualmente después de ejecutar el EDA:

# - Variables más correlacionadas con `quality`.
# - Posibles outliers.
# - Distribuciones sesgadas.
# - Necesidad de escalamiento.
# - Necesidad de transformaciones.
# - Posibles variables predictoras."""
#     )
# )

nb["cells"] = cells

with open(NOTEBOOK_PATH, "w", encoding="utf-8") as f:
    nbf.write(nb, f)

print(f"Notebook generado correctamente: {NOTEBOOK_PATH}")