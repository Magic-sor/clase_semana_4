import pandas as pd
import exploracionDx as exdx
import tratamientoDx as ttdx
import matplotlib.pyplot as plt

df = pd.read_csv("Credit Card Clients.csv")

print (ttdx.eliminar_columnas_erroneas(df))
print(exdx.matriz_correlación(df))
exdx.create_pairplot(df)
plt.show()