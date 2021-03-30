'''
作用：
    1、了解普通二值化的使用代码
    2、读入视频第一帧，然后显示对其进行二值化处理后的图像，按Esc结束陈旭运行

输入：视频文件

输出：无

'''
import cv2

video = cv2.VideoCapture("G1.mp4")
fps = video.get(cv2.CAP_PROP_FPS)
frameCount = video.get(cv2.CAP_PROP_FRAME_COUNT)
size = (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))


success, frame = video.read()  
index = 1
frame_GRAY = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(frame_GRAY, 127, 255, cv2.THRESH_BINARY)#177为阈值

cv2.imshow("binary ", binary)
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
     cv2.destroyAllWindows()

