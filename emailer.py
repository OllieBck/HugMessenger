import os
import RPi.GPIO as GPIO
import random

sayings = ["I love you", "Thinking of you", "Hello Dad"]

def sendText():
    os.system("echo %s | mail EMAILFORTHEACCOUNT@gmail.com" % random.choice(sayings))

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.IN, pull_up_down = GPIO.PUD_UP)

while True:
    GPIO.wait_for_edge(22, GPIO.FALLING)
    GPIO.wait_for_edge(22, GPIO.RISING)
    
    sendText()

GPIO.cleanup()