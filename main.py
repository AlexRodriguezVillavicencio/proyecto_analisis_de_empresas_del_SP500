import pandas as pd
import numpy as np

from utils import roi_anual, scraping_url, scraping_column
from utils import retorno_gap, retorno_intra, descarga_datos
from utils import dataframe_export_gi

from sqlalchemy import create_engine
from configparser import ConfigParser


site = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
table = scraping_url(site)

#column "TICKER"
ticker = scraping_column(table,0)
#column "COMPANY"
company = scraping_column(table,1)
#column "SECTOR"
sector = scraping_column(table,3)
#column "INDUSTRY"
industry = scraping_column(table,4)


############################
# connection MySQL
############################
file = 'config.ini'
config = ConfigParser()
config.read(file)

USER_BASE = config['database']['user']
PASSWORD_BASE = config['database']['passw']
DATABASE = config['database']['db']
PORT = config['database']['port']
HOST = config['database']['host']

create_connection = f'postgresql+psycopg2://{USER_BASE}:{PASSWORD_BASE}@{HOST}:{PORT}/{DATABASE}'
connection = create_engine(create_connection)

############################
# table roi_anual
############################
diccionario = {}
for tck in ticker:
    df = descarga_datos(tck)
    if df.shape[0] != 0:
        df.reset_index(inplace=True)
        lista = np.arange(2000,2022)
        roi = roi_anual(lista,df)
        diccionario[tck] = roi[0]

clave = list(diccionario.keys())
valor = list(diccionario.values())
for i in range(len(clave)):
    nuevo = [0]*(22 - len(valor[i]))
    diccionario[clave[i]] = nuevo + valor[i]

dfp = pd.DataFrame(diccionario, columns= clave)
dfp['AÑO'] = lista
first_column = dfp.pop('AÑO')
dfp.insert(0,'AÑO',first_column)
dft = dfp.transpose()
dft.reset_index(inplace=True)
dft.rename(columns={'index':'TICKER',0:'2000',1:'2001',2:'2002',3:'2003',4:'2004',
                    5:'2005',6:'2006',7:'2007',8:'2008',9:'2009',10:'2010',11:'2011',
                    12:'2012',13:'2013',14:'2014',15:'2015',16:'2016',17:'2017',18:'2018',
                    19:'2019',20:'2020',21:'2021'}, inplace=True)
dft.drop(dft.index[0],inplace=True)

try:
    dft.to_sql(name='roi_anual',con=connection, index=False)
except:
    print("la tabla ya existe")


############################
# table sp500
############################
df_SP = pd.DataFrame()
df_SP['TICKER'] = ticker
df_SP['COMPANY'] = company
df_SP['SECTOR'] = sector
df_SP['INDUSTRY'] = industry

try:
    df_SP.to_sql(name='sp500',con=connection, index=False)
except:
    print("la tabla ya existe")


############################
# table gap
############################
Gap = []
Dayg = []
for tck in ticker:
    df = descarga_datos(tck)
    if df.shape[0] != 0:
        df.reset_index(inplace=True)
        max_dayg = retorno_gap(df)
        Gap.append(tck)
        Dayg.append(max_dayg)

exportGi = dataframe_export_gi(Gap,Dayg)
df_gap = pd.DataFrame()
df_gap['SEMANA'] = exportGi.index
df_gap['NGAP'] = exportGi.values

try:
    df_gap.to_sql(name='gap',con=connection, index=False)
except:
    print("la tabla ya existe")


############################
# table intra
############################
Intra = []
Dayi = []
for intra in ticker:
    df = descarga_datos(intra)
    if df.shape[0] != 0:
        df.reset_index(inplace=True)
        max_dayi = retorno_intra(df)
        Intra.append(intra)
        Dayi.append(max_dayi)

exportIn = dataframe_export_gi(Intra,Dayi)
df_intra = pd.DataFrame()
df_intra['SEMANA'] = exportIn.index
df_intra['NINTRA'] = exportIn.values

try:
    df_intra.to_sql(name='intra',con=connection, index=False)
except:
    print("la tabla ya existe")