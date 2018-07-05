import utime
from machine import Pin

class Dmeasure():
    def __init__(self,trig,echo):
        self.trig = trig
        self.echo = echo
    def distance(self):
        trig1 = Pin(self.trig, Pin.OUT,Pin.PULL_UP)
        echo1 = Pin(self.echo, Pin.IN)
        trig1.value(0)
        start = 0
        end = 0
        echo1.value(0)
        while(echo.value()==0):
        trig.value(1)
        utime.sleep_us(100)
        trig.value(0)
        start = utime.ticks_us()
    
        while(echo.value()==1):
            end = utime.ticks_us()
       
        delta = end - start
        distance = delta/1000000*34299/2
        print('distance is:'+str(distance)+'cm')
        return distance