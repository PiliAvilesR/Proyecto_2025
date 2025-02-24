# %%%



import pandas as pd
import missingno as msno

def valores_nulos(df):
    cantidad=df.isnull().sum()
    return cantidad, msno.bar(df)


f='../data/DATOS/RUOA/Datos_hora/2017-RUOA-HR.csv'
ruoa=pd.read_csv(f,skiprows=[0,2,3],index_col=0,parse_dates=True,dayfirst=True)

valores_nulos(ruoa)
# %%
