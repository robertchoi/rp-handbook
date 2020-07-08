# gpio-interrupt-test.py
# GPIO12에 입력이 들어오면 문장을 출력한다.

# 라이브러리 불러오기
import RPi.GPIO as GPIO
import time

btn_input = 15

# 스위치 눌렸을 때 콜백함수
def switchPressed(channel):
    print('channel %s pressed!!'%channel)

GPIO.setmode(GPIO.BCM)

GPIO.setup(btn_input, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# interrupt 선언
GPIO.add_event_detect(12, GPIO.RISING, callback=switchPressed)

# 메인 쓰레드
try:
    while 1:
        print(".")
        time.sleep(0.1)
finally:
    GPIO.cleanup()
    