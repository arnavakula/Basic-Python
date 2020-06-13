import socket

host = '10.0.0.10'
port = 5005

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creating a server (socket object)
s.bind((host, port)) #setting conditions (in the form of a set)
print("Server listening on port:", port)
s.listen(1) #start listening on 1 connection(1 client)

c, addr = s.accept() #returns connection, address and accept client connection

file_name = c.recv(1024)

try:
    f = open(file_name, 'rb') #must send/receive in binary format
    content = f.read()
    c.send(content)
except FileNotFoundError:
    c.send(b'File does not exist')
finally:
    f.close()

c.close()
