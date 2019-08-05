import socket
import threading
import cv2



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

    file_text = open("display_text.txt")
    for line in file_text:
        text_display = line.strip().split()

    cv2.putText(frame, text_display, (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 5, (0, 255, 0), 2)

    cv2.namedWindow("Frame", cv2.WINDOW_KEEPRATIO)
    cv2.setWindowProperty("Frame", cv2.WND_PROP_ASPECT_RATIO, cv2.WINDOW_KEEPRATIO)
    cv2.setWindowProperty("Frame", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    cv2.imshow("Frame", frame)

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break