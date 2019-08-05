import socket
import threading
import cv2

# Variables for holding information about connections
connections = []
total_connections = 0


# Client class, new instance created for each connected client
# Each instance has the socket and address that is associated with items
# Along with an assigned ID and a name chosen by the client
class Client(threading.Thread):
    def __init__(self, socket, address, id, name, signal):
        threading.Thread.__init__(self)
        self.socket = socket
        self.address = address
        self.id = id
        self.name = name
        self.signal = signal

    def __str__(self):
        return str(self.id) + " " + str(self.address)

    # Attempt to get data from client
    # If unable to, assume client has disconnected and remove him from server data
    # If able to and we get data back, print it in the server and send it back to every
    # client aside from the client that has sent it
    # .decode is used to convert the byte data into a printable string
    def run(self):
        while self.signal:
            frame = cv2.imread("screen.png")
            try:
                data = self.socket.recv(32)
            except:
                print("Client " + str(self.address) + " has disconnected")
                self.signal = False
                connections.remove(self)
                break
            if data != "":
                print("ID " + str(self.id) + ": " + str(data.decode("utf-8")))
                for client in connections:
                    if client.id != self.id:
                        client.socket.sendall(data)
                cv2.imshow("text display", frame)


# Wait for new connections
def newConnections(socket):
    while True:
        sock, address = socket.accept()
        global total_connections
        connections.append(Client(sock, address, total_connections, "Name", True))
        connections[len(connections) - 1].start()
        print("New connection at ID " + str(connections[len(connections) - 1]))
        total_connections += 1


def main():
    # Get host and port
    host = "192.168.43.150"
    port = 60000

    frame = cv2.imread("screen.png")
    cv2.namedWindow("Frame", cv2.WINDOW_KEEPRATIO)

    cv2.namedWindow("Frame", cv2.WINDOW_KEEPRATIO)
    cv2.setWindowProperty("Frame", cv2.WND_PROP_ASPECT_RATIO, cv2.WINDOW_KEEPRATIO)
    cv2.setWindowProperty("Frame", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    # show the output frame
    cv2.imshow("Frame", frame)

    print("Display Screen")

    # Create new server socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(5)

    # Create new thread to wait for connections
    newConnectionsThread = threading.Thread(target=newConnections, args=(sock,))
    newConnectionsThread.start()


main()