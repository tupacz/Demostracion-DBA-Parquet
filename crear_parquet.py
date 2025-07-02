import pandas as pd

df = pd.read_csv('ventas.csv')

print("Datos leídos del CSV:")
print(df)
print("\n")

df.to_parquet('ventas.parquet')

print("¡Archivo 'ventas.parquet' creado con éxito!")

# 4. lectura selectiva
print("Leyendo SOLO las columnas 'Producto' y 'Precio' desde el archivo Parquet:")
columnas_deseadas = ['Producto', 'Precio']
df_parquet_selectivo = pd.read_parquet('ventas.parquet', columns=columnas_deseadas)

print(df_parquet_selectivo)