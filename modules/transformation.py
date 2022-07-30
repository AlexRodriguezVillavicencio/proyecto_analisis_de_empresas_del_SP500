import numpy as np
from extraction import get_data

from utils import roi_anual
from utils import trading_gap, trading_intra


roi_dict = {}
roi_list = []
gap = []
gap_day = []
intra = []
intra_day = []

ticker_prueba = ['MMM','ABBV','ABMD']

for tck in ticker_prueba:
    df = get_data(tck)
    if df.shape[0] != 0:
        df.reset_index(inplace=True)

        # table roi_anual
        roi_list = np.arange(2000,2022)
        roi = roi_anual(roi_list,df)
        roi_dict[tck] = roi[0]

        # table gap
        max_gap_day = trading_gap(df)
        gap.append(tck)
        gap_day.append(max_gap_day)

        # table intra
        max_intra_day = trading_intra(df)
        intra.append(tck)
        intra_day.append(max_intra_day)

def transform_dict():
    return roi_dict

def transform_list():
    return roi_list

def transform_gap():
    return gap

def transform_gapDay():
    return gap_day

def transform_intra():
    return intra

def transform_intraDay():
    return intra_day