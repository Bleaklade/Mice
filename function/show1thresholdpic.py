import cv2

video = cv2.VideoCapture("G1.mp4")
fps = video.get(cv2.CAP_PROP_FPS)
frameCount = video.get(cv2.CAP_PROP_FRAME_COUNT)
size = (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))
outputFile='Picout_dg\\'


success, frame = video.read()  
index = 1
frame_GRAY = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(frame_GRAY, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("binary ", binary)
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
     cv2.destroyAllWindows()

