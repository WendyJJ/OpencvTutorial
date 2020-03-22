import cv2 as cv

"""
    准备工作：找到分类器：

    方法：安装opencv软件包，或者把此文件放到根目录 
    
    1.用pip安装的opencv不带分类器，所以要下载完整版的，可去官网下载安装，分类器位置在
    
    opencv\build\etc\haarcascades\haarcascade_frontalface_alt_tree.xml
    官网地址:https://sourceforge.net/projects/opencvlibrary/

    2.或者直接下载此文件把它放到根目录就行
    
"""


def face_image(image):
    """
    人脸检测
    :param iamge:
    :return:
    """
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    face_detector = cv.CascadeClassifier(r"D:\opencv\build\etc\haarcascades\haarcascade_frontalface_alt_tree.xml") #绝对路径
    faces = face_detector.detectMultiScale(gray, 1.02, 5)
    for x, y, w, h in faces:
        cv.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)
    cv.imshow("result", image)


def camera_face_image(image):
    """
    摄像头人脸检测
    :param image:
    :return:
    """
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    face_detector = cv.CascadeClassifier(
        r"D:\opencv\build\etc\haarcascades\haarcascade_frontalface_alt_tree.xml")  # 绝对路径
    faces = face_detector.detectMultiScale(gray, 1.02, 5)
    for x, y, w, h in faces:
        cv.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv.imshow("result", image)


capture = cv.VideoCapture(0)
while(True):
    ret, frame = capture.read()
    frame = cv.flip(frame, 1)
    face_image(frame)
    if cv.waitKey(50) == 27:    # 键盘输入q退出窗口，不按q点击关闭会一直关不掉 也可以设置成其他键。
        break


# src = cv.imread("./imgs/lu.jpg")
# cv.imshow("origrinal", src)
# face_image(src)
# camera_face_image()
cv.waitKey(0)
cv.destroyAllWindows()


