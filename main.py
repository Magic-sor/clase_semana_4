import pandas as pd
import exploracionDx as exdx
import tratamientoDx as ttdx

df = pd.read_csv("Credit Card Clients.csv")

#Tratamiento de datos
df_col_limpio = ttdx.eliminar_columnas_erroneas(df)
df_fil_limpio = ttdx.eliminas_filas_erroneas(df_col_limpio)

print(exdx.matriz_correlación(df_fil_limpio))