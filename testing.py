import cv2

img = cv2.imread('source/test.png')
cv2.imshow("img", img)
cv2.waitKey()
print(img)
