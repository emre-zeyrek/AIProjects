import cv2
import numpy as np

capture = cv2.VideoCapture(1)

if not capture.isOpened():
    print("VideoWriter did not open correctly")
    exit()

lower_black = np.array([0, 0, 0])
upper_array = np.array([180, 255, 50])


while capture.isOpened():

    ret, frame = capture.read()

    if not ret:
        print("Cant receive frame. exiting..")
        break

    frame = cv2.flip(frame, 1)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_black, upper_array)

    kernel = np.ones((5,5), np.uint8)
    mask = cv2.erode(mask, kernel, iterations=2)
    mask = cv2.dilate(mask, kernel, iterations=2)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        largest = max(contours, key=cv2.contourArea)

        if cv2.contourArea(largest) > 500:
            x, y, w, h = cv2.boundingRect(largest)
            cv2.rectangle(frame, (x,y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, "Black object", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)


    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
capture.release()





