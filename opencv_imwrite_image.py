# -*- coding: utf-8 -*-
"""
@Time ： 2019/12/1 23:10
@Auth ： WJJ
@File ：opencv_numpy_img.py
@IDE ：PyCharm
@Motto：Don't forget what you started out with and stick to it(Always Be Coding)

"""
import cv2 as cv
import numpy as np


def get_img_info(image):
    """
    输出图片属性
    :return:
    """
    print(type(image)) # 显示图片属性, numpy类型的数组
    print(image.shape) # 图片矩阵的shape属性表示图片的大小, shape会返回tuple元组,
                       # 第一个元素表示矩阵行数
                       # 第二个元素表示矩阵列数
                       # 第三个元素是3, 表示像素值由光的三原色组成
    print(image.size)  # 图片的大小
    print(image.dtype) # 图片类型
    pixel_data = np.array(image)
    print(pixel_data)  #图片矩阵

if __name__ == '__main__':
    src = cv.imread(r"D:\project\OpencvTutorial\images\panda.jpg")
    cv.namedWindow("panda", cv.WINDOW_NORMAL)
    cv.imshow("panda", src)
    get_img_info(src)
    cv.imwrite(r"D:\project\OpencvTutorial\images\panda_copy.jpg", src) # 图片保存位置
    cv.waitKey(0)
    cv.destroyAllWindows()