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
    img = cv2.imread(path)
    color = ('b', 'g', 'r')
    for i, col in enumerate(color):
        histr = cv2.calcHist([img], [i], None, [256], [0, 256])
        histr[0] = 0
        plt.plot(histr, color=col)
        plt.xlim([0, 256])
    plt.savefig(resultname)
    return 0


def get_relative_val(src_):
    _under_val, _upper_val = np.percentile(src_[src_ != 0], q=[LOW_CUT, 100 - HIGH_CUT], interpolation='nearest')
    return _under_val, _upper_val