import pandas_datareader.data as web 
import pandas as pd
import numpy as np
import Openmarket
import time
import datetime

class PriceMatrix():

    def __init__(self):
        
        df1=pd.read_csv('S&P500index.csv')
        stocks = df1.iloc[:, 0].tolist()

        dates = pd.date_range('19700101',periods=17100)
        dates_st = [None]*len(dates)
        df2 = pd.DataFrame(0, index=stocks, columns=dates_st)
        for i in range(len(stocks)):
            for j in range (len(dates_st)):
                dates_st[j] = dates[j].strftime('%Y-%m-%d')
                if Openmarket.Openmarket(dates_st[j]).judgeWeekend(t=5) == False:
                    df2.iloc[i,j] = None
                else:
                    df2.iloc[i,j] = web.DataReader(stocks[i], 'yahoo', dates_st[j] , dates_st[j]).Close[dates_st[j]]



        df2.to_csv('pricedata.csv')