"""
作用：
    1、进一步了解普通二值化的使用代码
    2、读入视频第一帧，然后让阈值从0-255进行二值化处理，将每张图像作为一帧合成新视频

输入：视频文件

输出：不同阈值下第一帧二值化图像的合成视频，格式avi，帧率10，图像大小与原视频相同

"""

import cv2

#output is the threshold image of the first frame of video for all the threshold from 0 to 255

video = cv2.VideoCapture("G1.mp4")
fps = video.get(cv2.CAP_PROP_FPS)
frameCount = video.get(cv2.CAP_PROP_FRAME_COUNT)
size = (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))
outputFile='start2\\'

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('testthreshold.avi',fourcc, 10,size,False)


success=1
index = 0
head=0
success, frame = video.read()
frame_GRAY = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
for iter in range(0,256):
    ret, binary = cv2.threshold(frame_GRAY, iter, 255, cv2.THRESH_BINARY_INV)
    outputName = outputFile+str(int(iter))+'.jpg'
    out.write(binary)
video.release()

