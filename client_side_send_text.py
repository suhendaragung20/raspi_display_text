import socket
import threading
import sys
import time


#Get host and port
host = "10.14.3.249"
port = 60000

interval_send = 0.2
last_send = time.time()

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
        message = "None"
        try:
            with open('raspi_display_text/get_name_detected.txt', 'r') as file:
                data = file.read().replace('\n', '')
                message = str(data)
        except KeyboardInterrupt:
            break
        except:
            continue

        if time.time() - last_send >= interval_send:
            sock.sendall(str.encode(message))
            last_send = time.time()
    except:
        break