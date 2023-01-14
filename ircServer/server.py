import socket

# take the server name and port name
#host = 'ircserver'
hostname = socket.gethostname()
host = socket.gethostbyname(hostname)
port = 5000

# create a socket at server side
# using TCP / IP protocol
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket with server
# and port number
s.bind(('', port))

# allow maximum 1 connection to
# the socket
s.listen(1)

while True:
    c, addr = s.accept()
    print("CONNECTION FROM:", str(addr))

    # send message
    c.send(b"Hello, there! :)")

    msg = "Bye.............."
    c.send(msg.encode())
    print("Stopping connection")

    # disconnect the server
    c.close()
