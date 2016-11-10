import time
import datetime
import urllib
import urlparse
import string

class Openmarket():
    
    def __init__(self, t1, stocks):
        self._tt = t1
        self._stock = stocks
    
    def judgeTime(self, t=0, y=0, m=0, d=0, m2=0, stock='AAPL', url = "http://ichart.finance.yahoo.com/table.csv?g=d&f=2014&e=12&c=2014&b=10&a=7&d=7&s=AAPL", bits=0, qs=0):    
        t = time.strptime(self._tt, '%Y-%m-%d') 
        stock = self._stock
        y,m,d = t[0:3]
        m2 = m - 1 
        url = "http://ichart.finance.yahoo.com/table.csv?g=d&f=2014&e=12&c=2014&b=10&a=7&d=7&s=AAPL"
        bits = list(urlparse.urlparse(url))
        qs = urlparse.parse_qs(bits[4])
        qs['c'] = qs['f'] = y
        qs['a'] = qs['d'] = m2
        qs['b'] = qs['e'] = d
        qs['s'] = stock
        bits[4] = urllib.urlencode(qs, True)
                
        if ((urllib.urlopen(urlparse.urlunparse(bits)).read().find('html')) > 0 or len(urllib.urlopen(urlparse.urlunparse(bits)).read()) < 43):
            return False
        else:
            return True


