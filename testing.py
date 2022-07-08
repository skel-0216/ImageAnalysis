import cv2
import numpy as np


hsv = np.full((200, 200, 3), (150, 255, 255), dtype=np.uint8)

img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)


cv2.imshow("img", img)
cv2.waitKey()
cv2.imwrite("result/img.png", img)