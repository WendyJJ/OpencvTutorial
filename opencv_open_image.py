import cv2 as cv

"""
    图像的开闭操作
    作用： 删除图像的小的干扰项
"""


def open_image(image):
    """
    图像的开闭操作
    :param image:
    :return:
    """
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    net, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("threshold", binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5,5))
    binary = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel)
    cv.imshow("open", binary)



def close_image(image):
    """
    闭区间
    :param image:
    :return:
    """
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    binary = cv.morphologyEx(binary, cv.MORPH_CLOSE, kernel)
    cv.imshow("close", binary)


src = cv.imread("./imgs/gu0.jpg")
cv.imshow("origrinal", src)
open_image(src)
close_image(src)
cv.waitKey(0)
cv.destroyAllWindows()