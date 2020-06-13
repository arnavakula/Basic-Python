import socket

host = '10.0.0.10'
port = 5005

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creating a server (socket object)
s.bind((host, port)) #setting conditions (in the form of a set)
print("Server listening on port:", port)
s.listen(1) #start listening on 1 connection(1 client)

c, addr = s.accept() #returns connection, address and accept client connection
print('Connection from: ' ,str(addr))

c.send(b"Hello client, how are you?") #communicate to client using binary

c.close()
