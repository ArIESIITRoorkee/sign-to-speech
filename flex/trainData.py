from __future__ import print_function
from sklearn import preprocessing


def printer(data, sign=''):
    for d in data:
        print("%d " % (d), end ='')
    print(sign)

import serial
ser = serial.Serial('/dev/ttyACM1', baudrate=9600, timeout=1)



while 1:
    sign = 24
    sign = str(sign)
    arduinoData = ser.readline()
    if len(arduinoData) == 0:
        continue
    # print(arduinoData)
    data = arduinoData.strip().split(" ")
    while '$' in data:
        data.remove('$')
    if len(data) < 9:
        continue
    possible = True
    for d in data:
        if d < 10:
            possible = False
    if not possible:
        continue
    data.append(sign)
    with open("signdata.txt", "a+") as f:
        f.write(" ".join(data)) 
        f.write("\n")   
    data = map(int, data)
    printer(data)


