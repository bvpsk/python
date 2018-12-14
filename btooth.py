from time import sleep
import serial
ser = serial.Serial('/dev/cu.wchusbserial1420', 9600) # Establish the connection on a specific port
while True:
     data = input(print('enter:'))
     ser.write(data)# Convert the decimal number to ASCII then send it to the Arduino
     # Read the newest output from the Arduino
     sleep(.1) # Delay for one tenth of a second
