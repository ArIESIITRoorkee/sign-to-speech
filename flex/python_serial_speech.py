from __future__ import print_function
from sklearn.externals import joblib
import numpy as np
import os


clf = joblib.load('mymodel.pkl')

def sanity_check(data):
    if len(data) != 9:
        return False
    possible = True
    for d in data:
        if d < 10:
            possible = False
    return possible

def printer(data):
    for d in data:
        print("%d " % (d), end ='')
    print()
def decodeSign(n):
    if n == 0:
        return ""
    if n < 10:
        return chr(64+n)
    return chr(65+n)

import serial
ser = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=1)

def say(text):
    command = "spd-say " + text
    os.system(command)

text = ""
while 1:
    try:
        arduinoData = ser.readline()
        if len(arduinoData) == 0:
            continue
        print(arduinoData)
        data = arduinoData.strip().split(" ")
        while '$' in data:
            data.remove('$')    
        data = map(int, data)
        # if not sanity_check(data):
        #     continue
        print(data)
        # data = np.array(data).reshape(1, -1)
        sign = clf.predict(data)
        print(sign)
        sign = decodeSign(sign)
        print(sign)
        if sign == "":
            say(text)
            text = ""
        else:
            text += sign
        # printer(data)
    except:
        pass