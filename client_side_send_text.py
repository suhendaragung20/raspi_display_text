import socket
import threading
import sys


#Get host and port
host = "192.168.43.150"
port = 60000

#Attempt connection to server
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
except:
    print("Could not make a connection to the server")
    input("Press enter to quit")
    sys.exit(0)

#Send data to server
#str.encode is used to turn the string message into bytes so it can be sent across the network
while True:
    try:
        message = input()
        sock.sendall(str.encode(message))
    except:
        break