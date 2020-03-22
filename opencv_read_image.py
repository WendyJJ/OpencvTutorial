# -*- coding: utf-8 -*-
"""
@Time ： 2019/12/1 23:10
@Auth ： WJJ
@File ：opencv_numpy_img.py
@IDE ：PyCharm
@Motto：Don't forget what you started out with and stick to it(Always Be Coding)

"""
import cv2 as cv


src = cv.imread(r"D:\project\OpencvTutorial\images\panda.jpg")
cv.namedWindow("1",0)
cv.imshow("panda", src)
cv.waitKey(0)
cv.destroyAllWindows()



#备注
"""
    1. imread(const String & filename, int flags) 读取图片
    第一个参数是图片地址: "\\", "\" 和"/" ,"//"
    第二个参数是图片读取方式: 默认正常读取方式,如果为0则为灰度图, 为2也是灰度图
    
    2. cv.NameWindow(const char* name, int flags) 创建窗口,不写也可以show图片
    第一个参数是定义窗口的名称 设置中文时.py文件上加 #-*-coding=GBK-*-
    第二个参数是窗口显示方式:
        为0或cv.WINDOW_NORMAL: 可以改变窗口大小
        不写或cv.WINDOW_AUTOSIZE: 则不可以改变大小
    
    3. imshow(const string & winname, InputArray mat) 显示图片显示窗口 
    第一个参数: 窗口名称, 如果上面有NameWindow()函数,这个名称要与它一样,
    不然不会出现两个窗口,一个是NameWindow的空白窗口,一个是imshow()的图片窗口.
    
    第二个参数:要显示的的图片.
    如果窗口是用CV_WINDOW_AUSTSIZE(默认值)标志创建的,那么显示图像的原始大小.否则,将图片进行缩放
    以适合的窗口.而imshow()函数缩放图像,取决于图像的深度
    
    4.waitKey(k) 窗口显示时间, 单位:毫秒
        k=0: (也可以是小于0的数值)一直显示,键盘上按下一个数字即会消失
        k >0: 显示多少毫秒
    5.  destroyAllWindows(): 删除建立的全部窗口,释放资源.
"""