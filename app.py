#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, Response
from camera import VideoCamera
import sys

app = Flask(__name__)
_id = 0

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera(_id)),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    try:
        port = sys.argv[1]
    except:
        print 'Первым аргументом должен быть номер порта!'
        exit(1)
    try:
        #global _id
        _id = int(sys.argv[2])
    except:
        print 'Вторым аргументом должен быть ID камеры!'
        exit(1)
    app.run(host='192.168.70.17', port=int(port), debug=False)
