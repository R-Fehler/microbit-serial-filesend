import serial
import os
import time

def writefile_to_microbit():
    print("starte übertragung")
    port="COM9"
    baud=9600
    ser=serial.Serial(port)
    ser.baudrate=baud
    f=open("katalog.txt","r")
    i=0
    j=0
    time.sleep(1)
    print(ser.read_all().decode('UTF-8'))
    while i<105:
        data = f.readline()
        print("Test from file:")
        print(data)
        string=data.encode('UTF-8')
        print("Test after encode")
        print(string)
        ser.write(string)
        print(ser.read_all().decode('UTF-8'))
        time.sleep(0.4)
        i=i+1

    while j<100:
        print(ser.read_all().decode('UTF-8'))
        time.sleep(0.1)

    print("ende")

writefile_to_microbit()