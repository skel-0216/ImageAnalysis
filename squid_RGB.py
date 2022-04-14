import cv2
import numpy as np
from matplotlib import pyplot as plt
from mylib import *

# filter (반사광 제거정도..? 만들기)


'''
save_rgb_hist(path_maker('squid#1', 'stage00', 'body', 'bright', '00'), 'result/#1_00_body_bright_00')
save_rgb_hist(path_maker('squid#1', 'stage00', 'body', 'bright', '01'), 'result/#1_00_body_bright_01')
save_rgb_hist(path_maker('squid#1', 'stage00', 'body', 'bright', '02'), 'result/#1_00_body_bright_02')
save_rgb_hist(path_maker('squid#1', 'stage00', 'body', 'bright', '03'), 'result/#1_00_body_bright_03')
save_rgb_hist(path_maker('squid#1', 'stage00', 'body', 'bright', '04'), 'result/#1_00_body_bright_04')

save_rgb_hist(path_maker('squid#1', 'stage01', 'body', 'bright', '00'), 'result/#1_01_body_bright_00')
save_rgb_hist(path_maker('squid#1', 'stage01', 'body', 'bright', '01'), 'result/#1_01_body_bright_01')
save_rgb_hist(path_maker('squid#1', 'stage01', 'body', 'bright', '02'), 'result/#1_01_body_bright_02')
save_rgb_hist(path_maker('squid#1', 'stage01', 'body', 'bright', '03'), 'result/#1_01_body_bright_03')
save_rgb_hist(path_maker('squid#1', 'stage01', 'body', 'bright', '04'), 'result/#1_01_body_bright_04')

save_rgb_hist(path_maker('squid#1', 'stage02', 'body', 'bright', '00'), 'result/#1_02_body_bright_00')
save_rgb_hist(path_maker('squid#1', 'stage02', 'body', 'bright', '01'), 'result/#1_02_body_bright_01')
save_rgb_hist(path_maker('squid#1', 'stage02', 'body', 'bright', '02'), 'result/#1_02_body_bright_02')
save_rgb_hist(path_maker('squid#1', 'stage02', 'body', 'bright', '03'), 'result/#1_02_body_bright_03')
save_rgb_hist(path_maker('squid#1', 'stage02', 'body', 'bright', '04'), 'result/#1_02_body_bright_04')
'''
"""
save_rgb_hist(path_maker('squid#1', 'stage00', 'head', 'bright', '00'), 'result/#1_00_body_bright_00')
save_rgb_hist(path_maker('squid#1', 'stage00', 'head', 'bright', '01'), 'result/#1_00_body_bright_01')
save_rgb_hist(path_maker('squid#1', 'stage00', 'head', 'bright', '02'), 'result/#1_00_body_bright_02')
save_rgb_hist(path_maker('squid#1', 'stage00', 'head', 'bright', '03'), 'result/#1_00_body_bright_03')
save_rgb_hist(path_maker('squid#1', 'stage00', 'head', 'bright', '04'), 'result/#1_00_body_bright_04')

save_rgb_hist(path_maker('squid#1', 'stage01', 'head', 'bright', '00'), 'result/#1_01_body_bright_00')
save_rgb_hist(path_maker('squid#1', 'stage01', 'head', 'bright', '01'), 'result/#1_01_body_bright_01')
save_rgb_hist(path_maker('squid#1', 'stage01', 'head', 'bright', '02'), 'result/#1_01_body_bright_02')
save_rgb_hist(path_maker('squid#1', 'stage01', 'head', 'bright', '03'), 'result/#1_01_body_bright_03')
save_rgb_hist(path_maker('squid#1', 'stage01', 'head', 'bright', '04'), 'result/#1_01_body_bright_04')

save_rgb_hist(path_maker('squid#1', 'stage02', 'head', 'bright', '00'), 'result/#1_02_body_bright_00')
save_rgb_hist(path_maker('squid#1', 'stage02', 'head', 'bright', '01'), 'result/#1_02_body_bright_01')
save_rgb_hist(path_maker('squid#1', 'stage02', 'head', 'bright', '02'), 'result/#1_02_body_bright_02')
save_rgb_hist(path_maker('squid#1', 'stage02', 'head', 'bright', '03'), 'result/#1_02_body_bright_03')
save_rgb_hist(path_maker('squid#1', 'stage02', 'head', 'bright', '04'), 'result/#1_02_body_bright_04')
"""
'''
path_acc01 = [path_maker('squid#1', 'stage00', 'body', 'bright', '00'),
              path_maker('squid#1', 'stage00', 'body', 'bright', '01'),
              path_maker('squid#1', 'stage00', 'body', 'bright', '02'),
              path_maker('squid#1', 'stage00', 'body', 'bright', '03'),
              path_maker('squid#1', 'stage00', 'body', 'bright', '04')]
              
save_rgb_hist_accumulate(path_acc01, 'result/acc00_body_bright')
'''
'''
path_acc02 = [path_maker('squid#1', 'stage01', 'body', 'bright', '00'),
              path_maker('squid#1', 'stage01', 'body', 'bright', '01'),
              path_maker('squid#1', 'stage01', 'body', 'bright', '02'),
              path_maker('squid#1', 'stage01', 'body', 'bright', '03'),
              path_maker('squid#1', 'stage01', 'body', 'bright', '04')]
              
save_rgb_hist_accumulate(path_acc01, 'result/acc01_body_bright')
'''

"""
path_acc03 = [path_maker('croaker#1', 'stage00', 'body', 'bright', '00'),
              path_maker('croaker#1', 'stage01', 'body', 'bright', '00'),
              path_maker('croaker#1', 'stage02', 'body', 'bright', '00'),
              path_maker('croaker#1', 'stage03', 'body', 'bright', '00'),
              path_maker('croaker#1', 'stage04', 'body', 'bright', '00'),
              path_maker('croaker#1', 'stage05', 'body', 'bright', '00')]
"""

path_acc03 = [path_maker('croaker#1', 'stage00', 'body', 'dark', '00'),
              path_maker('croaker#1', 'stage01', 'body', 'dark', '00'),
              path_maker('croaker#1', 'stage02', 'body', 'dark', '00'),
              path_maker('croaker#1', 'stage03', 'body', 'dark', '00'),
              path_maker('croaker#1', 'stage04', 'body', 'dark', '00'),
              path_maker('croaker#1', 'stage05', 'body', 'dark', '00')]

# save_rgb_hist_accumulate([path_acc03[0]], 'result/croaker_body_dark')
temp_num = 0
for path in path_acc03:
    save_rgb_hist_accumulate([path], 'result/croaker_body_dark_%d' % temp_num, y=(0, 35000))
    temp_num += 1

'''
save_rgb_hist_accumulate(path_maker('squid#1', 'stage00', 'head', 'bright', '00'), 'result/acc#1_00_body_bright_00')
save_rgb_hist_accumulate(path_maker('squid#1', 'stage00', 'head', 'bright', '01'), 'result/acc#1_00_body_bright_01')
save_rgb_hist_accumulate(path_maker('squid#1', 'stage00', 'head', 'bright', '02'), 'result/acc#1_00_body_bright_02')
save_rgb_hist_accumulate(path_maker('squid#1', 'stage00', 'head', 'bright', '03'), 'result/acc#1_00_body_bright_03')
save_rgb_hist_accumulate(path_maker('squid#1', 'stage00', 'head', 'bright', '04'), 'result/acc#1_00_body_bright_04')
'''
'''
save_rgb_hist_accumulate(path_maker('squid#1', 'stage01', 'head', 'bright', '00'), 'result/acc#1_01_body_bright_00')
save_rgb_hist_accumulate(path_maker('squid#1', 'stage01', 'head', 'bright', '01'), 'result/acc#1_01_body_bright_01')
save_rgb_hist_accumulate(path_maker('squid#1', 'stage01', 'head', 'bright', '02'), 'result/acc#1_01_body_bright_02')
save_rgb_hist_accumulate(path_maker('squid#1', 'stage01', 'head', 'bright', '03'), 'result/acc#1_01_body_bright_03')
save_rgb_hist_accumulate(path_maker('squid#1', 'stage01', 'head', 'bright', '04'), 'result/acc#1_01_body_bright_04')
'''
'''
save_rgb_hist_accumulate(path_maker('squid#1', 'stage02', 'head', 'bright', '00'), 'result/acc#1_02_body_bright_00')
save_rgb_hist_accumulate(path_maker('squid#1', 'stage02', 'head', 'bright', '01'), 'result/acc#1_02_body_bright_01')
save_rgb_hist_accumulate(path_maker('squid#1', 'stage02', 'head', 'bright', '02'), 'result/acc#1_02_body_bright_02')
save_rgb_hist_accumulate(path_maker('squid#1', 'stage02', 'head', 'bright', '03'), 'result/acc#1_02_body_bright_03')
save_rgb_hist_accumulate(path_maker('squid#1', 'stage02', 'head', 'bright', '04'), 'result/acc#1_02_body_bright_04')
'''
