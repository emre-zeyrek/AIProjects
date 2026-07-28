import cv2

img = cv2.imread("leaf.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresholded = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)


cv2.imshow("original", img)
cv2.imshow("gray", gray)
cv2.imshow("thresholded", thresholded)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("thresholded_leaf.png", thresholded)