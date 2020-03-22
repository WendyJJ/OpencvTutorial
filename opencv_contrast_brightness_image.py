import cv2 as cv
import numpy as np


def contrast_brightness_image(src1, a, g):
    """
    粗略的调节对比度和亮度
    :param src1:
    :param a:
    :param g:
    :return:
    """
    h, w, ch = src1.shape   #获取shape的数值， height和width, 通道

    #新建全零图片数组src2, 将height和width,类型设置为原图片的通道类型（色素全为零， 输出全黑图片）
    src2 = np.zeros([h, w, ch], src1.dtype)
    dst = cv.addWeighted(src1, a, src2, 1-a, g)    #addweighted函数说明如下
    cv.imshow("con-bri-demo", dst)


src = cv.imread("./imgs/color.jpg")
cv.namedWindow("origrinal", cv.WINDOW_NORMAL)
cv.imshow("origrnal2", src)
contrast_brightness_image(src, 1.5, 30)   #第一个1.2为对比度, 第二个为亮度数值越大越亮
cv.waitKey(0)
cv.destroyAllWindows()

"""
    addWeighted(InputArray src1, double alpha, InputArray src2, double beta, double gamma, OutputArray dst, int dtype=-1);

    一共有七个参数：
                前4个是两张要合成的图片及它们所占比例，
                第5个double gamma起微调作用，
                第6个OutputArray dst是合成后的图片，
                第七个输出的图片的类型（可选参数，默认-1）
    
    有公式得出两个图片加成输出的图片为：dst=src1*alpha+src2*beta+gamma
"""