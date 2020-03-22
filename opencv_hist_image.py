from matplotlib import pyplot as plt
import cv2 as cv


"""
   一：  绘制图片的直方图
"""
def hist_image(image):
    """
    绘制图片的直方图
    :param image:
    :return:
    """
    color = ("blue", "green", "red")
    for i, color in enumerate(color):
        hist = cv.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist, color = color)
        plt.xlim([0, 256])

    plt.show()

"""
    二：直方图应用
    直方图均衡化： 提升对比度的两种方法：默认，自定义
"""
def equalHist_image(image):
    """
    提升对比度（默认提升），只能是灰度图像
    :param image:
    :return:
    """
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imshow("origrinal", gray) # 因为只能处理灰度图像，所以输出原图的灰度图像用于对比
    dst = cv.equalizeHist(gray)
    cv.imshow(" default_processing", dst)


def clahe_image(image):
    """
    对比度限制
    :param image:
    :return:
    """
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(4, 4)) #clipLimit 是对比度的大小   tileGridSize 每次处理块的大小
    dst = clahe.apply(gray)
    cv.imshow("custom", dst)

src = cv.imread("./imgs/fangzhou.jpg")
cv.namedWindow("origrinal", cv.WINDOW_NORMAL)
cv.imshow("origrinal", src)

# hist_image(src) # 绘制图片直方图
equalHist_image(src) #直方图应用(默认处理方法)
clahe_image(src)     #直方图应用（自定义处理方法）

cv.waitKey(0)
cv.destroyAllWindows()