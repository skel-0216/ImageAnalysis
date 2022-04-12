import cv2
import numpy as np
from matplotlib import pyplot as plt
from mylib import *

# 이미지 HSV로 로드
# HSV에서 필터값(명도가 일정값 이상, 이하잇 값)에 걸러지는것들 v를 0으로
# HSV에서 특정 H값 사이에 있는 값을 제외한 v를 0으로
# 이미지에서 v = 0을 제외한 h의 hist 뽑기

