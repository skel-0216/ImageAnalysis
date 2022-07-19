import cv2
from matplotlib import pyplot as plt
import numpy as np
import os
import mylib


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
            print('Error: Creating directory.' + directory)


def save_hsv_hist_img(path, dst_name, y=(0, 20), range=(0, 180), color=False, line=True):
    sample_img = cv2.imread(path)
    img_hsv = cv2.cvtColor(sample_img, cv2.COLOR_BGR2HSV)
    h_, s_, v_ = cv2.split(img_hsv)
    hist = cv2.calcHist([h_], [0], None, [256], [0, 256])
    hist[0] = 00

    hist_max = max(hist)
    norm_hist = (hist / hist_max) * 255

    empty_image = np.empty((40, 360, 3), dtype=np.uint8)

    i = 0
    for pow in norm_hist:
        # print(int(pow))
        cv2.line(empty_image, (i * 2, 0), (i * 2, 20 * 2), (int(pow), int(pow), int(pow)), 2)
        i += 1
    if line:
        cv2.line(empty_image, (130 * 2, 0 * 2), (130 * 2, 5 * 2), (0, 0, 255), 1)
        cv2.line(empty_image, (130 * 2, 15 * 2), (130 * 2, 20 * 2), (0, 0, 255), 1)

    cv2.imwrite(dst_name, empty_image)
    cv2.waitKey()

    return 0

# (X - MIN) / (MAX-MIN)
# 피크 130 주변에서 보이다가 이동


def save_img_2_350_dark():
    # stage0, 350, stomach, dark
    print("do save_img_2_350_dark()")
    save_hsv_hist_img("source/mackerel#2/stage00/350/stomach/dark/01.png",
                      "result/mackerel_result/stage00_350_stomach_dark_01.png")
    save_hsv_hist_img("source/mackerel#2/stage00/350/stomach/dark/02.png",
                      "result/mackerel_result/stage00_350_stomach_dark_02.png")
    save_hsv_hist_img("source/mackerel#2/stage00/350/stomach/dark/03.png",
                      "result/mackerel_result/stage00_350_stomach_dark_03.png")
    save_hsv_hist_img("source/mackerel#2/stage00/350/stomach/dark/04.png",
                      "result/mackerel_result/stage00_350_stomach_dark_04.png")
    save_hsv_hist_img("source/mackerel#2/stage00/350/stomach/dark/05.png",
                      "result/mackerel_result/stage00_350_stomach_dark_05.png")

    # stage1, 350, stomach, dark
    save_hsv_hist_img("source/mackerel#2/stage01/350/stomach/dark/01.png",
                      "result/mackerel_result/stage01_350_stomach_dark_01.png")
    save_hsv_hist_img("source/mackerel#2/stage01/350/stomach/dark/02.png",
                      "result/mackerel_result/stage01_350_stomach_dark_02.png")
    save_hsv_hist_img("source/mackerel#2/stage01/350/stomach/dark/03.png",
                      "result/mackerel_result/stage01_350_stomach_dark_03.png")
    save_hsv_hist_img("source/mackerel#2/stage01/350/stomach/dark/04.png",
                      "result/mackerel_result/stage01_350_stomach_dark_04.png")
    save_hsv_hist_img("source/mackerel#2/stage01/350/stomach/dark/05.png",
                      "result/mackerel_result/stage01_350_stomach_dark_05.png")


def save_img_2_350_bright():
    # stage0, 350, stomach, bright
    print("do save_img_2_350_bright()")
    save_hsv_hist_img("source/mackerel#2/stage00/350/stomach/bright/01.png",
                      "result/mackerel_result/stage00_350_stomach_bright_01.png")
    save_hsv_hist_img("source/mackerel#2/stage00/350/stomach/bright/02.png",
                      "result/mackerel_result/stage00_350_stomach_bright_02.png")
    save_hsv_hist_img("source/mackerel#2/stage00/350/stomach/bright/03.png",
                      "result/mackerel_result/stage00_350_stomach_bright_03.png")
    save_hsv_hist_img("source/mackerel#2/stage00/350/stomach/bright/04.png",
                      "result/mackerel_result/stage00_350_stomach_bright_04.png")
    save_hsv_hist_img("source/mackerel#2/stage00/350/stomach/bright/05.png",
                      "result/mackerel_result/stage00_350_stomach_bright_05.png")

    # stage1, 350, stomach, bright
    save_hsv_hist_img("source/mackerel#2/stage01/350/stomach/bright/01.png",
                      "result/mackerel_result/stage01_350_stomach_bright_01.png")
    save_hsv_hist_img("source/mackerel#2/stage01/350/stomach/bright/02.png",
                      "result/mackerel_result/stage01_350_stomach_bright_02.png")
    save_hsv_hist_img("source/mackerel#2/stage01/350/stomach/bright/03.png",
                      "result/mackerel_result/stage01_350_stomach_bright_03.png")
    save_hsv_hist_img("source/mackerel#2/stage01/350/stomach/bright/04.png",
                      "result/mackerel_result/stage01_350_stomach_bright_04.png")
    save_hsv_hist_img("source/mackerel#2/stage01/350/stomach/bright/05.png",
                      "result/mackerel_result/stage01_350_stomach_bright_05.png")


def save_img_3_350_bright():
    # stage0, 350, stomach, bright
    print("do save_img_3_350_bright()")
    save_hsv_hist_img("source/mackerel#3/stage00/350/stomach/bright/01.png",
                      "result/mackerel_result/stage00_350_stomach_bright_01.png")
    save_hsv_hist_img("source/mackerel#3/stage00/350/stomach/bright/02.png",
                      "result/mackerel_result/stage00_350_stomach_bright_02.png")
    save_hsv_hist_img("source/mackerel#3/stage00/350/stomach/bright/03.png",
                      "result/mackerel_result/stage00_350_stomach_bright_03.png")
    save_hsv_hist_img("source/mackerel#3/stage00/350/stomach/bright/04.png",
                      "result/mackerel_result/stage00_350_stomach_bright_04.png")
    save_hsv_hist_img("source/mackerel#3/stage00/350/stomach/bright/05.png",
                      "result/mackerel_result/stage00_350_stomach_bright_05.png")

    # stage1, 350, stomach, bright
    save_hsv_hist_img("source/mackerel#3/stage01/350/stomach/bright/01.png",
                      "result/mackerel_result/stage01_350_stomach_bright_01.png")
    save_hsv_hist_img("source/mackerel#3/stage01/350/stomach/bright/02.png",
                      "result/mackerel_result/stage01_350_stomach_bright_02.png")
    save_hsv_hist_img("source/mackerel#3/stage01/350/stomach/bright/03.png",
                      "result/mackerel_result/stage01_350_stomach_bright_03.png")
    save_hsv_hist_img("source/mackerel#3/stage01/350/stomach/bright/04.png",
                      "result/mackerel_result/stage01_350_stomach_bright_04.png")
    save_hsv_hist_img("source/mackerel#3/stage01/350/stomach/bright/05.png",
                      "result/mackerel_result/stage01_350_stomach_bright_05.png")


def save_img_3_350_dark():
    # stage0, 350, stomach, bright
    print("do save_img_3_350_dark()")
    save_hsv_hist_img("source/mackerel#3/stage00/350/stomach/dark/01.png",
                      "result/mackerel_result/stage00_350_stomach_dark_01.png")
    save_hsv_hist_img("source/mackerel#3/stage00/350/stomach/dark/02.png",
                      "result/mackerel_result/stage00_350_stomach_dark_02.png")
    save_hsv_hist_img("source/mackerel#3/stage00/350/stomach/dark/03.png",
                      "result/mackerel_result/stage00_350_stomach_dark_03.png")
    save_hsv_hist_img("source/mackerel#3/stage00/350/stomach/dark/04.png",
                      "result/mackerel_result/stage00_350_stomach_dark_04.png")
    save_hsv_hist_img("source/mackerel#3/stage00/350/stomach/dark/05.png",
                      "result/mackerel_result/stage00_350_stomach_dark_05.png")

    # stage1, 350, stomach, bright
    save_hsv_hist_img("source/mackerel#3/stage01/350/stomach/dark/01.png",
                      "result/mackerel_result/stage01_350_stomach_dark_01.png")
    save_hsv_hist_img("source/mackerel#3/stage01/350/stomach/dark/02.png",
                      "result/mackerel_result/stage01_350_stomach_dark_02.png")
    save_hsv_hist_img("source/mackerel#3/stage01/350/stomach/dark/03.png",
                      "result/mackerel_result/stage01_350_stomach_dark_03.png")
    save_hsv_hist_img("source/mackerel#3/stage01/350/stomach/dark/04.png",
                      "result/mackerel_result/stage01_350_stomach_dark_04.png")
    save_hsv_hist_img("source/mackerel#3/stage01/350/stomach/dark/05.png",
                      "result/mackerel_result/stage01_350_stomach_dark_05.png")


def save_img_2_250_dark():
    # stage0, 350, stomach, dark
    print("do save_img_2_250_dark()")
    save_hsv_hist_img("source/mackerel#2/stage00/250/stomach/dark/01.png",
                      "result/mackerel_result/stage00_250_stomach_dark_01.png")
    save_hsv_hist_img("source/mackerel#2/stage00/250/stomach/dark/02.png",
                      "result/mackerel_result/stage00_250_stomach_dark_02.png")
    save_hsv_hist_img("source/mackerel#2/stage00/250/stomach/dark/03.png",
                      "result/mackerel_result/stage00_250_stomach_dark_03.png")
    save_hsv_hist_img("source/mackerel#2/stage00/250/stomach/dark/04.png",
                      "result/mackerel_result/stage00_250_stomach_dark_04.png")
    save_hsv_hist_img("source/mackerel#2/stage00/250/stomach/dark/05.png",
                      "result/mackerel_result/stage00_250_stomach_dark_05.png")

    # stage1, 350, stomach, dark
    save_hsv_hist_img("source/mackerel#2/stage01/250/stomach/dark/01.png",
                      "result/mackerel_result/stage01_250_stomach_dark_01.png")
    save_hsv_hist_img("source/mackerel#2/stage01/250/stomach/dark/02.png",
                      "result/mackerel_result/stage01_250_stomach_dark_02.png")
    save_hsv_hist_img("source/mackerel#2/stage01/250/stomach/dark/03.png",
                      "result/mackerel_result/stage01_250_stomach_dark_03.png")
    save_hsv_hist_img("source/mackerel#2/stage01/250/stomach/dark/04.png",
                      "result/mackerel_result/stage01_250_stomach_dark_04.png")
    save_hsv_hist_img("source/mackerel#2/stage01/250/stomach/dark/05.png",
                      "result/mackerel_result/stage01_250_stomach_dark_05.png")


def save_img_2_250_bright():
    # stage0, 350, stomach, bright
    print("do save_img_2_250_bright()")
    save_hsv_hist_img("source/mackerel#2/stage00/250/stomach/bright/01.png",
                      "result/mackerel_result/stage00_250_stomach_bright_01.png")
    save_hsv_hist_img("source/mackerel#2/stage00/250/stomach/bright/02.png",
                      "result/mackerel_result/stage00_250_stomach_bright_02.png")
    save_hsv_hist_img("source/mackerel#2/stage00/250/stomach/bright/03.png",
                      "result/mackerel_result/stage00_250_stomach_bright_03.png")
    save_hsv_hist_img("source/mackerel#2/stage00/250/stomach/bright/04.png",
                      "result/mackerel_result/stage00_250_stomach_bright_04.png")
    save_hsv_hist_img("source/mackerel#2/stage00/250/stomach/bright/05.png",
                      "result/mackerel_result/stage00_250_stomach_bright_05.png")

    # stage1, 350, stomach, bright
    save_hsv_hist_img("source/mackerel#2/stage01/250/stomach/bright/01.png",
                      "result/mackerel_result/stage01_250_stomach_bright_01.png")
    save_hsv_hist_img("source/mackerel#2/stage01/250/stomach/bright/02.png",
                      "result/mackerel_result/stage01_250_stomach_bright_02.png")
    save_hsv_hist_img("source/mackerel#2/stage01/250/stomach/bright/03.png",
                      "result/mackerel_result/stage01_250_stomach_bright_03.png")
    save_hsv_hist_img("source/mackerel#2/stage01/250/stomach/bright/04.png",
                      "result/mackerel_result/stage01_250_stomach_bright_04.png")
    save_hsv_hist_img("source/mackerel#2/stage01/250/stomach/bright/05.png",
                      "result/mackerel_result/stage01_250_stomach_bright_05.png")


def save_img_3_250_bright():
    # stage0, 350, stomach, bright
    print("do save_img_3_250_bright()")
    save_hsv_hist_img("source/mackerel#3/stage00/250/stomach/bright/01.png",
                      "result/mackerel_result/stage00_250_stomach_bright_01.png")
    save_hsv_hist_img("source/mackerel#3/stage00/250/stomach/bright/02.png",
                      "result/mackerel_result/stage00_250_stomach_bright_02.png")
    save_hsv_hist_img("source/mackerel#3/stage00/250/stomach/bright/03.png",
                      "result/mackerel_result/stage00_250_stomach_bright_03.png")
    save_hsv_hist_img("source/mackerel#3/stage00/250/stomach/bright/04.png",
                      "result/mackerel_result/stage00_250_stomach_bright_04.png")
    save_hsv_hist_img("source/mackerel#3/stage00/250/stomach/bright/05.png",
                      "result/mackerel_result/stage00_250_stomach_bright_05.png")

    # stage1, 350, stomach, bright
    save_hsv_hist_img("source/mackerel#3/stage01/250/stomach/bright/01.png",
                      "result/mackerel_result/stage01_250_stomach_bright_01.png")
    save_hsv_hist_img("source/mackerel#3/stage01/250/stomach/bright/02.png",
                      "result/mackerel_result/stage01_250_stomach_bright_02.png")
    save_hsv_hist_img("source/mackerel#3/stage01/250/stomach/bright/03.png",
                      "result/mackerel_result/stage01_250_stomach_bright_03.png")
    save_hsv_hist_img("source/mackerel#3/stage01/250/stomach/bright/04.png",
                      "result/mackerel_result/stage01_250_stomach_bright_04.png")
    save_hsv_hist_img("source/mackerel#3/stage01/250/stomach/bright/05.png",
                      "result/mackerel_result/stage01_250_stomach_bright_05.png")


def save_img_3_250_dark():
    # stage0, 350, stomach, bright
    print("do save_img_3_250_dark()")
    save_hsv_hist_img("source/mackerel#3/stage00/250/stomach/dark/01.png",
                      "result/mackerel_result/stage00_250_stomach_dark_01.png")
    save_hsv_hist_img("source/mackerel#3/stage00/250/stomach/dark/02.png",
                      "result/mackerel_result/stage00_250_stomach_dark_02.png")
    save_hsv_hist_img("source/mackerel#3/stage00/250/stomach/dark/03.png",
                      "result/mackerel_result/stage00_250_stomach_dark_03.png")
    save_hsv_hist_img("source/mackerel#3/stage00/250/stomach/dark/04.png",
                      "result/mackerel_result/stage00_250_stomach_dark_04.png")
    save_hsv_hist_img("source/mackerel#3/stage00/250/stomach/dark/05.png",
                      "result/mackerel_result/stage00_250_stomach_dark_05.png")

    # stage1, 350, stomach, bright
    save_hsv_hist_img("source/mackerel#3/stage01/250/stomach/dark/01.png",
                      "result/mackerel_result/stage01_250_stomach_dark_01.png")
    save_hsv_hist_img("source/mackerel#3/stage01/250/stomach/dark/02.png",
                      "result/mackerel_result/stage01_250_stomach_dark_02.png")
    save_hsv_hist_img("source/mackerel#3/stage01/250/stomach/dark/03.png",
                      "result/mackerel_result/stage01_250_stomach_dark_03.png")
    save_hsv_hist_img("source/mackerel#3/stage01/250/stomach/dark/04.png",
                      "result/mackerel_result/stage01_250_stomach_dark_04.png")
    save_hsv_hist_img("source/mackerel#3/stage01/250/stomach/dark/05.png",
                      "result/mackerel_result/stage01_250_stomach_dark_05.png")

# # stage0, 350, stomach, dark
# mylib.save_hsv_hist(["source/mackerel#2/stage00/350/stomach/dark/01.png"], "result/mackerel_result/hist_stage00_350_stomach_dark_01.png")
# mylib.save_hsv_hist(["source/mackerel#2/stage00/350/stomach/dark/02.png"], "result/mackerel_result/hist_stage00_350_stomach_dark_02.png")
# mylib.save_hsv_hist(["source/mackerel#2/stage00/350/stomach/dark/03.png"], "result/mackerel_result/hist_stage00_350_stomach_dark_03.png")
# mylib.save_hsv_hist(["source/mackerel#2/stage00/350/stomach/dark/04.png"], "result/mackerel_result/hist_stage00_350_stomach_dark_04.png")
# mylib.save_hsv_hist(["source/mackerel#2/stage00/350/stomach/dark/05.png"], "result/mackerel_result/hist_stage00_350_stomach_dark_05.png")
#
# # stage1, 350, stomach, dark
# mylib.save_hsv_hist(["source/mackerel#2/stage01/350/stomach/dark/01.png"], "result/mackerel_result/hist_stage01_350_stomach_dark_01.png")
# mylib.save_hsv_hist(["source/mackerel#2/stage01/350/stomach/dark/02.png"], "result/mackerel_result/hist_stage01_350_stomach_dark_02.png")
# mylib.save_hsv_hist(["source/mackerel#2/stage01/350/stomach/dark/03.png"], "result/mackerel_result/hist_stage01_350_stomach_dark_03.png")
# mylib.save_hsv_hist(["source/mackerel#2/stage01/350/stomach/dark/04.png"], "result/mackerel_result/hist_stage01_350_stomach_dark_04.png")
# mylib.save_hsv_hist(["source/mackerel#2/stage01/350/stomach/dark/05.png"], "result/mackerel_result/hist_stage01_350_stomach_dark_05.png")

save_img_2_250_dark()
save_img_2_250_bright()