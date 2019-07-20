import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)
p = GPIO.PWM(11,50)
p.start(0)

delay = 0.015                   #delay between successive positions(0.015)
pos = 2.5                       #duty cycle corresponding to positions[2.5,12.5]
step = 0.05                     #increments in positions(0.05)
try:
    while True:
        if(pos > 12.5):
            ret = -1            #reverses the direction
        elif(pos <= 2.5):
            ret = 1
        p.ChangeDutyCycle(pos)
        print(pos)                #debug
        pos += ret * step
        sleep(delay)
except:
    p.stop()
    GPIO.cleanup()
