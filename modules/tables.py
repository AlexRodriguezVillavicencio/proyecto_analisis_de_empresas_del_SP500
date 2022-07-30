import pandas as pd
from modules.utils import dataframe_export_gi

def get_roiAnual(roi_dict:dict, roi_list:list):    
    key = list(roi_dict.keys())
    value = list(roi_dict.values())
    for i in range(len(key)):
        nuevo = [0]*(22 - len(value[i]))
        roi_dict[key[i]] = nuevo + value[i]

    dfp = pd.DataFrame(roi_dict, columns=key)
    dfp['AÑO'] = roi_list
    first_column = dfp.pop('AÑO')
    dfp.insert(0, 'AÑO', first_column)
    dft = dfp.transpose()
    dft.reset_index(inplace=True)
    dft.rename(columns={'index': 'TICKER', 0: '2000', 1: '2001', 2: '2002', 3: '2003', 4: '2004',
                        5: '2005', 6: '2006', 7: '2007', 8: '2008', 9: '2009', 10: '2010', 11: '2011',
                        12: '2012', 13: '2013', 14: '2014', 15: '2015', 16: '2016', 17: '2017', 18: '2018',
                        19: '2019', 20: '2020', 21: '2021'}, inplace=True)
    dft.drop(dft.index[0], inplace=True)
    return dft


def get_sp500(df_table):
    df = pd.DataFrame()
    for key, value in df_table.items():
        df[key.upper()] = value
    return df

def get_GAP(Gap,Dayg):
    exportGi = dataframe_export_gi(Gap,Dayg)
    df_gap = pd.DataFrame()
    df_gap['SEMANA'] = exportGi.index
    df_gap['NGAP'] = exportGi.values
    return df_gap

def get_INTRA(Intra,Dayi):
    exportIn = dataframe_export_gi(Intra,Dayi)
    df_intra = pd.DataFrame()
    df_intra['SEMANA'] = exportIn.index
    df_intra['NINTRA'] = exportIn.values