import serial
import time

print('start')

port  = "/dev/tty.HC-06-DevB"


bluetooth= serial.Serial(port,9600)

print("Connected")

bluetooth.flushInput()

for i  in range(5):
    print("Ping")
    bluetooth.write(b"BOOP" + str.encode(str(i))) #send a numerically incremented ping each time 
    input_data = bluetooth.readline()
    print(input_data.decode()) #these are bytes coming in so a decode is needed
    time.sleep(0.1)

bluetooth.close() #otherwise the connection will remain open until a timeout which ties up the /dev/thingamabob

print("Done")