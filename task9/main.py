import cv2


img = cv2.imread("leaf.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


print("shape of original image:", img.shape)
print("shape of gray iamge:", gray.shape)

print("data type of orginal image:", img.dtype)
print("data type of gray image:", gray.dtype)

print("original pixel:", img[100,100])
print("gray pixel:", gray[100,100])

print("original average:", img.mean(axis=(0,1)))
print("gray avg:", gray.mean())

print("size of original image:", img.size)
print("size of gray image:", gray.size)


