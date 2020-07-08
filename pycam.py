

import picamera, sys  # 카메라랑 시스템을 관리하는 라이브러리를 사용합니다.


with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.start_preview()
    camera.start_recording('cos.h264')
    camera.wait_recording(30)
    camera.stop_recording()
    camera.stop_preview()
