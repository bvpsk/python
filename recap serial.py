import serial
ard = serial.Serial( "/dev/cu.wchusbserial1410" , 9600)
b = []
ff  = open('test.txt','a')
for i in range(100):
    try:
        a = int(ard.readline())
        b.append(a)
    except ValueError:
        pass
ff.write(str(b))
ff.close()
