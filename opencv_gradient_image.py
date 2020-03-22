import cv2 as cv



"""
    图像梯度
"""


def sobel_image(image):
    """
    图像梯度，： 索贝尔算子
    :param image:
    :return:
    """

    grad_x = cv.Sobel(image, cv.CV_32F, 1, 0)   #X方向导数
    grad_y = cv.Sobel(image, cv.CV_32F, 0, 1)   #Y方向导数
    gradx = cv.convertScaleAbs(grad_x)
    grady = cv.convertScaleAbs(grad_y)

    cv.imshow("x", gradx)   #颜色变化在水平分层
    cv.imshow("y", grady)   #颜色变化在垂直分层
    gradxy = cv.addWeighted(gradx, 0.5, grady, 0.5, 0)
    cv.imshow("addxy", gradxy)


def scharr_image(image):
    """
    scharr 算子
    图像梯度： scharr算子， 增强边缘
    :param image:
    :return:
    """
    grad_x = cv.Scharr(image, cv.CV_32F, 1, 0)   # X方向导数
    grad_y = cv.Scharr(image, cv.CV_32F, 0, 1)   # Y方向导数
    gradx = cv.convertScaleAbs(grad_x)
    grady = cv.convertScaleAbs(grad_y)
    cv.imshow("x", gradx)
    cv.imshow("y", grady)

    gradxy = cv.addWeighted(gradx, 0.5, grady, 0.5, 0)
    cv.imshow("xy", gradxy)


def lapalian_image(image):
    """
    拉普拉斯算子
    :param image:
    :return:
    """
    dst = cv.Laplacian(image, cv.CV_32F)
    lpls = cv.convertScaleAbs(dst)
    cv.imshow("lapalian", lpls)



src = cv.imread("./imgs/gu0.jpg")
cv.imshow("origrinal", src)

# sobel_image(src)  #索贝尔算子
# scharr_image(src) #scharr 算子
lapalian_image(src) #拉普
cv.waitKey(0)
cv.destroyAllWindows()


