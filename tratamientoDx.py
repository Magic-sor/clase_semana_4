import pandas as pd

def eliminar_columnas_erroneas(df):
    df_sin_nulos = df.dropna(axis=1, how='any')
    return df_sin_nulos

def eliminar_filas_erroneas(df):
    df_sin_nulos = df.dropna()
    return df_sin_nulos


