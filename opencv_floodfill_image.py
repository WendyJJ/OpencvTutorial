import cv2 as cv
import numpy as np


def fill_image(image):
    """
    指定颜色替换
    :param image:
    :return:
    """

    copyImage = image.copy()
    h, w = image.shape[:2]      #读取图像的宽和高
    mask = np.zeros([h+2, w+2], np.uint8)     # 新建图像矩阵   +2是官方函数要求
    cv.floodFill(copyImage, mask, (0, 80), (0, 100, 255), (100, 100, 50),(50, 50, 50), cv.FLOODFILL_FIXED_RANGE)
    cv.imshow("fill", copyImage)

def fill2_image():
    image = np.zeros([200, 200, 3], np.uint8)

    cv.imshow("origrinal", image)
    mask = np.ones([202, 202, 1], np.uint8)
    mask[100:150, 100:150] = 0

    cv.floodFill(image, mask, (100, 100), (0, 255, 255), cv.FLOODFILL_MASK_ONLY)
    cv.imshow("fill", image)



src = cv.imread("./imgs/black.jpg")
cv.imshow("origrinal", src)
# fill_image(src)  #指定颜色替换
fill2_image()

cv.waitKey(0)
cv.destroyAllWindows()

"""
    floodFill函数： 漫水填充算法
    官方定义：floodFill(InputOutputArray image, Point seedPoint, Scalar newVal, Rect* rect=0, Scalar loDiff=Scalar(), 
            Scalar upDiff=Scalar(), int flags=4)
            
            floodFill(1.操作的图像, 2.掩模, 3.起始像素值, 4. 填充的颜色, 5.填充颜色的低值, 6.填充颜色的高值, 7.填充的方法)
            
            参数5, 填充的颜色的低值：(参数3 - 参数5)
            参数6, 填充颜色的高值： (参数3 + 参数5)
            参数4, 则是两个数值之间的色素替换为参数4的颜色
            参数7, 填充的方法， 彩色图像一般是FLOODFILL_FIXED_RENGE 指定颜色填充
                   或FLOOFILL_MASK_ONLY, mask的指定位置为零时才填充，不为零不填充
               
"""




