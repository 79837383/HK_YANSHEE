#coding=utf-8
#############################################################################
		############Author: Xuyang Jie####################

		############Date: 13/03/2018######################
#############################################################################
import cv2
import time
import os
from picamera import PiCamera
from picamera.array import PiRGBArray


# Initialization
camera = PiCamera()
camera.resolution = (320,240)
camera.framerate = 40
rawCapture = PiRGBArray(camera, size = (320, 240))
time_start = time.time()
counter = 0


# Load the cascade files for detecting faces
face_cascade = cv2.CascadeClassifier("./haarcascade_frontalface_default.xml")


# Capture frames from camera
for capture in camera.capture_continuous(rawCapture,format = "bgr", use_video_port = True):
	image = capture.array

	#Frame pre-process
	grayimage = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

	#Comparison
	face = face_cascade.detectMultiScale(grayimage,scaleFactor = 2.0)

	#Mark the face
	for (x,y,w,h) in face:
		cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
		cv2.putText(image,"Found face",(x,y-2),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0),2)

    #Use Green text to show FPS at the left image corner
	counter = counter + 1
	fps = counter / ( time.time() - time_start )
	cv2.putText(image,str(fps),(15,15),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),2)

	#Show Frame
	cv2.imshow('Camera Capture',image)

	# Press 'q' to quit
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

	#Wait for next frame
	rawCapture.truncate(0)

#Close window and camera
camera.close()
cv2.destroyAllWindows()