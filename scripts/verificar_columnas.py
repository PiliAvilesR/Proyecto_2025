import os
import pandas as pd

# Carpeta donde están los archivos CSV
carpeta = "../data/DATOS/RUOA/Datos_hora/"  

# Obtener la lista de archivos CSV
archivos = [f for f in os.listdir(carpeta) if f.endswith(".csv")]

if not archivos:
    print("No se encontraron archivos CSV en la carpeta.")
    exit()

# Leer el primer archivo para tomarlo como referencia
referencia = pd.read_csv(os.path.join(carpeta, archivos[0]),skiprows=1)
columnas_referencia = set(referencia.columns)

print(f"Archivo de referencia: {archivos[0]}")
print(f"Columnas de referencia: {columnas_referencia}")

# Verificar los demás archivos
for archivo in archivos[1:]:
    df = pd.read_csv(os.path.join(carpeta, archivo))
    columnas_actual = set(df.columns)

    if columnas_actual != columnas_referencia:
        print(f"Diferencia en {archivo}")
        print(f"Columnas faltantes: {columnas_referencia - columnas_actual}")
        print(f"Columnas extra: {columnas_actual - columnas_referencia}")
    else:
        print(f"{archivo} tiene las mismas columnas.")

print("Verificación completada.")
