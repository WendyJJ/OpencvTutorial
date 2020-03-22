import cv2 as cv
import numpy as np


def incise_image(src1):
    """
    截取图片中的指定区域在指定区域添加某一图片
    :param src1:
    :return:
    """

    src2 = src1[20:90, 200:360]     #截取第5-90行的第500-630列的区域
    cv.imshow("incise", src2)

    src1[20:90, 200:360] = src2  # 指定位置填充，大小要一样才能填充
    cv.imshow("compound ", src1)


src = cv.imread("./imgs/black.jpg")
cv.imshow("origrinal", src)
incise_image(src)

cv.waitKey(0)
cv.destroyAllWindows()