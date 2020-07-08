import RPi.GPIO as GPIO
import time

gpio_input = 15

GPIO.setmode(GPIO.BCM)
GPIO.setup(gpio_input, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while 1:
	if GPIO.input(gpio.input) == GPIO.HIGH:
		print("Button pushed!") 
	time.sleep(0.1)

GPIO.cleanup()
