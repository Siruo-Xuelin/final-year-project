import time
import datetime

class Openmarket():
    
    def __init__(self, t1):
        self._tt = t1
        
    
    def judgeWeekend(self,t):    
        t = time.strptime(self._tt, '%Y-%m-%d') 
        y,m,d = t[0:3]
        a = datetime.datetime.weekday(datetime.datetime(y,m,d))
        if (a+1>5):
            return False
        else:
            return a   
