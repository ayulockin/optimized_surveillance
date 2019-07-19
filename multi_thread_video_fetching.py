import cv2
import datetime
import time
import numpy as np

from threading import Thread
from queue import Queue

class multiThreadVideoStream():
    def __init__(self, path, queueSize=1000):
        self.cap = cv2.VideoCapture(path)
        self.stopped = False
        self.Q = Queue(maxsize=queueSize)

    def start(self):
        t = Thread(target=self.update, args=())
        t.daemon = True
        t.start()
        return self

    def update(self):
        while True:
            if self.stopped:
                return

            if not self.Q.full():
                _, frame = self.cap.read()

                if not _:
                    self.stop()
                    return

                self.Q.put(frame)

    def stop(self):
        self.stopped = True
        self.cap.release()

    def more(self):
        return self.Q.qsize() > 0

    def read(self):
        return self.Q.get()


path = "videos/BirdNoSound.mp4"
fvs = multiThreadVideoStream(path).start()
time.sleep(1.0)

start = datetime.datetime.now()
num_frames = 0

while fvs.more():

    frame = fvs.read()
##    frame = cv2.resize(frame, (400,400))
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = np.dstack([frame, frame, frame])

    cv2.putText(frame, "Fast Method", (10,30), cv2.FONT_HERSHEY_SIMPLEX,
                0.6, (0,255,0), 2)

    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    num_frames+=1  

end = datetime.datetime.now()
elapsed = (end-start).total_seconds()
print("[INFO] elasped time: {:.2f}".format(elapsed))
print("[INFO] approx. FPS: {:.2f}".format(num_frames/elapsed))

cv2.destroyAllWindows()
fvs.stop()
    
    














