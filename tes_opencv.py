import cv2
import time
from imutils.video import VideoStream
from imutils.video import FPS
import copy
import numpy as np


# initialize the video stream, then allow the camera sensor to warm up
print("[INFO] starting video stream...")
#vs = VideoStream(src="rtsp://192.168.19.12:8554/unicast").start()
#vs = cv2.VideoCapture("rtsp://192.168.18.138:8554/unicast")
#vs = cv2.VideoCapture(0)
#vs = VideoStream(src=0).start()
time.sleep(2.0)

# start the FPS throughput estimator
fps = FPS().start()

tic = time.time()

while True:
    #ssize, frame = vs.read()
    #frame = vs.read()

    frame = cv2.imread("screen.png")

    print(type(frame))

    #frame_pure = copy.copy(frame)

    cv2.namedWindow("Frame", cv2.WINDOW_KEEPRATIO)

    cv2.namedWindow("Frame", cv2.WINDOW_KEEPRATIO)
    cv2.setWindowProperty("Frame", cv2.WND_PROP_ASPECT_RATIO, cv2.WINDOW_KEEPRATIO)
    cv2.setWindowProperty("Frame", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    cv2.imshow("Frame", frame)

    # Plot FPS
    fps.update()

    key = cv2.waitKey(1) & 0xFF

    if time.time() - tic > 100:
        break

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break

fps.stop()
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))