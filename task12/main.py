import cv2

capture = cv2.VideoCapture(1)

if not capture.isOpened():
    print("VideoWriter did not open correctly")
    exit()


while capture.isOpened():
    ret, frame = capture.read()

    if not ret:
        print("Cant receive frame. Exiting..")
        break

    frame = cv2.flip(frame, 1)

    cv2.imshow("frame", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
capture.release()


