import logging
import threading
import time

import numpy as np
import argparse
import imutils
import cv2
import os

from queue import Queue
from detection.Detection import yoloDetection

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-y", "--yolo", required=True,
    help="base path to YOLO directory")
ap.add_argument("-i", "--input", required=False,
    help="path to input video")
ap.add_argument("-c", "--confidence", type=float, default=0.5,
    help="minimum probability to filter weak detections")
ap.add_argument("-t", "--threshold", type=float, default=0.3,
    help="threshold when applyong non-maxima suppression")
ap.add_argument("-b", "--bbox", required=False, default=True,
    help="turn on bounding box")
args = vars(ap.parse_args())

Q = Queue(maxsize=1)

# vs = cv2.VideoCapture(0)

# _, frame = vs.read()

def thread1_function(name):
    ## Reading frames
    global Q
    logging.info("Thread %s: starting ", name)
    vs = cv2.VideoCapture(0)
    while True:
        _, frame = vs.read()
        # print("thread 1:", frame)
        Q.put(frame)
        print("Thread 1: starting ", Q.qsize())

    logging.info("Thread %s: finishing", name) 

def thread2_function(name):
    global Q
    ## Detection
    logging.info("Thread %s: starting ", name)

    detector = yoloDetection(args["yolo"], args["input"], args["confidence"],
    args["threshold"], args["bbox"])

    detector.prepareModel()

    while True:
        frame = Q.get()
        # print(frame.shape)
        # print("Thread 2: starting ", Q.qsize())
        # print(frame)
        out = detector.runInference(frame)
        # print(out.shape)

        if args["bbox"] is True:
            cv2.imshow('detector', out)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            print(out)
            ## TO STOP THIS CTRL+C

    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    logging.info("Main    : before creating thread")

    # Create the first thread here
    x = threading.Thread(target=thread1_function, args=(1,))
    time.sleep(1.0)
    # Create the second thread here
    x1 = threading.Thread(target=thread2_function, args=(2,))

    logging.info("Main    : before running thread")
    # Start the first thread
    x.start()
    # time.sleep(1.0)
    # Start the second thread
    x1.start()

    logging.info("Main    : wait for the thread to finish")
    logging.info("Main    : all done")