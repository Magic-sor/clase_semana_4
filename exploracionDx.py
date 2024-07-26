import pandas as pd
import seaborn as sns

def matriz_correlación(df):
    df_number = df.select_dtypes(include=['number'])
    correlacion = df_number.corr()
    return correlacion

def create_pairplot(df):
    df_number = df.select_dtypes(include=['number'])
    return(sns.pairplot(df_number))
    
