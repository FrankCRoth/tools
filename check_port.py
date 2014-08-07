import socket
import sys

def connect(name, port=22):
    s = socket.socket()
    try:
        s.connect((name, port))
    except Exception, e:
        print("Can't connect: %s" % e)
        sys.exit(1)
    print("Connected")

if __name__ == "__main__":
    name = raw_input("Hostname > ")
    port = int(raw_input("Port >"))
    connect(name,port)
