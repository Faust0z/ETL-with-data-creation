import pandas as pd
import numpy as np

df = pd.read_csv('data-ventas.csv')

df['fecha'] = pd.to_datetime(df['fecha'], errors='coerce')
df = df.dropna(subset=['fecha'])

# Hay variables con valores "consultar", "Diez", "ERROR" y "s/d"
df['cantidad'] = df['cantidad'].replace('Diez', "10")
df['cantidad'] = pd.to_numeric(df['cantidad'], errors='coerce')
df = df.dropna(subset=['cantidad'])

# Algunos precios unitarios tienen un símbolo "$" al principio
df['precio_unitario'] = df['precio_unitario'].astype(str).str.replace('$', '')
df['precio_unitario'] = pd.to_numeric(df['precio_unitario'], errors='coerce').astype(int)

df['email_cliente'] = df['email_cliente'].fillna("Sin correo")

df = df.drop_duplicates()

df['sucursal'] = df['sucursal'].astype('category')
df['producto'] = df['producto'].astype('category')

df.to_csv('data-ventas-limpio.csv', index=False)