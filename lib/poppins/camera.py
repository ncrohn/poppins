# camera.py

import io, time
import picamera
import cv2
import numpy as np

class VideoCamera(object):
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        self.video = cv2.VideoCapture(0)
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('/Users/nickcrohn/Desktop/KarmiePrint.mp4')

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()

        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()