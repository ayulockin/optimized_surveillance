from flask import Flask, render_template, Response
import cv2
import os

# http://99.136.119.239/mjpg/video.mjpg
# http://47.21.223.167/mjpg/video.mjpg

app = Flask(__name__)
video = cv2.VideoCapture('http://99.136.119.239/mjpg/video.mjpg')

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        rval, frame = video.read()
        dim = (640, 480)
        frame_small = cv2.resize(frame, dim)
        cv2.imwrite('framebuffer.jpg', frame_small)
        yield(b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + open('framebuffer.jpg', 'rb').read() + b'\r\n')
        # print(type(frame))

@app.route('/video_feed')
def video_feed():
    return Response(gen(video), mimetype='multipart/x-mixed-replace; boundary=frame')

# port = int(os.getenv('VCAP_APP_PORT'))
port = 80

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port ,debug=True, threaded=True)
