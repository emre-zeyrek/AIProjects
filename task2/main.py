import cv2

img = cv2.imread("taskimage.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("gray_photo",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("taskimage_gray.png", gray)

