import pandas as pd

df_ven = pd.read_csv('data-ventas-limpio.csv')
df_log = pd.read_csv('data-logistica-limpio.csv')

df = pd.merge(df_ven, df_log, on = 'id_pedido', how = 'left')


df = df.dropna(subset=['fecha_entrega'])
df = df.query("status_envio == 'ENTREGADO'")

df['fecha'] = pd.to_datetime(df['fecha'])
df['fecha_entrega'] = pd.to_datetime(df['fecha_entrega'])
df['dias_demora'] = (df['fecha_entrega'] - df['fecha']).dt.days

df['cumple_sla'] = df['dias_demora'] <= 5
sla_report = df.groupby('transportista')['cumple_sla'].mean() * 100
print("\n--- % de Entregas a Tiempo (SLA <= 5 días) ---")
print(sla_report.round(3).astype(str) + '%')


tabla = df.pivot_table(
    index='transportista',
    columns='sucursal',
    values='dias_demora',
    aggfunc='mean'
)
print(f"Días promedio para cada transportista según la sucursal: \n {tabla}")

