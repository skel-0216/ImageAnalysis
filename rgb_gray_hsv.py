import cv2
import numpy as np

temp_path = "source/2022.8_mackerel/cont/al/eye/d0-dark.tif"


def black_mask(np_arr):
    temp = cv2.cvtColor(np_arr, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(temp, 0, 255, cv2.THRESH_BINARY)
    return mask


# input : "rgb image's path"
# output : (r, g, b)
def get_rgb_mean(path_):
    img = cv2.imread(path_)
    mean_bgr = cv2.mean(img, mask=black_mask(img))

    return mean_bgr[:3]


# input : "rgb image's path"
# output : (gray mean)
def get_gray_mean(path_):
    img = cv2.imread(path_)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    mean_gray = cv2.mean(img_gray, mask=black_mask(img))
    return mean_gray[0]


# input : "rgb image's path"
# output : (h, s, v)
# h:색상, s:채도, v:명도
def get_hsv_mean(path_):
    img = cv2.imread(path_)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mean_hsv = cv2.mean(hsv, mask=black_mask(img))
    return mean_hsv[:3]


# 예시 출력
print(get_rgb_mean(temp_path))
print(get_gray_mean(temp_path))
print(get_hsv_mean(temp_path))