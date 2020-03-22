import cv2 as cv
from PIL import Image
import pytesseract



def recognize_text(image):
    dst = cv.GaussianBlur(image, (3, 3), 0)
    gray = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (1, 3))
    binl = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (2, 1))
    open_out = cv.morphologyEx(binl, cv.MORPH_OPEN, kernel)
    cv.bitwise_not(open_out, open_out)   #背景变白色
    cv.imshow("transform", open_out)
    textImage = Image.fromarray(open_out)
    text = pytesseract.image_to_string(textImage)
    print("success: "+str(text))



src = cv.imread("./imgs/yan4.jpg")
cv.imshow("origrinal", src)

recognize_text(src)
cv.waitKey(0)
cv.destroyAllWindows()