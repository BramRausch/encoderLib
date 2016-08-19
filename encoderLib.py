import time
from machine import Pin

class encoder:
    currentTime = time.ticks_ms()
    loopTime    = currentTime
    encoder_clk_prev = False;
    i = 0

    def __init__(self, clk_pin, cs_pin):
        self.clk = Pin(clk_pin, Pin.IN)
        self.cs  = Pin(cs_pin, Pin.IN)
    
    def getValue(self):
        self.currentTime = time.ticks_ms()

        if self.currentTime >= (self.loopTime + 5):
            self.encoder_clk = self.clk.value()
            self.encoder_cs  = self.cs.value()

            if not self.encoder_clk and self.encoder_clk_prev:
                if self.encoder_cs:
                    self.i+=1
                else:
                    self.i-=1

            self.encoder_clk_prev = self.encoder_clk    
            self.loopTime         = self.currentTime
        return(self.i)
        