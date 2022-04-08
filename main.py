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




save_rgb_hist(path_maker('squid#1', 'stage00', 'head', 'bright', '00'), 'result/#1_00_body_bright_00')
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


'''
save_rgb_hist_accumulate(path_maker('squid#1', 'stage00', 'body', 'bright', '00'), 'result/acc#1_00_body_bright_00')
save_rgb_hist_accumulate(path_maker('squid#1', 'stage00', 'body', 'bright', '01'), 'result/acc#1_00_body_bright_01')
save_rgb_hist_accumulate(path_maker('squid#1', 'stage00', 'body', 'bright', '02'), 'result/acc#1_00_body_bright_02')
save_rgb_hist_accumulate(path_maker('squid#1', 'stage00', 'body', 'bright', '03'), 'result/acc#1_00_body_bright_03')
save_rgb_hist_accumulate(path_maker('squid#1', 'stage00', 'body', 'bright', '04'), 'result/acc#1_00_body_bright_04')
'''
'''
save_rgb_hist_accumulate(path_maker('squid#1', 'stage01', 'body', 'bright', '00'), 'result/acc#1_01_body_bright_00')
save_rgb_hist_accumulate(path_maker('squid#1', 'stage01', 'body', 'bright', '01'), 'result/acc#1_01_body_bright_01')
save_rgb_hist_accumulate(path_maker('squid#1', 'stage01', 'body', 'bright', '02'), 'result/acc#1_01_body_bright_02')
save_rgb_hist_accumulate(path_maker('squid#1', 'stage01', 'body', 'bright', '03'), 'result/acc#1_01_body_bright_03')
save_rgb_hist_accumulate(path_maker('squid#1', 'stage01', 'body', 'bright', '04'), 'result/acc#1_01_body_bright_04')

'''
'''
save_rgb_hist_accumulate(path_maker('squid#1', 'stage02', 'body', 'bright', '00'), 'result/acc#1_02_body_bright_00')
save_rgb_hist_accumulate(path_maker('squid#1', 'stage02', 'body', 'bright', '01'), 'result/acc#1_02_body_bright_01')
save_rgb_hist_accumulate(path_maker('squid#1', 'stage02', 'body', 'bright', '02'), 'result/acc#1_02_body_bright_02')
save_rgb_hist_accumulate(path_maker('squid#1', 'stage02', 'body', 'bright', '03'), 'result/acc#1_02_body_bright_03')
save_rgb_hist_accumulate(path_maker('squid#1', 'stage02', 'body', 'bright', '04'), 'result/acc#1_02_body_bright_04')
'''
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