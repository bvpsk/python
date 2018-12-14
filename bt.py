import socket
serverMACAddress = '98:D3:35:00:C8:3F'
port = 9600
s=socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM,socket.BTPROTO_RFCOMM)
s.connect((serverMACAddress,port))
while 1:
    text = input(print('enter a or d:'))
    if text == "quit":
        break
    s.send(bytes(text, 'UTF-8'))
s.close()
