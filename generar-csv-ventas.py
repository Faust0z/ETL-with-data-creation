import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

### CSV Ventas

NUM_ROWS = 10000
PRODUCTOS = ['Matarazzo Spaghetti', 'Lucchetti Municiones', 'Gallo Oro', 'Exquisita Bizcochuelo', 'Granja del Sol Milanesas', 'Preferido Pan Rallado']
SUCURSALES = ['Norte', 'Oeste', 'CABA', 'Sur']

data = {
    'id_pedido': range(1000, 1000 + NUM_ROWS),
    'fecha': [datetime(2025, 1, 1) + timedelta(days=random.randint(0, 365)) for _ in range(NUM_ROWS)],
    'producto': [random.choice(PRODUCTOS) for _ in range(NUM_ROWS)],
    'sucursal': [random.choice(SUCURSALES) for _ in range(NUM_ROWS)],
    'cantidad': [random.randint(1, 50) for _ in range(NUM_ROWS)],
    'precio_unitario': [round(random.uniform(500.0, 4500.0), 2) for _ in range(NUM_ROWS)],
    'email_cliente': [f"cliente_{i}@gmail.com" for i in range(NUM_ROWS)]
}

df = pd.DataFrame(data)

df.loc[df.sample(frac=0.1).index, 'email_cliente'] = np.nan

df['cantidad'] = df['cantidad'].astype(object)
indices_error_cant = df.sample(frac=0.05).index
df.loc[indices_error_cant, 'cantidad'] = [random.choice(['Diez', 'ERROR', 's/d', 'consultar']) for _ in range(len(indices_error_cant))]

df.loc[df.sample(frac=0.03).index, 'fecha'] = pd.NaT

df['precio_unitario'] = df['precio_unitario'].astype(object)
indices_precio = df.sample(frac=0.1).index
df.loc[indices_precio, 'precio_unitario'] = df.loc[indices_precio, 'precio_unitario'].apply(lambda x: f"${x}")

duplicados = df.sample(n=200)
df = pd.concat([df, duplicados], ignore_index=True)

df.to_csv('data-ventas.csv', index=False)