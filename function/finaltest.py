'''
作用：
    1、预期的最终总代码

输入：视频文件

输出：格式为mp4,基本参数与原视频相同，背景被消除的视频

存在问题：
    1、代码运行速度太慢
    2、仍然无法得到只有小鼠的视频
'''
import cv2
import numpy

'''
    函数作用：对提取到的每一帧进行处理
    处理过程：转灰度图->直方图均衡化->自适应二值化->高斯噪声模糊->黑帽处理（形态学）
    输出：最终经过黑帽处理的图像，直接将处理过的当前帧输出视频文件，并返回该帧图像
'''

def getFrame(frame1,head):

    frame2 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    
    frame3 = cv2.equalizeHist(frame2)
    
    frame4 = cv2.adaptiveThreshold(frame3, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 7, 5)
    
    frame5 = cv2.GaussianBlur(frame4,(3,3),0)
    
    kernel_2 = numpy.ones((5,5),dtype=numpy.uint8)#黑帽处理卷积核大小
    frame6 = cv2.morphologyEx(frame5,cv2.MORPH_BLACKHAT,kernel_2)

    frameout = frame6

    out.write(frameout) 
    return(frameout)


video = cv2.VideoCapture("G1.mp4")
fps = video.get(cv2.CAP_PROP_FPS)
frameCount = video.get(cv2.CAP_PROP_FRAME_COUNT)
size = (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('C:\Python\code\Result\out.mp4',fourcc, fps,size,False)

success, frame = video.read()
head = numpy.ones(size,dtype=numpy.uint8)
head = getFrame(frame,head)

#ret, head = cv2.threshold(frame_GRAY, 9, 255, cv2.THRESH_BINARY_INV)#普通二值化原本语句
while success :  
    temp = getFrame(frame,head)
    success, frame = video.read()

video.release()

