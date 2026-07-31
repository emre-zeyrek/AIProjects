import cv2


net = cv2.dnn.readNetFromDarknet("yolov3-face.cfg", "yolov3-wider_16000.weights")
layer_names = net.getLayerNames()
output_layers = [layer_names[i -1] for i in net.getUnconnectedOutLayers()]


capture = cv2.VideoCapture(1)

if not capture.isOpened():
    print("VideoWriter didnt open correctly")
    exit()

while capture.isOpened():
    boxes = []
    confidences = []

    ret, frame = capture.read()

    if not ret:
        print("cant receive frame. exiting..")
        break

    frame = cv2.flip(frame, 1)
    blob = cv2.dnn.blobFromImage(frame, 1/255.0, (416,416), swapRB=True, crop=False)
    net.setInput(blob)
    outputs = net.forward(output_layers)
    print(len(outputs))

    height, width = frame.shape[:2]

    for out in outputs:
        for detection in out:
            confidence = detection[4]
            if confidence > 0.5:
                confidences.append(float(confidence))
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                x = int(center_x - w/2)
                y = int(center_y - h/2)
                boxes.append([x, y, w, h])


    indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    for i in indices:
        x, y, w, h = boxes[i]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)



    cv2.imshow("frame", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
capture.release()
