# Wine Quality Prediction - DSRP MLE1

## 1. Problema de Machine Learning

### Objetivo

El objetivo de este proyecto es predecir la calidad de un vino tinto a partir de sus propiedades fisicoquímicas.

La variable objetivo es:

* **quality**: puntuación de calidad asignada al vino.

### Tipo de problema

Se plantea como un problema de **Machine Learning Supervisado de Regresión**, donde:

* Variables de entrada: características químicas del vino.
* Variable de salida: calidad del vino (`quality`).

### Caso de negocio

La capacidad de estimar automáticamente la calidad de un vino permite:

* Reducir costos de evaluación manual.
* Priorizar muestras para análisis sensorial.
* Detectar lotes potencialmente defectuosos.
* Mejorar el control de calidad durante la producción.

---

## 2. Arquitectura y Flujo del Proyecto

```text
                           ┌─────────────┐
                           │ Kaggle/UCI  │
                           │ Wine Dataset│
                           └──────┬──────┘
                                  │
                                  ▼
                      ┌────────────────────┐
                      │ Data Ingestion     │
                      └─────────┬──────────┘
                                │
                                ▼
                      ┌────────────────────┐
                      │ Data Validation    │
                      └─────────┬──────────┘
                                │
                                ▼
                      ┌────────────────────┐
                      │ Data Processing    │
                      └─────────┬──────────┘
                                │
                                ▼
                      ┌────────────────────┐
                      │ Exploratory Data   │
                      │ Analysis (EDA)     │
                      └─────────┬──────────┘
                                │
                                ▼
                      ┌────────────────────┐
                      │ Feature Selection  │
                      └─────────┬──────────┘
                                │
                                ▼
                      ┌────────────────────┐
                      │ LightGBM Training  │
                      └─────────┬──────────┘
                                │
                                ▼
                      ┌────────────────────┐
                      │ Model Evaluation   │
                      └─────────┬──────────┘
                                │
                                ▼
                      ┌────────────────────┐
                      │ SHAP Explainability│
                      └─────────┬──────────┘
                                │
                                ▼
                      ┌────────────────────┐
                      │ Model Artifacts    │
                      └────────────────────┘
```

---

## 3. Dataset

### Fuente

Dataset: Red Wine Quality Dataset

Basado en el trabajo de Cortez et al. (2009), ampliamente utilizado para tareas de regresión y clasificación de calidad de vinos.

### Tamaño

* Registros: 1,599
* Variables predictoras: 11
* Variable objetivo: 1 (`quality`)

---

## 4. Diccionario de Datos

| Variable             | Descripción                                |
| -------------------- | ------------------------------------------ |
| fixed acidity        | Acidez fija del vino                       |
| volatile acidity     | Cantidad de ácido acético presente         |
| citric acid          | Cantidad de ácido cítrico                  |
| residual sugar       | Azúcar residual después de la fermentación |
| chlorides            | Concentración de cloruros                  |
| free sulfur dioxide  | Dióxido de azufre libre                    |
| total sulfur dioxide | Dióxido de azufre total                    |
| density              | Densidad del vino                          |
| pH                   | Nivel de pH                                |
| sulphates            | Concentración de sulfatos                  |
| alcohol              | Porcentaje de alcohol                      |
| quality              | Calidad del vino (target)                  |

Descripción basada en la documentación original del dataset.

---

## 5. Exploratory Data Analysis

### Principales Hallazgos

* No se identificaron valores nulos.
* La distribución de `quality` presenta desbalance.
* Alcohol mostró correlación positiva con la calidad.
* Volatile Acidity mostró correlación negativa con la calidad.
* Se detectaron outliers en múltiples variables fisicoquímicas.

### Correlaciones Relevantes

| Variable         | Relación esperada con quality |
| ---------------- | ----------------------------- |
| alcohol          | Positiva                      |
| sulphates        | Positiva                      |
| volatile acidity | Negativa                      |
| density          | Negativa                      |

---

## 6. Modelo Utilizado

### Algoritmo

* LightGBM Regressor

### Justificación

LightGBM fue seleccionado debido a:

* Excelente desempeño en datos tabulares.
* Capacidad para modelar relaciones no lineales.
* Manejo eficiente de variables numéricas.
* Interpretabilidad mediante Feature Importance y SHAP.

---

## 7. Model Card

### Información General

| Campo             | Valor                         |
| ----------------- | ----------------------------- |
| Nombre            | Wine Quality Predictor        |
| Tipo              | Regressor                     |
| Framework         | LightGBM                      |
| Objetivo          | Predicción de calidad de vino |
| Variable objetivo | quality                       |
| Dominio           | Food & Beverage               |

### Datos de Entrenamiento

| Campo     | Valor            |
| --------- | ---------------- |
| Dataset   | Red Wine Quality |
| Registros | 1,599            |
| Features  | 11               |
| Target    | quality          |

### Usuarios Esperados

* Analistas de calidad.
* Equipos de control de producción.
* Científicos de datos.
* Investigadores académicos.

### Limitaciones

* Dataset relativamente pequeño.
* Solo contiene variables fisicoquímicas.
* No incluye información de marca, precio o tipo de uva.
* Puede no generalizar a vinos fuera del contexto del dataset original.

### Consideraciones Éticas

* No se identifican riesgos de privacidad.
* Uso restringido a soporte de decisiones.
* No reemplaza evaluación sensorial profesional.

---

## 8. Explainability

### Feature Importance

Las variables más influyentes identificadas por LightGBM fueron:

1. chlorides
2. total sulfur dioxide
3. density
4. pH
5. volatile acidity

### SHAP Analysis

El análisis SHAP permitió:

* Identificar variables con mayor impacto en la predicción.
* Explicar predicciones individuales.
* Comprender relaciones no lineales entre variables y calidad.

---

## 9. Resultados

### Métricas Offline

| Métrica | Valor |
| ------- | ----- |
| RMSE    | 0.58  |
| MAE     | 0.44  |
| R²      | 0.49  |

### Métricas Online

> No se realizaron pruebas online. El proyecto fue evaluado únicamente mediante métricas offline.

---

## 10. Reproducibilidad

### Instalación

```bash
git clone https://github.com/kuakimon/DSRP_MLE1.git

cd DSRP_MLE1

uv sync
```

### EDA

```bash
uv run python src/visualizations/generate_eda_notebook.py
```

### Entrenamiento

```bash
uv run python src/model/train.py
```

---

## 11. Conclusiones

* LightGBM logró modelar adecuadamente la calidad del vino utilizando únicamente variables fisicoquímicas.
* Alcohol y Volatile Acidity fueron algunas de las variables con mayor influencia en las predicciones.
* SHAP permitió interpretar el comportamiento del modelo y validar hallazgos obtenidos durante el EDA.
* El modelo puede utilizarse como apoyo para procesos de control de calidad.

### Trabajo Futuro

* Implementar búsqueda de hiperparámetros.
* Evaluar CatBoost y XGBoost.
* Implementar monitoreo del modelo.
* Desplegar mediante API para inferencia en tiempo real.
* Incorporar datasets de vinos blancos y otras variedades.

```
```
