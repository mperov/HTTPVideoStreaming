#/usr/bin/env python

import cv2
import time
import sys
import numpy as np
import os

class VideoCamera(object):
    def __init__(self, _id):
        self.video = self.VideoCapture(_id)

    def VideoCapture(self, _id):
        video = cv2.VideoCapture(_id)
        #video.set(3, 340)
        video.set(4, 240)

        return video

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, frame = self.video.read()
        ret, jpeg = cv2.imencode('.jpg', frame)
        return bytearray(jpeg)
