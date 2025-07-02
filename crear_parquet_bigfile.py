import pandas as pd

# 1. lectura csv
df = pd.read_csv('ventas_grandes.csv')

# 2. mostramos primeras 5 filas
print("Primeras 5 filas del dataset:")
print(df.head())
print(f"\nTotal de filas leídas: {len(df)}")

# 3. guardar en parquet
df.to_parquet('ventas_grandes.parquet')
print("\nArchivo 'ventas_grandes.parquet' creado.")

# 4. lectura selectiva
print("\nLeyendo SOLO las columnas 'Producto', 'Precio_Unitario' y 'Ciudad' desde Parquet:")
columnas_deseadas = ['Producto', 'Precio_Unitario', 'Ciudad']
df_selectivo = pd.read_parquet('ventas_grandes.parquet', columns=columnas_deseadas)
print(df_selectivo.head())