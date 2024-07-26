import pandas as pd
import exploracionDx as exdx
import tratamientoDx as ttdx

df = pd.read_csv("Credit Card Clients.csv")

print(exdx.matriz_correlación(df))

print (ttdx.eliminar_columnas_erroneas(df))
