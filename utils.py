import cv2

import os
import numpy as np
import math
import matplotlib.pyplot as plt

from openpyxl import Workbook

# RGB 분석방식 결과가 깔끔하지 않다. 구조 자체가 수정 필요
# 아니면 RGB hist 자체 return을 3개로 할까
import asset_filename


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

    def black_mask(self):
        temp = cv2.cvtColor(self.__img, cv2.COLOR_BGR2GRAY)
        ret, mask = cv2.threshold(temp, 0, 255, cv2.THRESH_BINARY)
        return mask

    def eye_black_hist(self):
        mask = self.black_mask()
        temp = cv2.cvtColor(self.__img, cv2.COLOR_BGR2GRAY)
        hist = cv2.calcHist([temp], [0], mask, [256], [0, 256])
        hist = hist / sum(hist) * 100
        result = hist.tolist()
        return sum(result, [])

    def eye_rgb_hist(self):
        mask = self.black_mask()

        color = ('b', 'g', 'r')
        result = []

        for i, col in enumerate(color):
            histr = cv2.calcHist([self.__img], [i], mask, [256], [0, 256])
            histr = histr / sum(histr) * 100
            temp = histr.tolist()
            result.append(sum(temp, []))

        return result[0], result[1], result[2]

    def get_representative_value(self, type="mode", value=1):
        result = []
        if type == "mode":
            h_, s_, v_ = cv2.split(self.__img_hsv)
            vals, counts = np.unique(h_, return_counts=True)

            # value에 따라 값 여러개 나오게 하기
            counts[0] = 0  # remove black - this can remove pure red

            for i in range(int(value)):
                # 최빈값 저장
                index = np.argmax(counts)
                result.append(vals[index])

                # 저장한 최빈값 제거-> 이후 최빈값 검색에서 찾지 않도록
                counts[index] = 0
            return result

        elif type == "mean":  # trimmed mean
            h_, s_, v_ = cv2.split(self.__img_hsv)
            vals, counts = np.unique(h_, return_counts=True)
            temp = vals * counts
            mean = sum(temp) / sum(counts)
            return mean

    def get_hsv_var(self, norm="Null"):
        temp = self.hsv_hist(norm=norm)
        variance = np.var(temp)
        return variance

    def get_rgb_var(self, norm="Null"):
        temp = self.rgb_hist(norm=norm)
        variance = np.var(temp)
        return variance

    def get_hsv_std(self, norm="Null"):
        temp = self.hsv_hist(norm=norm)
        variance = np.std(temp)
        return variance

    def get_rgb_std(self, norm="Null"):
        temp = self.rgb_hist(norm=norm)
        variance = np.std(temp)
        return variance

    def temp_get_grade(self):
        temp = self.hsv_hist(norm="Percent")
        temp1 = temp[130:]
        i = 50
        sum = 0
        for value in temp1:
            sum += i * math.sqrt(value)
            i -= 1
        return sum / 100


def excel_write(rows, filename="result/excel/temp.xlsx"):
    wb = Workbook()
    ws = wb.active
    ws.title = "First Sheet"

    for i in rows:
        ws.append(i)
    wb.save(filename)


def get_excel_old(case, value=180, filename=None):
    data_list = [["stage00"]]

    fish = 0
    for imgs in case[0]:
        image = Image(imgs)
        item = image.get_representative_value(value=value)
        data_list.append(['fish%d' % fish] + item)
        fish += 1

    fish = 0
    data_list.append(["stage01"])
    for imgs in case[1]:
        image = Image(imgs)
        item = image.get_representative_value(value=value)
        data_list.append(['fish%d' % fish] + item)
        fish += 1

    if filename is not None:
        excel_write(data_list, filename)
    else:
        excel_write(data_list)


def get_excel(case, value=180, filename=None, type="stomach"):
    count = 0
    data_list = []
    for i in range(len(case)):
        data_list.append(["stage%2d" % count])
        fish = 0
        for imgs in case[i]:
            image = Image(imgs)
            item =[]
            if type == "stomach":
                item = image.get_representative_value(value=value)
            elif type == "eye_gray":
                item = image.eye_black_hist()
            elif type == "eye_rgb":
                item = image.eye_rgb_hist()
            else:
                print("ERROR  :: Occur")
                return -1
            data_list.append(['fish%d' % fish] + item)
            fish += 1
        count += 1

    if filename is not None:
        excel_write(data_list, filename)
    else:
        excel_write(data_list)


def print_var_std(asset_list, norm="Null"):
    for imgs in asset_list:
        for img in imgs:
            image = Image(img)
            print(img, "   VAR : ", image.get_hsv_var(norm=norm))
        print()
        for img in imgs:
            image = Image(img)
            print(img, "   std : ", image.get_hsv_std(norm=norm))
        print()


# image00 = Image(asset_filename.mackerel2_250_stomach_dark[0][0])
# image01 = Image(asset_filename.mackerel2_250_stomach_dark[1][0])
#
# print(image00.get_representative_value(value=20))
# print(image01.get_representative_value(value=20))

# 15% is 27
# 90th num is '중앙값'
# 45th num is '4분위수'
# value = 45
#
# for imgs in asset_filename.mackerel2_250_stomach_dark[0]:
#     image = Image(imgs)
#     item = image.get_representative_value(value=value)
#     print(item, '  \t', sum(item)/value)
#
#
# for imgs in asset_filename.mackerel2_250_stomach_dark[1]:
#     image = Image(imgs)
#     item = image.get_representative_value(value=value)
#     print(item, '  \t', sum(item)/value)

# get_excel(asset_filename.mackerel2_250_stomach_dark, "result/excel/mackerel2_250_stomach_dark.xlsx")

# 최빈값 찾긴 했는데.. 이건 그냥 피크 찾는거랑 같다.
# 분산 정도에 따른 값은 없을까?

# 데이터 엑셀에 정리

# get_excel(asset_filename.mackerel2_250_stomach_dark, filename="result/excel/mackerel2_250_stomach_dark.xlsx")
# get_excel(asset_filename.mackerel2_250_stomach_bright, filename="result/excel/mackerel2_250_stomach_bright.xlsx")
#
# get_excel(asset_filename.mackerel2_350_stomach_dark, filename="result/excel/mackerel2_350_stomach_dark.xlsx")
# get_excel(asset_filename.mackerel2_350_stomach_bright, filename="result/excel/mackerel2_350_stomach_bright.xlsx")
#
# get_excel(asset_filename.mackerel3_250_stomach_dark, filename="result/excel/mackerel3_250_stomach_dark.xlsx")
# get_excel(asset_filename.mackerel3_250_stomach_bright, filename="result/excel/mackerel3_250_stomach_bright.xlsx")
#
# get_excel(asset_filename.mackerel3_350_stomach_dark, filename="result/excel/mackerel3_350_stomach_dark.xlsx")
# get_excel(asset_filename.mackerel3_350_stomach_bright, filename="result/excel/mackerel3_350_stomach_bright.xlsx")
#
# get_excel(asset_filename.mackerel2_250_back_dark, filename="result/excel/mackerel2_250_back_dark.xlsx")
# get_excel(asset_filename.mackerel2_250_back_bright, filename="result/excel/mackerel2_250_back_bright.xlsx")
#
# get_excel(asset_filename.mackerel2_350_back_dark, filename="result/excel/mackerel2_350_back_dark.xlsx")
# get_excel(asset_filename.mackerel2_350_back_bright, filename="result/excel/mackerel2_350_back_bright.xlsx")
#
# get_excel(asset_filename.mackerel3_250_back_dark, filename="result/excel/mackerel3_250_back_dark.xlsx")
# get_excel(asset_filename.mackerel3_250_back_bright, filename="result/excel/mackerel3_250_back_bright.xlsx")
#
# get_excel(asset_filename.mackerel3_350_back_dark, filename="result/excel/mackerel3_350_back_dark.xlsx")
# get_excel(asset_filename.mackerel3_350_back_bright, filename="result/excel/mackerel3_350_back_bright.xlsx")

# print_var_std(asset_filename.mackerel2_350_stomach_dark, norm="Percent")

# for imgs in asset_filename.mackerel3_250_stomach_dark:
#     for img in imgs:
#         image = Image(img)
#         print(image.temp_get_grade())
#     print()


get_excel(asset_filename.mackerel3_350_eye_dark, filename="result/excel/mackerel_eyes_gray.xlsx", type="eye_gray")
