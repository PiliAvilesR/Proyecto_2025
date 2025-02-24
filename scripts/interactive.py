# %%

import pandas as pd 

f='../data/DATOS/RUOA/Datos_hora/2017-RUOA-HR.csv'

df=pd.read_csv(f,skiprows=[0,2,3],index_col=0,parse_dates=True,dayfirst=True)

columnas=df.columns


# %%

def veri_tipos(cols=columnas):
    for columna in cols:
        assert type(columna) is int,f'La {columna} no es entera'

    print('Todas las columnas pasaron la prueba')
# %%

veri_tipos(cols=columnas)
# %%
