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

        # Create the in-memory stream
        stream = io.BytesIO()
        with picamera.PiCamera() as camera:
            camera.start_preview()
            time.sleep(2)
            camera.capture(stream, format='jpeg')
            # Construct a numpy array from the stream
            self.__data = np.fromstring(stream.getvalue(), dtype=np.uint8)

    def get_frame(self):
        image = cv2.imdecode(self.__data, 1)
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        ret, image = cv2.imencode('.jpg', image[:, :, ::-1]
        return image