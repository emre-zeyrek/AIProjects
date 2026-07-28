import cv2

img = cv2.imread("taskimage.png")

x1, y1 = 100, 100
x2, y2 = 1000, 800

yellow = (0,255,255)

cv2.rectangle(img, (x1,y1), (x2,y2), yellow, -1)

cv2.imshow("yellow_rectangle", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("taskimage_yellow_rectangle.png", img)
