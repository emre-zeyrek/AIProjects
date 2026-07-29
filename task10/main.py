import cv2
import numpy as np



img = cv2.imread("leaf.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray,0,255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
kernel = np.ones((3,3), np.uint8)

erosion = cv2.erode(thresh, kernel, iterations=2)

cv2.imshow("erosion", erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()

dilate = cv2.dilate(thresh, kernel, iterations=2)

cv2.imshow("dilate", dilate)
cv2.waitKey(0)
cv2.destroyAllWindows()

opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

cv2.imshow("opening", opening)
cv2.waitKey(0)
cv2.destroyAllWindows()


cv2.imwrite("leaf_erosion.png", erosion)
cv2.imwrite("leaf_dilate.png", dilate)
cv2.imwrite("leaf_opening.png", opening)