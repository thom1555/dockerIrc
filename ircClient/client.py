import socket

# take the server name and port name

host = '172.18.0.2'
port = 5000

# create a socket at client side
# using TCP / IP protocol
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect it to server and port
# number on local computer.
s.connect((host, port))

# receive message string from
# server, at a time 1024 B
msg = s.recv(1024)

# repeat as long as message
# string are not empty
while msg:
    print('Received:' + msg.decode())
    msg = s.recv(1024)

# disconnect the client
s.close()
