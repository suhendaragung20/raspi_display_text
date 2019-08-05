
import cv2


text_display = ""

while True:
    frame = cv2.imread("screen.png")

    key = cv2.waitKey(1) & 0xFF

    try:
        file_text = open("display_text.txt")
        for line in file_text:
            text_display = line.strip().split()
    except KeyboardInterrupt:
        break
    except:
        continue

    cv2.putText(frame, text_display, (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 5, (0, 255, 0), 2)

    cv2.namedWindow("Frame", cv2.WINDOW_KEEPRATIO)
    cv2.setWindowProperty("Frame", cv2.WND_PROP_ASPECT_RATIO, cv2.WINDOW_KEEPRATIO)
    cv2.setWindowProperty("Frame", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    cv2.imshow("Frame", frame)

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break