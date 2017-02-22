import pandas_datareader.data as web 
import pandas as pd
import numpy as np
import time
import datetime
import Openmarket 

class StockList():
    
    def __init__(self, selectiondate):
        df=pd.read_csv('S&P500index.csv')
        stocks = df['Symbol']
        #now_time = datetime.datetime.now()
        #y_time = now_time + datetime.timedelta(days=-1)
        #y_time_nyr = y_time.strftime('%Y-%m-%d')
        
        df1=web.DataReader(stocks, 'yahoo', selectiondate, selectiondate)
        df2 = df1['Volume'].T
        #volumes = df2[selectiondate]
        #s = df2.axes


        self._df = df2
        self._seleciondate = selectiondate

    def topNVolume(self, n = 5, order = False, minVolume = 0):
        if minVolume == 0:
            r = self._df.sort_values(by=self._seleciondate, ascending=False)[:n]
            if order:
                return r
            else:
                return r.sort_index()
        else:
            return self._df[self._df.volume >= minVolume]        