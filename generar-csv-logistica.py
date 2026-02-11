import pandas as pd
import numpy as np
from datetime import timedelta

df = pd.read_csv('data-ventas-limpio.csv')
df['fecha'] = pd.to_datetime(df['fecha'])

cant = len(df)

opciones_transporte = ['Andreani', 'Ocasa', 'Correo Argentino', 'Moto']
transportistas = np.random.choice(opciones_transporte, size=cant, p=[0.3, 0.3, 0.2, 0.2])

dias_demora = np.zeros(cant, dtype=int)

mask_moto = (transportistas == 'Moto')
dias_demora[mask_moto] = np.random.randint(1, 4, size=mask_moto.sum())

mask_privados = (transportistas == 'Andreani') | (transportistas == 'Ocasa')
dias_demora[mask_privados] = np.random.randint(2, 7, size=mask_privados.sum())

mask_correo = (transportistas == 'Correo Argentino')
dias_demora[mask_correo] = np.random.randint(5, 16, size=mask_correo.sum())

mask_sur = (df['sucursal'] == 'Sur')
dias_demora[mask_sur] += np.random.randint(2, 5, size=mask_sur.sum())

mask_norte = (df['sucursal'] == 'Norte')
dias_demora[mask_norte] += np.random.randint(1, 3, size=mask_norte.sum())

mask_oeste = (df['sucursal'] == 'Oeste')
dias_demora[mask_oeste] += np.random.randint(0, 2, size=mask_oeste.sum())

df['fecha_entrega_dt'] = df['fecha'] + pd.to_timedelta(dias_demora, unit='D')

df_log = pd.DataFrame({
    'id_pedido': df['id_pedido'],
    'fecha_entrega': df['fecha_entrega_dt'].dt.strftime('%d/%m/%Y'),
    'transportista': transportistas,
    'status_envio': np.random.choice(['Entregado', 'en camino', 'devuelto', 'ENTREGADO'], size=cant)
})

df_log['id_pedido'] = df_log['id_pedido'].astype(object)

idx_float = df_log.sample(frac=0.05).index
df_log.loc[idx_float, 'id_pedido'] = df_log.loc[idx_float, 'id_pedido'].apply(lambda x: f"{float(x)}")

idx_prefix = df_log.sample(frac=0.05).index
df_log.loc[idx_prefix, 'id_pedido'] = df_log.loc[idx_prefix, 'id_pedido'].apply(lambda x: f"ID-{x}")

idx_space = df_log.sample(frac=0.05).index
df_log.loc[idx_space, 'id_pedido'] = df_log.loc[idx_space, 'id_pedido'].apply(lambda x: f"{x} ")

df_log.to_csv('data-logistica.csv', index=False)