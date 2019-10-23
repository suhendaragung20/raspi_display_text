import socket
import cv2


# Get host and port
host = "10.14.3.249"
port = 60000

# Create new server socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(5)

sock_client, address_client = sock.accept()

print("Connected with " + str(address_client))

text_display = ""

while True:

    try:
        data = sock_client.recv(32)
    except:
        print("Client " + str(address_client) + " has disconnected")
        break
    if data != "":
        print(str(data.decode("utf-8")))
        text_display = str(data.decode("utf-8"))

        f = open('display_text.txt', "w+")
        for i in range(1):
            f.write(text_display)
        f.close()

    # -------------- DISPLAY -----------------

    frame = cv2.imread("screen.png")

    key = cv2.waitKey(1) & 0xFF

    try:
        with open('display_text.txt', 'r') as file:
            data = file.read().replace('\n', '')
            text_display = str(data)
    except KeyboardInterrupt:
        break
    except:
        continue

    result = [x.strip() for x in text_display.split(',')]

    if len(result) > 1:
        cv2.putText(frame, result[0], (30, 350), cv2.FONT_HERSHEY_SIMPLEX, 5, (0, 0, 0), 10)
        cv2.putText(frame, result[1], (30, 600), cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 0, 0), 8)

    # print(text_display)

    (rows, cols) = frame.shape[:2]
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 180, 1)
    frame = cv2.warpAffine(frame, M, (cols, rows))

    cv2.namedWindow("Frame", cv2.WINDOW_KEEPRATIO)
    cv2.setWindowProperty("Frame", cv2.WND_PROP_ASPECT_RATIO, cv2.WINDOW_KEEPRATIO)
    cv2.setWindowProperty("Frame", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    cv2.imshow("Frame", frame)

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break