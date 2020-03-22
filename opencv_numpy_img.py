# -*- coding=GBK -*-

"""
@Time ： 2019/12/1 23:10
@Auth ： WJJ
@File ：opencv_numpy_img.py
@IDE ：PyCharm
@Motto：Don't forget what you started out with and stick to it(Always Be Coding)

"""

"""
    python实现opencv: numpy操作数组输出图片
"""

import cv2 as cv
import numpy as np

def access_pixles(image):
    """
    numpy 数组操作
    :param image:
    :return:
    """

    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    channel = image.shape[2]

    print("width: {}, height: {}, channel: {}".format(width, height, channel))

    for row in range(height):
        for col in range(width):
            for c in range(channel):
                pv = image[row, col, c]
                image[row, col, c] = 255 - pv
    cv.imshow("edit", image)

# if __name__ == '__main__':
#     src = cv.imread(r"D:\project\OpencvTutorial\images\panda.jpg")
#     cv.imshow("befor", src)
#     t1 = cv.getTickCount() # 毫秒级的记时函数, 没记录了系统启动以来的时间毫秒
#     access_pixles(src)
#     t2 = cv.getTickCount()
#     time = (t2 - t1)*1000/cv.getTickFrequency() # getTickFrequency 用于返回CPU的频率, 则是美妙的计时间周期数
#     print("time: {}".format(time))  # 输出运行时间
#     cv.waitKey(0)
#     cv.destroyAllWindows()


def create_image_zeros():
    """
        自定义一张多通道的图片
        用到函数: zeros 和ones
    """
    img = np.zeros([400, 400, 3], np.uint8) # zeros: double类零矩阵, 创建400*400 3个通道的矩阵图像,
                                            # 参数是classname 为uint8
    img[:, :, 0] = np.ones([400, 400])*255  # ones([400, 400]) 是创建一个400*400的全1矩阵, *255即全255矩阵,
                                            # 并将这个矩阵的值赋给img的第一维
    img[:, :, 1] = np.ones([400, 400])*255  # 第二维全是255
    img[:, :, 2] = np.ones([400, 400])*255  # 第三维全是255
    cv.imshow("my_image", img)            # 输出一张400*400的白色图片(255, 255, 255): 蓝(B), 绿(G), 红(R)


# if __name__ == '__main__':
#     create_image_zeros()
#     cv.waitKey(0)
#     cv.destroyAllWindows()


def create_image_ones():
    """
        自定义一张单通道的图片
    """

    img = np.ones([400, 400, 1], np.uint8)
    img = img * 127
    cv.imshow("my_image", img)

# if __name__ == '__main__':
#     create_image_ones()
#     cv.waitKey(0)
#     cv.destroyAllWindows()


def inverse(image):
    """
    调用库函数实现像素取反 ,调用bitwise_not函数运行时间非常快
    :param image:
    :return:
    """

    dst = cv.bitwise_not(image)
    cv.imshow("inverse", dst)

if __name__ == '__main__':
    src = cv.imread(r"D:\project\OpencvTutorial\images\panda.jpg")
    cv.namedWindow("befor", cv.WINDOW_NORMAL)
    cv.imshow("befor", src)
    t1 = cv.getTickCount()
    inverse(src)
    t2 = cv.getTickCount()
    time = (t2 - t1)*1000/cv.getTickFrequency()
    print("time: {}".format(time))
    cv.waitKey(0)
    cv.destroyAllWindows()