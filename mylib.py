import cv2
import numpy as np
from matplotlib import pyplot as plt


LOW_CUT = 5
HIGH_CUT = 5


def path_maker(type_, stage_, target_, light_, n_):
    path = type_ + '/' + stage_ + '/' + target_ + '/' + light_ + '/' + n_ + '.png'
    return path


def save_rgb_hist(path, resultname):
    img = cv2.imread(path)
    color = ('b', 'g', 'r')
    for i, col in enumerate(color):
        histr = cv2.calcHist([img], [i], None, [256], [0, 256])
        histr[0] = 0
        plt.plot(histr, color=col, label=col)
        plt.legend()
        plt.xlim([0, 256])
    plt.savefig(resultname)
    plt.close()
    return 0


def save_rgb_hist_accumulate(path, resultname):
    for paths in path:
        img = cv2.imread(paths)
        color = ('b', 'g', 'r')
        for i, col in enumerate(color):
            histr = cv2.calcHist([img], [i], None, [256], [0, 256])
            histr[0] = 0
            plt.plot(histr, color=col)
            plt.xlim([0, 256])
    plt.savefig(resultname)
    return 0


def get_relative_val(src_, low_cut=LOW_CUT, high_cut=HIGH_CUT):
    _under_val, _upper_val = np.percentile(src_[src_ != 0], q=[low_cut, 100 - high_cut], interpolation='nearest')
    return _under_val, _upper_val


def hue_high_cut(src, value=240):
    img_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
    h_, s_, v_ = cv2.split(img_hsv)
    v_[v_ > value] = 0
    img_result = cv2.merge([h_, s_, v_])
    return img_result

