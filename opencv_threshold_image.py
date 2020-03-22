import cv2 as cv
import numpy as np


"""
    图像二值化
    函数threshold() 参数说明
    cv.THRESH_BINARY | cv.THRESH_OTSU  #大律法， 全局自适应阈值 参数0可改为任意数字但不起作用
    cv.THRESH_BINARY | cv.THRESH_TRIANGLE # TRIANGLE法， 全局自适应阈值，参数0可改为任意数字但不起作用， 适用于单个波峰
    cv.THRESH_BINARY # 自定义阈值为150， 大于150的是白色，小于的是黑色
    cv.THRESH_TRUNC  # 截断 大于150的是改为150，小于150的保留
    cv.THRESH_TOZERO # 截断 小于150的是改为150， 大于150的保留
"""


def threshold_image(image):
    """
    图像二值化  0白色 1黑色
    全局阈值
    :param image:
    :return:
    """

    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imshow("origrinal", gray)

                                # 大律法，全局自适应阈值，参数0可改为任意数字但不起作用
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    print("threshold==", ret)
    cv.imshow("OTSU", binary)
                                # TRIANGLE法,全局自适应阈值， 参数0可改为任意数字但不起作用，适用于单个波峰
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_TRIANGLE)
    print("threshold==", ret)
    cv.imshow("TRIANGLE", binary)

                                # 自定义阈值为150， 大于150是黑色， 小于150是白色
    ret, binary = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
    print("threshold", ret)
    cv.imshow("custom", binary)
                                # 自定义阈值为150，大于150是黑色，小于150是白色
    ret, binary = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
    print("threshold", ret)
    cv.imshow("custom_inv", binary)
                                #截断， 大于150改为150， 小于150的保留
    ret, binary = cv.threshold(gray, 150, 255, cv.THRESH_TRUNC)
    print("threshold", ret)
    cv.imshow("cut1", binary)
                                # 截断， 小于150的改为150， 大于150的保留
    ret, binary = cv.threshold(gray, 150, 255, cv.THRESH_TOZERO)
    print("threshold", ret)
    cv.imshow("cut2", binary)



def local_image(image):
    """
    局部阈值
    :param image:
    :return:
    """
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imshow("origrinal", gray)
    binary1 = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 25, 10)
    cv.imshow("local1", binary1)

    binary2 = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 25, 10)  #高斯处理
    cv.imshow("local2", binary2)


def custom_image(image):
    """
    图像均值作为阈值来二值化
    :param image:
    :return:
    """

    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imshow("origrinal", gray)

    h, w = gray.shape[:2]

    m = np.reshape(gray, [1, w*h])  #化为一维数组
    mean = m.sum() / (w*h)
    print("mean: ", mean)
    ret, binary = cv.threshold(gray, mean, 255, cv.THRESH_BINARY)
    cv.imshow("threshold", binary)

src = cv.imread("./imgs/ku.jpg")
# threshold_image(src)
# local_image(src)
custom_image(src)
cv.waitKey(0)
cv.destroyAllWindows()