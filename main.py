from modules.extraction import get_table, scraping_url
from modules.transformation import *
from modules.load import load_db

from database import db_connection
import modules.tables as tables


############################
# table sp500
############################
site = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
table = scraping_url(site)

scr_dict = {
    'ticker':0,
    'company':1,
    'sector':3,
    'industry':4
}

df_table = get_table(table, scr_dict)
df_sp = tables.get_sp500(df_table)
load_db(df_sp,db_connection(),'sp500')

############################
# table roi_anual
############################
diccionario = transform_dict()
lista = transform_list()
df_roi = tables.get_roiAnual(diccionario, lista)
load_db(df_roi,db_connection(),'roi_anual')

############################
# table gap
############################
Gap = transform_gap()
Dayg = transform_gapDay()
df_gap = tables.get_GAP(Gap,Dayg)
load_db(df_gap,db_connection(),'gap')

############################
# table intra
############################
Intra = transform_intra()
Dayi = transform_intraDay()
df_intra = tables.get_INTRA(Intra,Dayi)
load_db(df_intra,db_connection(),'intra')