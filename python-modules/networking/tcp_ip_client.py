import socket

host = '10.0.0.10'
port = 5005

s = socket.socket()
s.connect((host, port))

msg = s.recv(1024) #receive param bytes at a time

while msg: 
    print("Message: ", msg.decode())
    msg = s.recv(1024)

s.close()