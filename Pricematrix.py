import pandas_datareader.data as web 
import pandas as pd
import numpy as np
import Openmarket
import time
import datetime
import urllib
import urlparse
import string

class PriceMatrix():

    def __init__(self):
        
        df1=pd.read_csv('S&P500index.csv')
        stocks = df1.iloc[:, 0].tolist()

        dates = pd.date_range('19900101',periods=9700)
        dates_st = [None]*len(dates)
        
        for j in range (len(dates)):
                dates_st[j] = dates[j].strftime('%Y-%m-%d')
        
        df2 = pd.DataFrame(0, index=stocks, columns=dates_st)

        ts = [None]*len(dates)
        ds = [None]*len(dates)
        ms = [None]*len(dates)
        ys = [None]*len(dates)
        

        
        for i in range(len(stocks)):
            for j in range (len(dates_st)):
                ts[j] = time.strptime(dates_st[j], '%Y-%m-%d')
                ys[j],ms[j],ds[j] = ts[j][0:3]
                ms[j] = ms[j]-1
        
                url = "http://ichart.finance.yahoo.com/table.csv?g=d&f=2014&e=12&c=2014&b=10&a=7&d=7&s=AAPL"
                bits = list(urlparse.urlparse(url))
                qs = urlparse.parse_qs(bits[4])
                qs['c'] = qs['f'] = ys[j]
                qs['a'] = qs['d'] = ms[j]
                qs['b'] = qs['e'] = ds[j]
                qs['s'] = stocks[i]
                bits[4] = urllib.urlencode(qs, True)

                if ((urllib.urlopen(urlparse.urlunparse(bits)).read().find('Not')) > 0):
                    df2.iloc[i,j] = 0
                else:
                    df2.iloc[i,j] = web.DataReader(stocks[i], 'yahoo', dates_st[j] , dates_st[j]).Close[dates_st[j]]



        df2.to_csv('pricedata.csv')