import pandas as pd
def eliminar_columnas_erroneas(df):
    df_sin_nulos = df.dropna(axis=1, how='any')
    return df_sin_nulos

