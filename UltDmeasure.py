import utime
from machine import Pin

class Dmeasure():
    def __init__(self,trig,echo):
        self.trig = trig
        self.echo = echo
        self.d = 0
    def measure(self):
        trig1 = Pin(self.trig, Pin.OUT)
        echo1 = Pin(self.echo, Pin.IN)
        trig1.value(0)
        start = 0
        end = 0
        echo1.value(0)
        while(echo1.value()==0):
            trig1.value(1)
            utime.sleep_us(100)
            trig1.value(0)
            start = utime.ticks_us()
    
        while(echo1.value()==1):
            end = utime.ticks_us()
       
        delta = end - start
        self.d = delta/1000000*34299/2
        
    def distance(self):
        return self.d
        
'''调用该模块例子
import UltDmeasure
a = UltDmeasure.Dmeasure(14,12)  #初始化端口，trig=14,echo=12
a.measure()      #测量
d = a.distance()     #返回测量距离
print('distance is:'+str(d)+'cm')   #显示