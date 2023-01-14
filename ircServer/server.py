import socket


def start_server():
    """Start listening for client connections"""
    #host = 'ircserver'
    hostname = socket.gethostname()
    host = socket.gethostbyname(hostname)
    port = 5000

    # Create a listening socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', port))
    s.listen(1)

    while True:
        # Accept connection
        c, addr = s.accept()
        print("CONNECTION FROM:", str(addr))

        # Send message
        c.send(b"Hello, there! :)")

        msg = "Bye.............."
        c.send(msg.encode())
        print("Stopping connection")

        # Disconnect the server
        c.close()

def server():
    print("Quien eres")
    answer = input("Enter your name: ")
    print("Hello, " + answer)


if __name__ == "__main__":
    start_server()
