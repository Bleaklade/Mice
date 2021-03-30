'''
作用：
    1、调试函数getFrame用代码

输入：视频文件

输出：格式为mp4,基本参数与原视频相同，背景被消除的视频

'''

import cv2
import numpy

'''
    函数作用：对提取到的每一帧进行处理
    处理过程：转灰度图->直方图均衡化->自适应二值化->高斯噪声模糊->黑帽处理（形态学）
    输出：最终经过黑帽处理的图像，直接将处理过的当前帧输出视频文件，并返回该帧图像
'''
def outP(str,img):
    cv2.imshow(str, img)
    k = cv2.waitKey(0)
    if k == 27:         # wait for ESC key to exit
        cv2.destroyAllWindows()

'''
    函数作用：对提取到的每一帧进行处理
    处理过程：转灰度图->直方图均衡化->自适应二值化->高斯噪声模糊->黑帽处理（形态学）
    每次处理都显示当前处理得到的图片，按Esc则显示下一张图片
    输出：最终经过黑帽处理的图像，直接将处理过的当前帧输出视频文件，并返回该帧图像

    存在问题：
        1、显示时总是无法显示大图
'''
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

