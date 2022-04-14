from mylib import *

# 이미지 HSV로 로드
# HSV에서 필터값(명도가 일정값 이상, 이하잇 값)에 걸러지는것들 v를 0으로
# HSV에서 특정 H값 사이에 있는 값을 제외한 v를 0으로
# 이미지에서 v = 0을 제외한 h의 hist 뽑기

path_list = [path_maker('croaker#1', 'stage00', 'body', 'dark', '04'),
             path_maker('croaker#1', 'stage01', 'body', 'dark', '04'),
             path_maker('croaker#1', 'stage02', 'body', 'dark', '04'),
             path_maker('croaker#1', 'stage03', 'body', 'dark', '04'),
             path_maker('croaker#1', 'stage04', 'body', 'dark', '04'),
             path_maker('croaker#1', 'stage05', 'body', 'dark', '04')]

# save_hsv_hist(path_list, 'croaker_result/stage_dark1_hsv', gray=False, y=(0, 10))


i = 0
for path in path_list:
    save_hsv_hist([path], 'croaker_result/04_dark%d_hsv'%i, color='k', y=(0, 10))
    i += 1
