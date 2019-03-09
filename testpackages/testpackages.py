import serial
import os
import sys

def main():
    print("start")
    port="COM9"
    baud=115200
    ser=serial.Serial(port)
    ser.baudrate=baud
    f=open("log.txt","w+")
    i=0
    while i<1000:
        data = ser.readline()

        string=data.decode('UTF-8')
        print(string)
        f.write(string)
        i=i+1

    print("ende")

main()