# -*- coding: utf-8 -*-
"""
@Time ： 2019/12/1 23:10
@Auth ： WJJ
@File ：opencv_numpy_img.py
@IDE ：PyCharm
@Motto：Don't forget what you started out with and stick to it(Always Be Coding)

"""
import cv2 as cv


def video_demo():
    """
    打开摄像头获取图片
    :return:
    """
    capture = cv.VideoCapture(0)    # 打开摄像头, 0代表是设备id, 如果有多个摄像头,可以设置其他数值
    while True:
        ret, frame = capture.read() # 读取摄像头, 它q能返回两个参数,
                                    # 第一个是bool型的ret, 其值为True或False,其代表有没有读到图片;
                                    # 第二个参数是frame, 是当前截取一帧的图片
        frame = cv.flip(frame, 1)   # 翻转 0: 上下颠倒 大于0水平颠倒 小于180旋转
        cv.imshow("vidow", frame)
        # if cv.waitKey(10) & 0xFF == ord('q'): # 键盘输入 q退出窗口, 不按q点击关闭会一直关不掉, 也可以自定义设置成其他键
        if cv.waitKey(40)== 27:
            break


    # 注释
    """
        1.  指定按键盘键值关掉窗口,或者是 cv.waitKey(40) == 27 按Esc关闭窗口
        
        2.  函数: VideoCapture(0)
            打开摄像头, 0代表的是设备ID, 如有多个摄像头,可以设置其他的数值
            也可以是视频文件地址, 调用视频文件, 如果要播放需设置帧的循环.
            
        3.  函数: read()
            读取摄像头, 它能返回两个参数,第一个参数是boot型的ret,或False, 代表有没有读到图片;
            第二个参数是frame, 是截取一帧的图片
            
        4.  函数: frame = cv.flip(frame, 1)
            表示翻转
                0: 上下颠倒
                大于0: 水平颠倒
                小于0: 180旋转
    """
if __name__ == '__main__':
    video_demo()
    cv.destroyAllWindows()
