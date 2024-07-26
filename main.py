import pandas as pd
import tratamientoDx as ttdx

df = pd.read_csv("Credit Card Clients.csv")

print (ttdx.eliminar_columnas_erroneas(df))
