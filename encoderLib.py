import time
from machine import Pin


class encoder:
    # Init variables
    currentTime = time.ticks_ms()  # Get current tick count
    loopTime = currentTime
    encoder_clk_prev = False
    i = 0

    def __init__(self, clk_pin, dt_pin):
        # Configure the rotary encoder pins
        self.clk = Pin(clk_pin, Pin.IN)
        self.dt = Pin(dt_pin, Pin.IN)

    def getValue(self):
        self.currentTime = time.ticks_ms()  # Get new tick count

        # Non blocking delay of 5ms
        if self.currentTime >= (self.loopTime + 5):
            # Read the rotary encoder pins
            self.encoder_clk = self.clk.value()
            self.encoder_dt = self.dt.value()

            # If rotary encoder rotated
            if not self.encoder_clk and self.encoder_clk_prev:
                # Get direction of rotation
                if self.encoder_dt:
                    self.i += 1
                else:
                    self.i -= 1

            self.encoder_clk_prev = self.encoder_clk
            self.loopTime = self.currentTime
        return(self.i)  # Return rotary encoder value
