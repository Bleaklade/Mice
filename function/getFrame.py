import cv2
import numpy

def outP(str,img):
    cv2.imshow(str, img)
    k = cv2.waitKey(0)
    if k == 27:         # wait for ESC key to exit
        cv2.destroyAllWindows()


def getFrame(frame):
    frame1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    outP('1',frame1)
    frame2 = cv2.equalizeHist(frame1)
    outP('2',frame2)
    frame3 = cv2.adaptiveThreshold(frame2, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 7, 0)
    outP('3',frame3)
    frame4 = cv2.GaussianBlur(frame3,(5,5),0)
    outP('4',frame4)
    kernel_2 = numpy.ones((9,9),dtype=numpy.uint8)
    frameg = cv2.morphologyEx(frame4,cv2.MORPH_BLACKHAT,kernel_2)
    outP('5',frame5)
    return(frame5)

video = cv2.VideoCapture("G1.mp4")
success, frame = video.read()
head=getFrame(frame)

