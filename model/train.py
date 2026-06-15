import pandas as pd
import numpy as np
import os
from lightgbm import LGBMRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)
import matplotlib.pyplot as plt
import shap
import joblib

MODELS_DIR = "model/"


## Carga Data
winesssss = pd.read_parquet("data/processed/winequality-red.parquet", engine='pyarrow')


## Train Test Split
cols = winesssss.drop(columns=['quality']).columns.to_list()
target = 'quality'

X = winesssss[cols]
y = winesssss[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


## Retirando features correlacionados
cols.remove('fixed acidity')
cols.remove('free sulfur dioxide')


## Train Model
model = LGBMRegressor(
    n_estimators=500,
    learning_rate=0.05,
    max_depth=5,
    random_state=42,
    verbose = -1
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

## Guarda Modelo
joblib.dump(model, MODELS_DIR+"lightgbm_model.joblib")


