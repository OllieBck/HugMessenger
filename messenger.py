import os
import time
import RPi.GPIO as GPIO

def playMessage():
    os.system('omxplayer -o local /home/pi/Google/CodeFiles/message.m4a')

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.IN, pull_up_down = GPIO.PUD_UP)

while True:
    GPIO.wait_for_edge(22, GPIO.FALLING)
    GPIO.wait_for_edge(22, GPIO.RISING)
    playMessage()
    time.sleep(1)

GPIO.cleanup()