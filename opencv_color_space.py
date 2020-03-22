# -*- coding: utf-8 -*-
"""
@Time ： 2019/12/2 22:48
@Auth ： WJJ
@File ：opencv_color_space.py
@IDE ：PyCharm
@Motto：Don't forget what you started out with and stick to it(Always Be Coding)

"""

"""
    python实现opencv学习: 色彩空间转换
"""


# 一: 调用转换函数实现图像色彩空间转换
import cv2 as cv
import numpy as np


def color_space_demo(image):
    """
    色彩空间的转换
    HSV 色彩空间说明:
    H: 0-180 S: 0-255 V: 0-255
    :param image:
    :return:
    """
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY) # RGB转换为gray
    cv.imshow("gray", gray)
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)   #rgb转换为HSV
    cv.imshow("hsv", hsv)
    yuv = cv.cvtColor(image, cv.COLOR_BGR2YUV)   #RGB转换为yuv
    cv.imshow("yuv", yuv)

# src = cv.imread(r"D:\project\OpencvTutorial\images\panda.jpg")
# cv.namedWindow("original", cv.WINDOW_NORMAL)
# cv.imshow("original", src)
# color_space_demo(src)
# cv.waitKey(0)
# cv.destroyAllWindows()


# 二: 色彩空间转换,利用inrange函数过滤视频中的颜色,实现跟踪某一颜色

def nextrace_object_demo():
    capture = cv.VideoCapture(r"D:\project\OpencvTutorial\images\25f4c12c20ee0244c25409f3b61f7cc9.mp4") #导入视频
    while True:
        ret, frame = capture.read()
        if ret == False:
            break
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV) # 转换色彩空间hsv
        #设置白色的范围, 跟踪视频中的白色
        lower_hsv = np.array([0, 0, 221])   #设置过滤的颜色低值
        upper_hsv = np.array([180, 30, 255]) #设置过滤的颜色高值

        mask = cv.inRange(hsv, lower_hsv, upper_hsv)  # 调节图像颜色信息(H), 饱和度(S), 亮度(V)区间,选择白色区域
        cv.imshow("video", frame)
        cv.imshow("mask", mask)

        if cv.waitKey(40) == 27:
            break

# nextrace_object_demo()
# cv.waitKey(0)
# cv.destroyAllWindows()


# 三: 通道分离,合并,修改某一通道

"""
    split() 将色彩图像分割成3个通道
    merge() 通道合并
"""


src = cv.imread(r"D:\project\OpencvTutorial\images\panda.jpg")
cv.namedWindow("original", cv.WINDOW_NORMAL)
cv.imshow("original", src)

#通道分离, 输出三个单通道图片
b, g, r = cv.split(src)
cv.imshow("blue", b)
cv.imshow("green", g)
cv.imshow("red", r)

# 通道合并
src = cv.merge([b, g, r])
cv.imshow("merge", src)

# 修改某个通道的值
src[:, :, 2] = 100
cv.imshow("one", src)

cv.waitKey(0)
cv.destroyAllWindows()
