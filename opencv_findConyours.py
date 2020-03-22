# -*- coding: utf-8 -*-
"""
@Time ： 2019/12/1 23:10
@Auth ： WJJ
@File ：opencv_numpy_img.py
@IDE ：PyCharm
@Motto：Don't forget what you started out with and stick to it(Always Be Coding)

"""
import numpy as np
import cv2 as cv

def edge_demo(image):

    dst = cv.GaussianBlur(image, (3, 3), 0)       # 高斯模糊去噪
    gray = cv.cvtColor(dst, cv.COLOR_RGB2GRAY)
    # X Grodient
    xgrad = cv.Sobel(gray, cv.CV_16SC1, 1, 0)

    # Y Grodient
    ygrad = cv.Sobel(gray, cv.CV_16SC1, 0, 1)

    #edge
    edge_output = cv.Canny(gray, 50, 100)
    cv.imshow("Canny Edge", edge_output)

    return edge_output

def contours_demo(image):
    # 第一种方法
    # dst = cv.GaussianBlur(image, (3, 3), 0)  # 高斯模糊去噪
    # gray = cv.cvtColor(dst, cv.COLOR_RGB2GRAY)
    # ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)  # 用大律法、全局自适应阈值方法进行图像二值化
    # cv.imshow("binary image", binary)

    # 第二种方法
    binary = edge_demo(image)
    # 旧版
    # cloneImage, contours, heriachy = cv.fi ndContours(binary,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
    # 新版
    contours, hierarchy = cv.findContours(binary, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    for i, countour in enumerate(contours):
        cv.drawContours(image, contours, i, (0, 0, 255), 2)
        print(i)
    cv.imshow("detect contours", image)

    for i, contour in enumerate(contours):
        cv.drawContours(image, contours, i, (0, 0, 255), -1) # 填充轮廓
    cv.imshow("pcontours", image)

if __name__ == '__main__':
    print("-----------python opencv image--------------------")
    src = cv.imread(r"D:\YD_wjj\gongzuojiaojie2\yd_files\OCRParse\OcrParse\app\images\1000_555_pan.jpg")
    cv.namedWindow("input image", cv.WINDOW_AUTOSIZE) #设置为WINDOW_NORMAL可以任意缩放
    cv.imshow("input image", src)
    contours_demo(src)
    cv.waitKey(0)
    cv.destroyAllWindows()