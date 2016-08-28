from machine import disable_irq
from machine import enable_irq
from machine import Pin
import time


lastEncoded = 0
encoderValue = 0

lastencoderValue = 0

lastMSB = 0
lastLSB = 0

clk_pin = 12
dt_pin = 13

clk = Pin(clk_pin, Pin.IN, Pin.PULL_UP)
dt = Pin(dt_pin, Pin.IN, Pin.PULL_UP)

def update(p):
    disable_irq()
    MSB = clk.value()
    LSB = dt.value()

    encoded = (MSB << 1) | LSB
    sum = (lastEncoded << 2) | encoded

    if sum == 0b1101 or sum == 0b0100 or sum == 0b0010 or sum == 0b1011:
        encoderValue += 1
    
    if sum == 0b1110 or sum == 0b0111 or sum == 0b0001 or sum == 0b1000:
        encoderValue -= 1

    lastEncoded = encoded
    enable_irq()

clk.irq(
    trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING,
    handler=update
)

dt.irq(
    trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING,
    handler=update
)
while True:
    time.sleep(0.5)
    print(encoderValue)