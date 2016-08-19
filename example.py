import encoderLib

last = 0
e = encoderLib.encoder(12, 13)
while True:
    value = e.getValue()
    if value != last:
        last = value
        print(value)