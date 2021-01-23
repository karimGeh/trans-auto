import serial
import time

ser = serial.Serial("COM5", 9600) #Change your port name COM... and your baudrate
# print(str(ser))
# start = str(ser).index('=')
# finish = str(ser).index(',')
# DeviceId = str(ser)[start + 1:finish]
# print(DeviceId)
print('connected')
# ser.write(bytearray(" B", "utf8"))
# def retrieveData(data):
#     if " ".join(data) == "58 238 102 26":
#         print("A")
#         ser.write(bytearray("S", "utf8"))
#     elif " ".join(data) == "69 187 172 32":
#         print("L")
#         ser.write(bytearray("L", "utf|8"))

while(True):
    time.sleep(1)
    print("Ping")
    if ser.in_waiting:
        print(str(ser.readline().decode('ascii')))
    else:
        ser.write(bytearray(str("A"), "utf8"))
    # data = str(ser.readline().decode('ascii'))
    # if data :
    #     print(data.split())
    #     print(type(data))
    #     retrieveData(data.split())
    