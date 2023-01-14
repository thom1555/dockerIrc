import socket


def connect_to_server():
    """Connect to server"""
    #host = '172.18.0.2'
    host = '127.0.0.1'
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

if __name__ == "__main__":
    connect_to_server()
