'''
作用：
    1、用openCV内置函数直接进行背景消除

输入：视频文件

输出：格式为mp4,基本参数与原视频相同，背景被消除的视频

'''

import numpy as np
import cv2

video = cv2.VideoCapture("G1.mp4")
fps = video.get(cv2.CAP_PROP_FPS)
frameCount = video.get(cv2.CAP_PROP_FRAME_COUNT)
size = (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))
video.release()

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('C:\Python\code\Result\out1.mp4',fourcc, fps,size,False)

cap = cv2.VideoCapture('G1.mp4')
ret = 1 

fgbg = cv2.createBackgroundSubtractorMOG2()
index = 0

while(ret):
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)

    if index/frameCount >=0.1:
        index=0
        print('|***|')
    
    index += 1

    out.write(fgmask)
cap.release()