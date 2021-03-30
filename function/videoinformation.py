'''
作用：
	1、用openCV读入视频，并获取视频的帧率、总帧数以及画面大小信息，并实时显示视频的时间、帧索引、帧率及总帧数信息
	2、输出含有上述信息的新视频

输入：视频文件

输出：格式为mp4,基本参数与原视频相同，背景被消除的视频

'''




import cv2

video = cv2.VideoCapture("test.mp4")# 在此可更改输入视频名字，需要注意视频需存放在代码所在目录下
fps = video.get(cv2.CAP_PROP_FPS)
frameCount = video.get(cv2.CAP_PROP_FRAME_COUNT)
size = (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))

videoWriter = cv2.VideoWriter('trans.mp4', cv2.VideoWriter_fourcc(*'MP4V'), fps, size)  )# 在此可更改输出视频名字、输出格式、帧率、图像大小等
success, frame = video.read()  
index = 1
while success :  
	cv2.putText(frame, 'fps: ' + str(fps), (0, 200), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,0,255), 5)
	cv2.putText(frame, 'count: ' + str(frameCount), (0, 300), cv2.FONT_HERSHEY_SIMPLEX,2, (255,0,255), 5)
	cv2.putText(frame, 'frame: ' + str(index), (0, 400), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,0,255), 5)
	cv2.putText(frame, 'time: ' + str(round(index / 24.0, 2)) + "s", (0,500), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,0,255), 5)
	cv2.imshow("new video", frame)
	cv2.waitKey(int(1000 / fps))# 如果觉得输出前的显示过程太漫长，可以更改这里的每帧显示后的暂停时间，或直接注释这一句
	videoWriter.write(frame)
	success, frame = video.read()
	index += 1

video.release()