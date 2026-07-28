import cv2

img = cv2.imread("taskimage.png")

resized = cv2.resize(img,(700,700))

cropped = resized[50:300,100:400]

cv2.imshow("cropped", cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("taskimage_resized.png", cropped)