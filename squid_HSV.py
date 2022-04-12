import cv2
import numpy as np
from matplotlib import pyplot as plt
from mylib import *

# 이미지 HSV로 로드
# HSV에서 필터값(명도가 일정값 이상, 이하잇 값)에 걸러지는것들 v를 0으로
# HSV에서 특정 H값 사이에 있는 값을 제외한 v를 0으로
# 이미지에서 v = 0을 제외한 h의 hist 뽑기

sample_img = cv2.imread(path_maker('squid#1', 'stage00', 'body', 'bright', '00'))

img_hsv = cv2.cvtColor(sample_img, cv2.COLOR_BGR2HSV)
h_, s_, v_ = cv2.split(img_hsv)
print(np.max(h_))
print(np.min(h_))
hist = cv2.calcHist([h_], [0], None, [256], [0, 256])
hist[0] = 00
plt.ylim(0, 350000)
plt.xlim(0, 179)
plt.plot(hist)
plt.show()
