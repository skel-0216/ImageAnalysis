import cv2
import numpy as np
from matplotlib import pyplot as plt


def mackerel2hist_H(src_image):
    img_hsv = cv2.cvtColor(src_image, cv2.COLOR_BGR2HSV)
    h_, s_, v_ = cv2.split(img_hsv)
    h_[v_ > 254] = 0
    hist = cv2.calcHist([h_], [0], None, [256], [0, 256])
    hist[0] = 0
    hist = (hist / hist.sum()) * 100
    return hist[:180]


def squid2hist_BGR(src_image):
    color = ('b', 'g', 'r')
    hist = []
    for i, col in enumerate(color):
        hist.append(cv2.calcHist([src_image], [i], None, [256], [0, 256]))

    # remove out of ROI
    hist[0][0] = 0
    hist[1][0] = 0
    hist[2][0] = 0

    # remove white(saturation)
    hist[0][255] = 0
    hist[1][255] = 0
    hist[2][255] = 0

    hist[0] = (hist[0] / hist[0].sum()) * 100
    hist[1] = (hist[1] / hist[1].sum()) * 100
    hist[2] = (hist[2] / hist[2].sum()) * 100
    return hist
