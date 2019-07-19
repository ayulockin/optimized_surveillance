import logging
import threading
import time

def thread1_function(name):
    logging.info("Thread %s: starting ", name)
    time.sleep(2)
    # Remove the sleep and read the video here
    logging.info("Thread %s: finishing", name)
def thread2_function(name):
    logging.info("Thread %s: starting ", name)
    time.sleep(2)
    # Remove the sleep and detect objects here
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    logging.info("Main    : before creating thread")
    # Create the first thread here
    x = threading.Thread(target=thread1_function, args=(1,))
    # Create the second thread here
    x1 = threading.Thread(target=thread2_function, args=(2,))
    logging.info("Main    : before running thread")
    # Start the first thread
    x.start()
    # Start the second thread
    x1.start()
    logging.info("Main    : wait for the thread to finish")
    logging.info("Main    : all done")