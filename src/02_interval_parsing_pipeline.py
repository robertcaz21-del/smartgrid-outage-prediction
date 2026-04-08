# ==========================================
# 02_interval_parsing_pipeline.ipynb
# Parsing correcto de Interval Data (AMI)
# ==========================================

import pandas as pd
import numpy as np
import re
from pathlib import Path

# ------------------------------------------
# 1. CONFIGURACIÓN DE RUTA
# ------------------------------------------
base_path = Path(r"C:/Users/rroman/OneDrive - Empresa Eléctrica de Guatemala, S.A. (EEGSA)/Documents/Unidad/2026/Capacitación/Data Science y Machine Learning/proyecto final/data")

input_path = base_path / "interim" / "df_final.parquet"   # Ajustar si es necesario
output_path = base_path / "processed"
output_path.mkdir(parents=True, exist_ok=True)

# ------------------------------------------
# 2. CARGAR DATA
# ------------------------------------------
df = pd.read_parquet(input_path)

# Asegurar formato datetime correcto
df["FirstIntervalDateTime"] = pd.to_datetime(
    df["FirstIntervalDateTime"],
    format="%m%d%Y%I%M%S%p"
)

# ------------------------------------------
# 3. FUNCIÓN DE PARSING CORRECTO
# ------------------------------------------

def parse_row(row):
    data = row["Data"]
    start = row["FirstIntervalDateTime"]
    interval = int(row["Interval"])

    # separar intervalos correctamente
    tokens = re.findall(r'~([A-Z]?)(\d*\.?\d*)', data)

    registros = []
    current_time = start

    for flag, value in tokens:
        if value == "":
            val = np.nan
        else:
            val = float(value)

        registros.append([
            row["Meter ID"],
            current_time,
            row["Units"],
            flag,
            val
        ])

        current_time += pd.Timedelta(minutes=interval)

    return registros

# ------------------------------------------
# 4. APLICAR PARSING
# ------------------------------------------
records = []

for i, row in df.iterrows():
    if i % 1000 == 0:
        print(f"Procesando fila {i}")
    records.extend(parse_row(row))


df_intervals = pd.DataFrame(records, columns=[
    "Meter ID", "Datetime", "Units", "Flag", "Value"
])

# ------------------------------------------
# 5. CALIDAD DE DATOS
# ------------------------------------------
df_intervals["Quality"] = df_intervals["Flag"].replace({
    "": "valid",
    "E": "estimated",
    "A": "adjusted",
    "R": "raw",
    "N": "missing"
})

# ------------------------------------------
# 6. FILTRAR MISSING REALES
# ------------------------------------------
df_intervals = df_intervals[df_intervals["Quality"] != "missing"]

# ------------------------------------------
# 7. PIVOT A FORMATO FINAL
# ------------------------------------------
df_dataset = df_intervals.pivot_table(
    index=["Meter ID", "Datetime"],
    columns="Units",
    values="Value",
    aggfunc="first"
).reset_index()

# ------------------------------------------
# 8. CONVERSIÓN DE TIPOS
# ------------------------------------------
for col in df_dataset.columns:
    if col not in ["Meter ID", "Datetime"]:
        df_dataset[col] = pd.to_numeric(df_dataset[col], errors="coerce")

# ------------------------------------------
# 9. GUARDAR PARQUET
# ------------------------------------------
output_file = output_path / "dataset_medidores.parquet"

df_dataset.to_parquet(output_file, engine="fastparquet", index=False)

print("Dataset guardado en:", output_file)

# ------------------------------------------
# 10. VALIDACIONES
# ------------------------------------------
print(df_dataset.shape)
print(df_dataset.head())

# Distribución de calidad
print(df_intervals["Quality"].value_counts(normalize=True))
