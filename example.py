import encoderLib

last = 0
e = encoderLib.encoder(12, 13) # Initializes the library with pin CLK on 12 and pin DT on 13

while True:                    # Infinite loop
    value = e.getValue()         # Get rotary encoder value
    if value != last:            # If there is a new value do
        last = value
        print(value)               # In this case it prints the value
