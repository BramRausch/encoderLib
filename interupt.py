from machine import disable_irq
from machine import enable_irq
from machine import Pin


class encoder:
    # Init variables
    encoder_clk_prev = False
    i = 0

    def __init__(self, clk_pin, dt_pin):
        # Configure the rotary encoder pins and interupt
        self.clk = Pin(clk_pin, Pin.IN, Pin.PULL_UP)
        self.dt = Pin(dt_pin, Pin.IN, Pin.PULL_UP)

        self.clk.irq(
            trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING,
            handler=self.update
        )

        self.dt.irq(
            trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING,
            handler=self.update
        )

    def getValue(self):
        disable_irq()
        return(self.i)  # Return rotary encoder value
        enable_irq()

    # Non blocking delay of 5ms
    def update(self, p):
        disable_irq()
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
        print(self.i)
        enable_irq()
