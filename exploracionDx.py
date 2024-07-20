import pandas as pd

def matriz_correlación(df):
    df_number = df.select_dtypes(include=['number'])
    correlacion = df_number.corr()
    return correlacion
