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

    print("Connected with " + str(address_client))

    text_display = ""

    while True:
        frame = cv2.imread("screen.png")

        key = cv2.waitKey(1) & 0xFF

        try:
            data = sock_client.recv(32)
        except:
            print("Client " + str(address_client) + " has disconnected")
            break
        if data != "":
            print(str(data.decode("utf-8")))
            text_display = str(data.decode("utf-8"))

        cv2.putText(frame, text_display, (30, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 5, (0, 255, 0), 2)

        cv2.namedWindow("Frame", cv2.WINDOW_KEEPRATIO)
        cv2.setWindowProperty("Frame", cv2.WND_PROP_ASPECT_RATIO, cv2.WINDOW_KEEPRATIO)
        cv2.setWindowProperty("Frame", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

        cv2.imshow("text", frame)

        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break


main()