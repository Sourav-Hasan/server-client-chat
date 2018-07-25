import socket


def Main():
    host = "127.0.0.1"
    port = 5000

    mySocket = socket.socket()
    mySocket.connect((host, port))
    while True:
        message = input(" -> ")
        if message=='':
            print("You should must need msg")
            continue
        else:
            break


    while message != 'shut':
        mySocket.send(message.encode())
        print("Message sent to server")
        while True:
            message = input(" -> ")
            if message == '':
                print("You should must need msg")
                continue
            else:
                break

    mySocket.close()


if __name__ == '__main__':
    Main()