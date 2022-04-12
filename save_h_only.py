import cv2
import numpy as np

src_path = 'squid#1/stage02/body/bright/01.png'

dest_path = 'temp/only_h_stage#2.png'

img_bgr = cv2.imread(src_path)

img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)

# H 그대로, S 최대, V 0이 아닌곳은 최대
img_hsv[:, :, 1] = 255
img_hsv[:, :, 2] == 255

result = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2RGB)

cv2.imshow('save_h_only', result)
cv2.waitKey()

cv2.imwrite(dest_path, result)

