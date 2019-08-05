import socket
import threading
import cv2



def main():
    # Get host and port
    host = "192.168.43.150"
    port = 60000

    # Create new server socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(5)

    sock_client, address_client = sock.accept()

    while True:
        frame = cv2.imread("screen.png")
        try:
            data = sock_client.recv(32)
        except:
            print("Client " + str(address_client) + " has disconnected")
            break
        if data != "":
            print(str(data.decode("utf-8")))
            cv2.imshow("text display", frame)


main()