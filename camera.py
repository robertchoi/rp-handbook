# -*- coding: utf-8 -*- 

import picamera, sys  # 카메라랑 시스템을 관리하는 라이브러리를 사용합니다.


camera = picamera.PiCamera() 
camera.resolution=(1920,1080) #출력 해상도를 1920x1080으로 설정합니다. 
camera.start_preview()  #프리뷰를 사작합니다.

def main():  #엔터를 누르면 프로그램이 꺼지게 하는 메인함수 입니다.
    print"Press Enter to quit..."
    
    try:
        sys.stdin.readline()
    except KeyboardInterrupt: 
        pass
    camera.stop_preview()  #프리뷰를 종료합니다.

if __name__ == "__main__": #메인함수
    main()