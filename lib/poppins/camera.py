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
        #self.video = cv2.VideoCapture(0)
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('/Users/nickcrohn/Desktop/KarmiePrint.mp4')
        self.__stream = io.BytesIO()
        self.__camera = picamera.PiCamera()
        self.__camera.start_preview()
        time.sleep(2)

    def get_frame(self):

        self.__camera.capture(self.__stream, format='jpeg')
        # Construct a numpy array from the stream
        data = np.fromstring(self.__stream.getvalue(), dtype=np.uint8)

        image = cv2.imdecode(data, 1)
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        ret, jpeg = cv2.imencode('.jpg', image[:, :, ::-1])
        return jpeg.tobytes()