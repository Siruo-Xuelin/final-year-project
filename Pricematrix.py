import pandas_datareader.data as web 
import pandas as pd


class PriceMatrix():

    def __init__(self, start, end):
        
        df1=pd.read_csv('S&P500index.csv')
        stocks = df1['Symbol']
        df2=web.DataReader(stocks, 'yahoo', start,end)
        df3=df2['Adj Close'].T
        df3.to_csv('pricedata.csv')