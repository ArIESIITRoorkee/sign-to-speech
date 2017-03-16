import serial

ser = serial.Serial('/dev/ttyACM1', baudrate=9600, timeout=1)

while 1:
    arduinoData = ser.readline()
    if len(arduinoData) == 0:
        continue
    print("$ "+arduinoData)