from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# CONFIGURACIÓN
# ==========================================

TARGET = "quality"

DATA_PATH = "data/raw/winequality-red.csv"

REPORTS_DIR = Path("reports/eda")
REPORTS_DIR.mkdir(parents=True, exist_ok=True)

sns.set_theme(style="whitegrid")

# ==========================================
# CARGA DE DATOS
# ==========================================

df = pd.read_csv(DATA_PATH)

# ==========================================
# REPORTE GENERAL
# ==========================================

report = []

report.append("# Exploratory Data Analysis\n")

report.append("## Dataset Shape")
report.append(f"- Filas: {df.shape[0]}")
report.append(f"- Columnas: {df.shape[1]}\n")

report.append("## Missing Values")
report.append(df.isnull().sum().to_markdown())
report.append("")

report.append("## Data Types")
report.append(df.dtypes.to_frame("dtype").to_markdown())
report.append("")

report.append("## Descriptive Statistics")
report.append(df.describe().to_markdown())
report.append("")

# ==========================================
# DISTRIBUCIÓN DEL TARGET
# ==========================================

plt.figure(figsize=(8, 5))
sns.countplot(data=df, x=TARGET)

plt.title("Target Distribution")
plt.tight_layout()

target_plot = REPORTS_DIR / "target_distribution.png"
plt.savefig(target_plot)
plt.close()

report.append("## Target Distribution")
report.append(f"![target](target_distribution.png)")
report.append("")

# ==========================================
# HISTOGRAMAS
# ==========================================

numeric_cols = df.select_dtypes(include="number").columns

for col in numeric_cols:

    plt.figure(figsize=(7, 4))

    sns.histplot(
        df[col],
        kde=True,
        bins=30
    )

    plt.title(col)

    filename = f"hist_{col.replace(' ', '_')}.png"

    plt.tight_layout()
    plt.savefig(REPORTS_DIR / filename)
    plt.close()

# ==========================================
# MATRIZ DE CORRELACIÓN
# ==========================================

corr = df.corr(numeric_only=True)

plt.figure(figsize=(10, 8))

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Matrix")

plt.tight_layout()

corr_file = REPORTS_DIR / "correlation_matrix.png"

plt.savefig(corr_file)
plt.close()

report.append("## Correlation Matrix")
report.append("![corr](correlation_matrix.png)")
report.append("")

# ==========================================
# CORRELACIÓN CON TARGET
# ==========================================

target_corr = (
    corr[TARGET]
    .sort_values(ascending=False)
)

report.append("## Correlation With Target")
report.append(target_corr.to_frame("correlation").to_markdown())
report.append("")

# ==========================================
# TOP FEATURES
# ==========================================

top_features = (
    target_corr
    .drop(TARGET)
    .abs()
    .sort_values(ascending=False)
    .head(5)
    .index
)

for feature in top_features:

    plt.figure(figsize=(8, 5))

    sns.boxplot(
        data=df,
        x=TARGET,
        y=feature
    )

    plt.title(f"{feature} vs {TARGET}")

    filename = (
        f"{feature.replace(' ', '_')}_vs_target.png"
    )

    plt.tight_layout()
    plt.savefig(REPORTS_DIR / filename)
    plt.close()

    report.append(f"## {feature} vs {TARGET}")
    report.append(f"![{feature}]({filename})")
    report.append("")

# ==========================================
# GUARDAR REPORTE
# ==========================================

with open(
    REPORTS_DIR / "eda_report.md",
    "w",
    encoding="utf-8"
) as f:
    f.write("\n".join(report))

print("EDA generado correctamente.")
print(f"Reporte: {REPORTS_DIR / 'eda_report.md'}")