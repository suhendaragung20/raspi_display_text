
import cv2


text_display = ""

while True:
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

    cv2.putText(frame, text_display, (30, 300), cv2.FONT_HERSHEY_SIMPLEX, 20, (0, 0, 0), 30)

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