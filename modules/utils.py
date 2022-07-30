import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

def trading_gap(df):
    m = pd.to_datetime(df['Date'])
    day =m.dt.day_name()
    df['Day'] = day
    gap = np.log(df['Open']/df['Close'].shift(1)).fillna(0)
    df['GAP'] = gap 
    max_day = df.loc[df['GAP'] >= 0].groupby(['Day']).size()
    valor = max_day.values == max_day.max()
    maxDay = max_day[valor].index[0]
    return maxDay

def trading_intra(df):
    m = pd.to_datetime(df['Date'])
    day =m.dt.day_name()
    df['Day'] = day
    gap = np.log(df['Open']/df['Close']).fillna(0)
    df['INTRA'] = gap 
    max_day = df.loc[df['INTRA'] > 0].groupby(['Day']).size()
    valor = max_day.values == max_day.max()
    maxDay = max_day[valor].index[0]
    return maxDay

def dataframe_export_gi(Tck,Day):
    new = pd.DataFrame()
    new['TICKER'] = Tck
    new['DAY'] = Day
    exportGi =new.groupby(['DAY']).size()
    return exportGi

def plot_gi(x,y, text:str):
    plt.figure(figsize=(10,4))
    plt.title(text)
    def addlabels(x,y):
        for i in range(len(x)):
            plt.text(i, y[i]//2, y[i], ha = 'center', fontsize=15, bbox=dict(color='black', alpha=0.7),color='white')
    addlabels(x, y)
    sns.barplot(x=x,y=y)
    return plt.show()

def roi_anual(lista, df):
    Roi = []
    Anual = []
    for m in lista:
        dfx =  df.loc[( df['Date']>= str(m) + '-01-01') & ( df['Date']<= str(m) + '-12-31' )]
        if dfx.shape[0] != 0:
            dfx.reset_index(inplace=True, drop=True)
            first = dfx.loc[0,['Adj Close']]
            last = dfx.loc[dfx.shape[0] - 1,['Adj Close']]
            rentabilidad_anual = ((last - first)/first )*100
            roi = round(float(rentabilidad_anual),2)
            Roi.append(roi)
            Anual.append(m)
    return Roi,Anual