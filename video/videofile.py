# -*- coding: utf-8 -*-
"""
Created on Sat May 18 17:28:17 2019

@author: MAGESHWARAN
"""

import cv2
import urllib
import numpy as np

def record_video(filename, fps=30, gray=False, os='windows'):

    cap = cv2.VideoCapture(0)

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    if os == "windows":
        fourcc = cv2.VideoWriter_fourcc(*"DIVX")

    elif os == "linux":
        fourcc = cv2.VideoWriter_fourcc(*"XVID")

    elif os == "mac":
        fourcc = cv2.cv.CV_FOURCC('m', 'p', '4', 'v')

    if gray:
        writer = cv2.VideoWriter(filename, fourcc,
                                 fps, (width, height), 0)
    else:
        writer = cv2.VideoWriter(filename, fourcc,
                                 fps, (width, height))
    while True:

        ret, frame = cap.read()

        if gray:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        writer.write(frame)
        cv2.imshow("frame", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    writer.release()
    cv2.destroyAllWindows()

def video_stream(url):

    while True:
        video = urllib.request.urlopen(url)
        video_arr = np.array(bytearray(video.read()), dtype=np.uint8)

        frame = cv2.imdecode(video_arr, -1)

        cv2.imshow("IPWebcam", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break
    cv2.destroyAllWindows()

if __name__ == "__main__":
    record_video("video.mp4", gray=False)

    # video_stream("http://192.168.43.1:8080/shot.jpg")