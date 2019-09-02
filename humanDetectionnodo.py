# import the necessary packages
import numpy as np
import time
import cv2
import os
import datetime
import argparse

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
ap.add_argument("-cont", "--counter", required=False, default=15,
	help="Detection will occur after every 'counter' frame")
args = vars(ap.parse_args())


detector = yoloDetection(args["yolo"], args["input"], args["confidence"],
	args["threshold"], args["bbox"])

detector.prepareModel()

vs = cv2.VideoCapture(0)

start = datetime.datetime.now()
counter = 0

while True:
	(grabbed, frame) = vs.read()
	counter += 1
	if not grabbed:
		break

	if args["bbox"] is True:
		cv2.imshow('detector', frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			# print("FPS: ", numF/(datetime.datetime.now()-start).total_seconds())
			break
	else:
		if counter==args["counter"]:
			print("[INFO] running inference")
			out = detector.runInference(frame)
			print(out)
			counter = 0
		## TO STOP THIS CTRL+C

vs.release()   
cv2.destroyAllWindows()
