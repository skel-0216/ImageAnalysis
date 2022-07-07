import cv2
import os

import numpy as np
from matplotlib import pyplot as plt

# RGB 분석방식 결과가 깔끔하지 않다. 구조 자체가 수정 필요
# 아니면 RGB hist 자체 return을 3개로 할까

test_path = "source/croaker#1/stage00/body/bright/01.png"


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory.' + directory)


class Image:
    def __init__(self, path):
        self.__img = cv2.imread(path)
        self.__img_hsv = cv2.cvtColor(self.__img, cv2.COLOR_BGR2HSV)
        pass

    def hsv_hist(self, norm="Null"):
        # norm type Null, MinMax, Percent
        h_, s_, v_ = cv2.split(self.__img_hsv)
        hist = cv2.calcHist([h_], [0], None, [256], [0, 256])[0:180]
        hist[0] = 00
        if norm == "Null":
            return hist

        # (X - MIN) / (MAX-MIN)
        if norm == "MinMax":
            hist_max = max(hist)
            hist_min = min(hist)
            norm_hist = (hist - hist_min) / hist_max * 255
            return norm_hist

        if norm == "Percent":
            norm_hist = (hist / sum(hist)) * 100
            return norm_hist

    def rgb_hist(self, norm="Null"):
        color = ('b', 'g', 'r')
        result = []
        for i, col in enumerate(color):
            histr = cv2.calcHist([self.__img], [i], None, [256], [0, 256])
            histr[0] = 0
            result.append(histr)

        hist = np.stack(result)

        if norm == "Null":
            return hist

            # (X - MIN) / (MAX-MIN)
        if norm == "MinMax":
            hist_max = max(hist)
            hist_min = min(hist)
            norm_hist = (hist - hist_min) / hist_max * 255
            return norm_hist

        if norm == "Percent":
            norm_hist = (hist / sum(hist)) * 100
            return norm_hist


def get_representative_value(type_="mode"):
    # 최빈값, 평균(절사평균), 중앙값
    if type_ == "mode":
        return 0
    elif type_ == "mean":   # trimmed mean
        return 1
    elif type_ == "median":
        return 3


image = Image(test_path)
print(image.hsv_hist().shape)

plt.plot(image.hsv_hist())
plt.show()


