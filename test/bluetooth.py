import serial
import time

print('start')

# port  = "/dev/tty.HC-06-DevB"
port  = "COM5"


bluetooth= serial.Serial(port,9600)

print("Connected")

bluetooth.flushInput()

while True:
    print("Ping")
    bluetooth.write(bytearray(input(), "utf8")) #send a numerically incremented ping each time 
    
bluetooth.close() #otherwise the connection will remain open until a timeout which ties up the /dev/thingamabob

print("Done")