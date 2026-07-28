import cv2
import numpy as np

img = cv2.imread("leaf.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 100, 200)

cv2.imshow("edges canny", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("edges.png", edges)

gray_float = np.float32(gray)
corners = cv2.cornerHarris(gray_float, 5, 3, 0.04 )

corners = cv2.dilate(corners, None)

img_corners = img.copy()
print(corners.max())
img_corners[corners > 0.1 * corners.max()] = [0, 0, 255]

cv2.imshow("corners.png", img_corners)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("corners.png", img_corners)
