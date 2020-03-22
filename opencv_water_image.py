import cv2 as cv
import numpy as np

"""
    分水岭分割流程： 图像——>灰度——>二值化——>距离变换——>寻找种子——>生成Marker——>分水岭变换——>输出
"""

def water_image():
    src = cv.imread("./imgs/circles2.jpg")
    print(src.shape)
    blurred = cv.pyrMeanShiftFiltering(src, 10, 100) #去除噪点

    #二值图像
    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray,0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("threshold", binary)

    # 形态操作
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    mb = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel, iterations=2)
    sure_bg = cv.dilate(mb, kernel, iterations=3)
    cv.imshow("morphologyEX", sure_bg)

    # 距离变换
    dist = cv.distanceTransform(mb, cv.DIST_L2, 3)
    dist_output = cv.normalize(dist, 0, 1.0, cv.NORM_MINMAX)
    cv.imshow("normalize", dist_output*70)

    # 寻找种子
    ret, surface = cv.threshold(dist, dist.max()*0.6, 255, cv.THRESH_BINARY)
    cv.imshow("surface", surface)

    surface_fg = np.uint8(surface)
    unknown = cv.subtract(sure_bg, surface_fg)
    ret, markers = cv.connectedComponents(surface_fg)
    print(ret)

    # watershed transfrom
    markers += 1
    markers[unknown == 255] = 0
    markers = cv.watershed(src, markers=markers)
    src[markers == -1] = [0, 0, 255]
    cv.imshow("water result", src)

src = cv.imread("./imgs/circles2.jpg")
cv.imshow("origrinal", src)
water_image()
cv.waitKey(0)
cv.destroyAllWindows()
