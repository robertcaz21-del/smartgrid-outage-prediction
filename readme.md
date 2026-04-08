# ⚡ Smart Grid Outage Prediction

## 📌 Descripción del Problema
Este proyecto tiene como objetivo predecir condiciones de riesgo de fallas eléctricas (outages) utilizando datos de medidores inteligentes.

Se utilizan perfiles de carga cuartihorarios junto con eventos eléctricos para identificar patrones que preceden a interrupciones del servicio.

---

## 📊 Datos Utilizados
- Perfiles de carga (~ delimitados)
- Intervalos de 15 minutos (96 por día)
- Tamaño aproximado:
  - Perfiles de carga: 5.63 GB
  - Eventos: 150 MB

Los datos no se incluyen en el repositorio debido a su tamaño.

---

## ⚙️ Pipeline del Proyecto

### 1. Limpieza de datos
- Lectura de múltiples archivos (~)
- Filtrado de medidores indirectos
- Eliminación de valores inválidos (flags "N")

### 2. Interval Parsing
- Separación de valor y calidad
- Construcción de timestamps a partir de FirstIntervalDateTime

### 3. Transformación (Pivot)
- Conversión de formato long → wide
- 1 fila por timestamp por medidor

### 4. Feature Engineering
- Voltaje promedio y desbalance
- Corriente promedio
- Sag y Swell
- Disturbance score
- Tendencias y variabilidad

### 5. Integración de eventos
- Join con eventos de outage/restore
- Creación de variable objetivo (t+3)

### 6. Modelado
Se evaluaron múltiples modelos:
- Logistic Regression
- ANN (MLP)
- XGBoost

---

## 📏 Métrica
Se utilizó **Precision Top-K**, adecuada para eventos raros.

---

## 🏆 Resultados
- XGBoost obtuvo el mejor desempeño:
  - Precision Top-K: **0.076**
  - Outages detectados: **76**
  - ≈190 veces mejor que el azar

---

## 🧠 Insights
- Los disturbios eléctricos (Sag, Disturbance) son fuertes predictores
- La variabilidad del voltaje es clave para anticipar fallas
- El voltaje promedio por sí solo no es suficiente

---

## 📁 Estructura del repositorio
# ⚡ Smart Grid Outage Prediction

## 📌 Descripción del Problema
Este proyecto tiene como objetivo predecir condiciones de riesgo de fallas eléctricas (outages) utilizando datos de medidores inteligentes.

Se utilizan perfiles de carga cuartihorarios junto con eventos eléctricos para identificar patrones que preceden a interrupciones del servicio.

---

## 📊 Datos Utilizados
- Perfiles de carga (~ delimitados)
- Intervalos de 15 minutos (96 por día)
- Tamaño aproximado:
  - Perfiles de carga: 5.63 GB
  - Eventos: 150 MB

Los datos no se incluyen en el repositorio debido a su tamaño.

---

## ⚙️ Pipeline del Proyecto

### 1. Limpieza de datos
- Lectura de múltiples archivos (~)
- Filtrado de medidores indirectos
- Eliminación de valores inválidos (flags "N")

### 2. Interval Parsing
- Separación de valor y calidad
- Construcción de timestamps a partir de FirstIntervalDateTime

### 3. Transformación (Pivot)
- Conversión de formato long → wide
- 1 fila por timestamp por medidor

### 4. Feature Engineering
- Voltaje promedio y desbalance
- Corriente promedio
- Sag y Swell
- Disturbance score
- Tendencias y variabilidad

### 5. Integración de eventos
- Join con eventos de outage/restore
- Creación de variable objetivo (t+3)

### 6. Modelado
Se evaluaron múltiples modelos:
- Logistic Regression
- ANN (MLP)
- XGBoost

---

## 📏 Métrica
Se utilizó **Precision Top-K**, adecuada para eventos raros.

---

## 🏆 Resultados
- XGBoost obtuvo el mejor desempeño:
  - Precision Top-K: **0.076**
  - Outages detectados: **76**
  - ≈190 veces mejor que el azar

---

## 🧠 Insights
- Los disturbios eléctricos (Sag, Disturbance) son fuertes predictores
- La variabilidad del voltaje es clave para anticipar fallas
- El voltaje promedio por sí solo no es suficiente

---

## 📁 Estructura del repositorio
# ⚡ Smart Grid Outage Prediction

## 📌 Descripción del Problema
Este proyecto tiene como objetivo predecir condiciones de riesgo de fallas eléctricas (outages) utilizando datos de medidores inteligentes.

Se utilizan perfiles de carga cuartihorarios junto con eventos eléctricos para identificar patrones que preceden a interrupciones del servicio.

---

## 📊 Datos Utilizados
- Perfiles de carga (~ delimitados)
- Intervalos de 15 minutos (96 por día)
- Tamaño aproximado:
  - Perfiles de carga: 5.63 GB
  - Eventos: 150 MB

Los datos no se incluyen en el repositorio debido a su tamaño.

---

## ⚙️ Pipeline del Proyecto

### 1. Limpieza de datos
- Lectura de múltiples archivos (~)
- Filtrado de medidores indirectos
- Eliminación de valores inválidos (flags "N")

### 2. Interval Parsing
- Separación de valor y calidad
- Construcción de timestamps a partir de FirstIntervalDateTime

### 3. Transformación (Pivot)
- Conversión de formato long → wide
- 1 fila por timestamp por medidor

### 4. Feature Engineering
- Voltaje promedio y desbalance
- Corriente promedio
- Sag y Swell
- Disturbance score
- Tendencias y variabilidad

### 5. Integración de eventos
- Join con eventos de outage/restore
- Creación de variable objetivo (t+3)

### 6. Modelado
Se evaluaron múltiples modelos:
- Logistic Regression
- ANN (MLP)
- XGBoost

---

## 📏 Métrica
Se utilizó **Precision Top-K**, adecuada para eventos raros.

---

## 🏆 Resultados
- XGBoost obtuvo el mejor desempeño:
  - Precision Top-K: **0.076**
  - Outages detectados: **76**
  - ≈190 veces mejor que el azar

---

## 🧠 Insights
- Los disturbios eléctricos (Sag, Disturbance) son fuertes predictores
- La variabilidad del voltaje es clave para anticipar fallas
- El voltaje promedio por sí solo no es suficiente

---

## 📁 Estructura del repositorio
smartgrid-outage-prediction/
│
├── data/
│   ├── raw/                # (vacío o instrucciones)
│   ├── interim/ 
│   ├── processed/          # parquet final (opcional)
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_interval_parsing.ipynb
│   ├── 03_pivot.ipynb
│   ├── 04_feature_engineering.ipynb
│   ├── 05_event_integration.ipynb
├── models/
│   ├── 06_modelo_SUPERVISADO_PRO.ipynb
│   ├── 07_advanced_features_xgboost.ipynb
│   ├── 08_model_comparison.ipynb
│
├── src/                    
│
├── reports/
│   ├── Proyecto_Outages_Presentacion.pptx
│
├── requirements.txt
├── README.md
└── .gitignore