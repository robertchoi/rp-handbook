import RPi.GPIO as GPIO
import time

led = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

myPwm = GPIO.PWM(led, 1000) # pin, frequency
myPwm.start(50) #dutycycle (0~100사이 값). 아두이노로 치면 analogWrite(18, 128)과 동일.

# 출력값 변경 (0~100%)
myPwm.ChangeDutyCycle(10)

# Frequency  변경 (Hz)
myPwm.ChangeFrequency(1500)

cycleValue = 10

for k in range(10):
	cycleValue += 8 
	time.sleep(1)


#swPWM 정지
myPwm.stop()

GPIO.cleanup()
