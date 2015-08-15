from flask import Flask, render_template, Response
from lib.poppins.camera import VideoCamera

class Server(object):

    def __init__(self):
        self.__app = Flask('__main__', template_folder='/Users/nickcrohn/git/ncrohn/poppins/templates')

        self.__app.add_url_rule('/', 'index', self.index)
        self.__app.add_url_rule('/video_feed', 'video_feed', self.video_feed)

    @property
    def app(self):
        return self.__app

    def index(self):
        return render_template('index.html')

    def gen(self, camera):
        while True:
            frame = camera.get_frame()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

    def video_feed(self):
        return Response(self.gen(VideoCamera()),
            mimetype='multipart/x-mixed-replace; boundary=frame')