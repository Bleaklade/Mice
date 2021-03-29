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