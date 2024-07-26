import pandas as pd
import exploracionDx as exdx

df = pd.read_csv("Credit Card Clients.csv")

print(exdx.matriz_correlación(df))



