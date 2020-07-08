#!/usr/bin/env python
'''
face detection using haar cascades
USAGE:
    facedetect.py [--cascade <cascade_fn>] [--nested-cascade <cascade_fn>] [<video_source>]
'''



# Python 2/3 compatibility

from __future__ import print_function



import numpy as np
import cv2



# local modules
from video import create_capture
from common import clock, draw_str



def detect(img, cascade):
    rects = cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=4, minSize=(30, 30),
                                     flags=cv2.CASCADE_SCALE_IMAGE)

    if len(rects) == 0:
        return []

    rects[:,2:] += rects[:,:2]
    return rects


def draw_rects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)



if __name__ == '__main__':
    # 파일 옵션을 입력 받는 부분입니다. 옵션을 사용하지 않으니 넘어가도록 하겠습니다.
    import sys, getopt
    print(__doc__)

    args, video_src = getopt.getopt(sys.argv[1:], '', ['cascade=', 'nested-cascade='])

    try:
        video_src = video_src[0]
    except:
        video_src = 0
    args = dict(args)



    # 옵션에서 특별한 요구사항이 없으면 기본 옵션으로 진행합니다.
    # 얼굴 인식과 눈 인식 2개의 학습된 뉴럴넷을 가져옵니다.
    cascade_fn = args.get('--cascade', "../../data/haarcascades/haarcascade_frontalface_alt.xml")
    nested_fn  = args.get('--nested-cascade', "../../data/haarcascades/haarcascade_eye.xml")



    cascade = cv2.CascadeClassifier(cascade_fn)
    nested = cv2.CascadeClassifier(nested_fn)



   // 별도의 이미지를 옵션으로 입력하지 않았다면 기본값으로 lena를 가져옵니다.
    cam = create_capture(video_src, fallback='synth:bg=../data/lena.jpg:noise=0.05')

    while True:
        #이미지 파일을 읽어옵니다.
        ret, img = cam.read()

        # 흑백이미지로 변환합니다.
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # 히스토그램을 이퀄라이즈 합니다.
        gray = cv2.equalizeHist(gray)



        # 시작한 시간을 측정합니다. 
        t = clock()

        # 얼굴 인식을 실행합니다.
        rects = detect(gray, cascade)

        # 원본이미지를 복사합니다.
        vis = img.copy()
        # 얼굴이 인식된 부분에 사각형을 그려줍니다.
        draw_rects(vis, rects, (0, 255, 0))
        # 같은 식으로 눈을 인식하고 눈 부분에 사각형을 그려줍니다.
        if not nested.empty():
            for x1, y1, x2, y2 in rects:
                roi = gray[y1:y2, x1:x2]
                vis_roi = vis[y1:y2, x1:x2]
                subrects = detect(roi.copy(), nested)
                draw_rects(vis_roi, subrects, (255, 0, 0))

        # 처리를 시작한 시점과 마친 시점의 시간 차이를 이용하여 소요된 시간을 계산합니다.

        dt = clock() - t
        draw_str(vis, (20, 20), 'time: %.1f ms' % (dt*1000))
        cv2.imshow('facedetect', vis)


        if cv2.waitKey(5) == 27:
            break

    cv2.destroyAllWindows()