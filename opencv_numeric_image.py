# -*- coding=GBK -*-
import cv2 as cv
import numpy as np



def numeric_image(src11, src22):
    """
        一： 数值运算
        opencv自带图片色素的处理函数：
        相加： add()
        相减： subtract()
        相乘： numltiply()
        相除： divide()
        原理: 通过获取两张（一次只能两张）个图片的同一个位置的色素值来实现运算
        运算的要求： 两张图片的shape要一样
    """

    src = cv.add(src11, src22)  #相加
    cv.imshow("add", src)

    src = cv.subtract(src11, src22)
    cv.imshow("subtract", src)

    src = cv.multiply(src11, src22)
    cv.imshow("multiply", src)

    src = cv.divide(src11, src22)
    cv.imshow("divide", src)



def logicl_image(src11, src22):
    """
    逻辑运算： 与或非的操作
    :param src11:
    :param src22:
    :return:
    """
    src = cv.bitwise_and(src11, src22)    #与  两张图片同一位置的色素两个值均不为零的才会有输出
    cv.imshow("and", src)

    src = cv.bitwise_or(src11, src22)     #或   两张图片同一位置的色素两个值不全为零的才会输出
    cv.imshow("or", src)

    src = cv.bitwise_not(src11, src22)    #非    对一张图片操作  取反
    cv.imshow("not", src)
src1 = cv.imread("./imgs/linux.jpg")
src2 = cv.imread("./imgs/window.jpg")
cv.imshow("origrinal1", src1)
cv.imshow("origrinal2", src2)

# numeric_image(src1, src2)   # 数值运算
logicl_image(src1, src2)
cv.waitKey(0)
cv.destroyAllWindows()