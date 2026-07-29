import cv2

img = cv2.imread("leaf.png")

flip_horizontal = cv2.flip(img, 1)
flip_vertical = cv2.flip(img, 0)
flip_both =cv2.flip(img, -1)

cv2.imshow("original", img)
cv2.imshow("flip horizontal", flip_horizontal)
cv2.imshow("flip vertical", flip_vertical)
cv2.imshow("flip both", flip_both)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("leaf_flip_horizontal.png", flip_horizontal)
cv2.imwrite("leaf_flip_vertical.png", flip_vertical)
cv2.imwrite("leaf_flip_both.png", flip_both)


