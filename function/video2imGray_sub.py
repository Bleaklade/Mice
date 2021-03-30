"""
作用：
    1、关注了与第一帧做差后所得图像的效果
    2、读入视频，进行一定的图像处理，然后将每一帧与第一帧做差，得到图像合成为新视频

输入：视频文件

输出：与第一帧做差后所得图像的合成视频，格式avi，图像大小、帧率、时间与原视频相同

混合了较多版本代码而有点混乱

"""

import cv2

video = cv2.VideoCapture("G1.mp4")
fps = video.get(cv2.CAP_PROP_FPS)
frameCount = video.get(cv2.CAP_PROP_FRAME_COUNT)
size = (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))
outputFile='Picout_dg\\'

success, frame = video.read()  
# 每三十张噪声就会变为彩色的
index = 1
#frame_GRAY = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#before=frame_GRAY
before=frame

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('testwrite.avi',fourcc, 60.0, (1920,1080),True)

while success :  
	success, frame = video.read()
	#frame_GRAY = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	#div = frame_GRAY-before
	div = frame-before
	frameIndex=int(video.get(cv2.CAP_PROP_POS_FRAMES))
	outputName=outputFile+str(frameIndex)+'.jpg'
	#cv2.imwrite(outputName,div)
	out.write(div)
	#cv2.imwrite(outputName,frame_GRAY)
	index += 1
#	before=frame_GRAY
	before=frame

video.release()