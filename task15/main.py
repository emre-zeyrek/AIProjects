import cv2
import numpy as np

capture = cv2.VideoCapture(1)

if not capture.isOpened():
    print("VideoWriter didnt open correctly")
    exit()

cv2.namedWindow("Trackbars")
cv2.createTrackbar("H-min", "Trackbars", 0, 179,lambda x: None)
cv2.createTrackbar("H-max", "Trackbars", 179, 179,lambda x: None)
cv2.createTrackbar("S-min", "Trackbars", 0, 255,lambda x: None)
cv2.createTrackbar("S-max", "Trackbars", 255, 255,lambda x: None)
cv2.createTrackbar("V-min", "Trackbars", 0, 255,lambda x: None)
cv2.createTrackbar("V-max", "Trackbars", 255, 255,lambda x: None)

while capture.isOpened():

    ret, frame = capture.read()

    if not ret:
        print("cant receive frame. exiting..")
        break

    frame = cv2.flip(frame, 1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    value = cv2.getTrackbarPos("H-min", "Trackbars")
    value2 = cv2.getTrackbarPos("H-max", "Trackbars")
    value3 = cv2.getTrackbarPos("S-min", "Trackbars")
    value4 = cv2.getTrackbarPos("S-max", "Trackbars")
    value5 = cv2.getTrackbarPos("V-min", "Trackbars")
    value6 = cv2.getTrackbarPos("V-max", "Trackbars")

    lower = np.array([value, value3, value5])
    upper = np.array([value2, value4, value6])
    mask = cv2.inRange(hsv, lower, upper)


    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        largest = max(contours, key=cv2.contourArea)

        if cv2.contourArea(largest) > 500:
            x, y, w, h = cv2.boundingRect(largest)
            cv2.rectangle(frame, (x,y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, "Colourful object", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)


    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
capture.release()