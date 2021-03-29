import cv2
import numpy

def getFrame(frame1,head):

    frame2 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    
    frame3 = cv2.equalizeHist(frame2)
    
    #frame4 = cv2.adaptiveThreshold(frame3, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 7, 5)
    
    #frame5 = cv2.GaussianBlur(frame4,(3,3),0)
    
    kernel_2 = numpy.ones((5,5),dtype=numpy.uint8)
    frame6 = cv2.morphologyEx(frame3,cv2.MORPH_BLACKHAT,kernel_2)

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

#ret, head = cv2.threshold(frame_GRAY, 9, 255, cv2.THRESH_BINARY_INV)
while success :  
    temp = getFrame(frame,head)
    success, frame = video.read()

video.release()

