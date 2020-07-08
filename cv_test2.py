import cv2

cap = cv2.VideoCapture(0) #카몌라 불러오기
if cap.isOpened() == False: #카메라 열림 확인
    exit()

while True :
    ret, img = cap.read() #카메라 읽기
    cv2.imshow('preview', img) #읽은 이미지 보여주기  
    if cv2.waitKey(10) >= 0 : #10ms간 대기, 입력이 있으면 종료
        break

# 연결 끊기
cap.release()
cv2.destroyAllWindows()