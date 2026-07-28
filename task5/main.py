import cv2

img = cv2.imread("taskimage.png")

x1, y1 = 100, 100
x2, y2 = 1000, 800

roi = img[y1:y2, x1:x2]

roi_gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

roi_gray_bgr = cv2.cvtColor(roi_gray, cv2.COLOR_GRAY2BGR)

roi_blurred = cv2.GaussianBlur(roi_gray_bgr, (15,15), 0)

img[y1:y2, x1:x2] = roi_blurred


cv2.imshow("gray_rectangle_blurred", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("blurred_image_with_gray_rectangle.png", img)
