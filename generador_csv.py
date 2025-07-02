import csv
import random
from datetime import datetime, timedelta

NUMERO_DE_FILAS = 1000000
NOMBRE_ARCHIVO = 'ventas_grandes.csv'

productos = [
    {'id': 'PROD_001', 'nombre': 'Laptop Pro X1', 'categoria': 'Electronica', 'precio_base': 1200.50},
    {'id': 'PROD_002', 'nombre': 'Mouse Inalambrico', 'categoria': 'Electronica', 'precio_base': 25.00},
    {'id': 'PROD_003', 'nombre': 'Teclado Mecanico', 'categoria': 'Electronica', 'precio_base': 75.75},
    {'id': 'PROD_004', 'nombre': 'El Secreto del Cosmos', 'categoria': 'Libros', 'precio_base': 15.99},
    {'id': 'PROD_005', 'nombre': 'Guia del Programador', 'categoria': 'Libros', 'precio_base': 29.95},
    {'id': 'PROD_006', 'nombre': 'Taza de Cafe Geek', 'categoria': 'Hogar', 'precio_base': 8.50},
    {'id': 'PROD_007', 'nombre': 'Silla Ergonomica', 'categoria': 'Oficina', 'precio_base': 150.00},
    {'id': 'PROD_008', 'nombre': 'Monitor 4K', 'categoria': 'Electronica', 'precio_base': 350.80},
    {'id': 'PROD_009', 'nombre': 'Botella de Agua', 'categoria': 'Deportes', 'precio_base': 12.00},
    {'id': 'PROD_010', 'nombre': 'Mochila para Laptop', 'categoria': 'Accesorios', 'precio_base': 45.50}
]

ciudades = ['Madrid', 'Barcelona', 'Valencia', 'Sevilla', 'Zaragoza', 'Bilbao']
metodos_pago = ['Tarjeta de Credito', 'PayPal', 'Transferencia Bancaria', 'Bizum']

def generar_fila(id_venta):
    producto_elegido = random.choice(productos)
    cantidad = random.randint(1, 5)
    
    precio_final = round(producto_elegido['precio_base'] * (1 + random.uniform(-0.05, 0.05)), 2)
    
    total_venta = round(precio_final * cantidad, 2)
    
    fecha_venta = datetime.now() - timedelta(days=random.randint(0, 365), hours=random.randint(0, 23))
    
    return [
        id_venta,
        producto_elegido['id'],
        producto_elegido['nombre'],
        producto_elegido['categoria'],
        precio_final,
        cantidad,
        total_venta,
        fecha_venta.strftime('%Y-%m-%d %H:%M:%S'),
        random.choice(ciudades),
        random.choice(metodos_pago)
    ]

columnas = [
    'ID_Venta', 'ID_Producto', 'Producto', 'Categoria', 
    'Precio_Unitario', 'Cantidad', 'Total_Venta', 'Fecha_Venta', 
    'Ciudad', 'Metodo_Pago'
]

try:
    with open(NOMBRE_ARCHIVO, 'w', newline='', encoding='utf-8') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        
        escritor_csv.writerow(columnas)
        
        for i in range(1, NUMERO_DE_FILAS + 1):
            fila_datos = generar_fila(10000 + i) # Empezar IDs de venta desde 10001
            escritor_csv.writerow(fila_datos)
            
    print(f"Archivo '{NOMBRE_ARCHIVO}' con {NUMERO_DE_FILAS} filas generado con éxito.")

except Exception as e:
    print(f"Ocurrió un error al generar el archivo: {e}")