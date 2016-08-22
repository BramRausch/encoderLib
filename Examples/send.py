import encoderLib
import socket

UDP_IP = "192.168.1.114"
UDP_PORT = 5005
MESSAGE = "Hello, World!"

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

last = 0
var = 0
e = encoderLib.encoder(12, 13)

while True:
    value = e.getValue()
    if value < last:
        last = value
        if var > 0:
            var-=1
        sock.sendto(str(var), (UDP_IP, UDP_PORT))
    elif value > last:
        last = value
        if var < 255:
            var += 1
        sock.sendto(str(var), (UDP_IP, UDP_PORT))