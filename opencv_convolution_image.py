import cv2 as cv
import numpy as np

"""
    利用卷积对图像模糊处理
    均值, 中值, 取周围所有像素的均值, 中值来设置这个像素的大小
    涉及边界的问题：填充方法有: 补零, 边界复制, 块复制, 镜像复制等方法 
    
    1. 均值模糊函数 blur(): 定义: blur(src,ksize,dst=None, anchor=None, borderType=None)
        定义是有5个参数，最后3个参数均为None, 相当于2个参数
        src: 要处理的图像
        ksize: 周围关联的像素的范围：代码中(5, 5) 是9*5的大小，计算这些范围内的均值来确定中心位置的大小
        
    2. 中值模糊函数medianBlur() 定义： medianBlur(src, ksize, dst=None)
        ksize与Blur()函数不同，不是矩阵，则是一个数字，例如5，则表示 5*5的方阵
        
    3. 高斯平滑函数GaussianBlur() 定义：GaussianBlur(src, ksize, sigmaY=None, borderType=None)
        sigmaX： 标准差
    
    4. 双边滤波函数bilateralFilter() 定义： bilateralFilter(src, d, sigmaColor, sigmaSpace, dst=None, borderType=None)
        d: 领域直径
        sigmaColor: 颜色标准差
        sigmaSpace: 空间标准差
        
    5. 自定义模糊 filter2D()： 定义为filter2D(src, ddepth, kernel)
        ddepth: 深度， 输入值为-1时，目标图像和原图像深度保持一致
        kernel: 卷积核，一个单通道浮点型矩阵
        修改kernel矩阵即可实现不同的模糊图像
"""

def dim_image(src1):
    """
    实现模糊
    :return:
    """
    # 均值模糊
    src2 = cv.blur(src1, (5, 5))
    cv.imshow("blur", src2)

    # 中值模糊
    src2 = cv.medianBlur(src1, 5)
    cv.imshow("medianBlur", src2)

    # 高斯模糊
    src2 = cv.GaussianBlur(src1, (5, 5), 2)
    cv.imshow("GaussianBlur", src2)

    # 双边模糊
    src2 = cv.bilateralFilter(src1, 5, 5, 2)
    cv.imshow("bilateralFiler", src2)


def self_image(src1):
    """
    自定义模糊
    :param src1:
    :return:
    """
    kernel1 = np.ones((5, 5), np.float)/25   #自定义矩阵，并防止数值溢出
    src2 = cv.filter2D(src1, -1, kernel1)
    cv.imshow("self_filter", src2)
    kernel2 = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32)
    src2 = cv.filter2D(src1, -1, kernel2)
    cv.imshow("self_array", src2)


src = cv.imread("./imgs/tie.jpg")
cv.namedWindow("origrinal", cv.WINDOW_NORMAL)
cv.imshow("origrinal", src)
# dim_image(src)
self_image(src)
cv.waitKey(0)
cv.destroyAllWindows()

