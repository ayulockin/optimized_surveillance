import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)
p = GPIO.PWM(11,50)
p.start(0)

delay = 1

#duty cycle = (length)/(period) * 100
#for length:
#0.5 -> 0 degrees
#1.5 -> 90 degrees
#2.5 -> 180 degrees
#for period
#period = 1000/freq ms
try:
    while True:
        p.ChangeDutyCycle(2.5)          #rotates to 0 degrees
        print('0')
        sleep(delay)
        p.ChangeDutyCycle(7.5)          #rotates to 90 degrees
        print('90')
        sleep(delay)
        p.ChangeDutyCycle(12.5)         #rotates to 180 degrees
        print('180')
        sleep(delay)
        p.ChangeDutyCycle(7.5)          #rotates to 90 degrees
        print('90')
        sleep(delay)
except:
    p.stop()
    GPIO.cleanup()
