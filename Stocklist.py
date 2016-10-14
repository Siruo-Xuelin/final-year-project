import ystockquote
import pandas as pd
import numpy as np

class StockList():
    
    def __init__(self):
        stocks=[None]*504
        volumes=[None]*504
        df=pd.read_csv('S&P500index.csv')
        
        for i in range(len(stocks)):
            stocks[i] = df.iloc[i,0]
            volumes[i] = ystockquote.get_volume(stocks[i])
            
        
        self._df = pd.DataFrame({'stocks': stocks, 'volume':volumes})
        self,_df = self._df.set_index('stock')
        

    def topNVolume(self, n = 5, order = False, minVolume = 0):
        if minVolume == 0:
            r = self._df.sort_values(by='volume', ascending=False)[:n]
            if order:
                return r
            else:
                return r.sort_index()
        else:
            return self._df[self._df.volume >= minVolume]        