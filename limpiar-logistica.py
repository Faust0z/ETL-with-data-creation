import pandas as pd
import numpy as np

df = pd.read_csv('data-logistica.csv')

df['id_pedido'] = df['id_pedido'].str.replace('ID-', '')
df['id_pedido'] = pd.to_numeric(df['id_pedido']).astype(int)

df['fecha_entrega'] = pd.to_datetime(df['fecha_entrega'], errors='coerce', dayfirst = True)

df['transportista'] = df['transportista'].astype('category')

df['status_envio'] = df['status_envio'].str.upper()
df['status_envio'] = df['status_envio'].astype('category')

df.to_csv('data-logistica-limpio.csv', index=False)