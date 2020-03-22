import cv2 as cv
import numpy as np


"""
    圆检测
    一.霍夫圆检测对噪声比较敏感，所以首先要对图像做中值滤波
    二. 基于效率考虑， Opencv中实现的霍夫变换圆检测是基于图像梯度的实现，分为2步
        1.检测边缘，发现可能的圆心
        2.基于第一步的基础从候选圆心开始计算最佳半径大小
    
"""

def circles_image(image):
    """
        圆检测
    """
    dst = cv.pyrMeanShiftFiltering(image, 10, 100) # 消除噪声
    cimage = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)
    circles = cv.HoughCircles(cimage, cv.HOUGH_GRADIENT, 1, 20, param1 = 50, param2= 30, minRadius= 0, maxRadius=0)
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        cv.circle(image, (i[0], i[1]), i[2], (0, 0, 255), 2)
        cv.circle(image, (i[0], i[1]), 2, (255, 0, 255), 2)

    cv.imshow("circles", image)


src = cv.imread("./imgs/circles3.png")
cv.imshow("origrinal", src)

circles_image(src)

cv.waitKey(0)
cv.destroyAllWindows()