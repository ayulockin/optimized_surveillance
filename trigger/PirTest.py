import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.IN)

rearm = 6                       #delay for rearming the PIR
startup = 2                     #startup delay
delay = 0.1                     #loop delay

try:
    sleep(startup)
    while True:
        if(GPIO.input(16)):
            print('DETECTED. Rearming...')
            sleep(rearm)
        print('Ready.')
        sleep(delay)
except:
    GPIO.cleanup()
