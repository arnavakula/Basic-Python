import socket

host = '10.0.0.10'
port = 5005

s = socket.socket()
s.connect((host, port))

file_name = input("Enter a file name: ")

s.send(file_name.encode())

content = s.recv(1024)
print(content.decode())

s.close()