import serial
ser=serial.Serial("/dev/cu.usbmodem1411", 9600)
while True:
    try:
        print(int(ser.readline()))
    except:
        pass
