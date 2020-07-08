import RPi.GPIO as GPIO
import time

led = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT)

for k in range(10): 
	GPIO.output(led, GPIO.HIGH) 
	time.sleep(0.5) 
	GPIO.output(led, GPIO.LOW) 
	time.sleep(0.5)

GPIO.cleanup()
