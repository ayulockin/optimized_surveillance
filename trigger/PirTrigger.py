import RPi.GPIO as GPIO
from time import sleep

#pins
Pir = 16
Servo = 11

#variables: Pir
rearm = 6
startup = 2
PirDelay = 0.1

#variables: Servo
pos = 2.5                   #[2.5, 12.5] => [0, 180] degrees
step = 0.05                 #0.05
ServoDelay = 0.015           #0.015
freq = 50                   #50 Hz = 20 ms signal
rot = 3                   #3

#setup
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(Servo, GPIO.OUT)
GPIO.setup(Pir, GPIO.IN)
M = GPIO.PWM(Servo, freq)
M.start(0)

def startMotor(pos, step, rot):
    rev = 1
    cycle = 0
    while(cycle <= rot):
        if(pos >= 12.5):
            rev = -1
        elif(pos <= 2.5):
            rev = 1
            cycle += 1
        M.ChangeDutyCycle(pos)
        print('%5.2f | %d'%(pos,cycle))
        pos += rev * step
        sleep(ServoDelay)
    M.ChangeDutyCycle(0)            #no signal

def readPir():
    if(GPIO.input(Pir)):
        return 1
    else:
        return 0

if(__name__ == '__main__'):
    try:
        while True:
            print(readPir())
            if(readPir()):
                startMotor(pos, step, rot)
            if(rot == 1):
                sleep(rearm)
    except:
        M.stop()
        GPIO.cleanup()
