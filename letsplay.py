import cv2
import numpy as np
import keyboard
import time

def up():
    keyboard.press('w')
    time.sleep(0.05)
    keyboard.release('w')
    #time.sleep(0.1)

def down():
    keyboard.press('s')
    time.sleep(0.05)
    keyboard.release('s')
    #time.sleep(0.1)

def right():

    keyboard.press('d')
    time.sleep(0.05)
    keyboard.release('d')
    #time.sleep(0.1)

def left():

    keyboard.press('a')
    time.sleep(0.05)
    keyboard.release('a')
    #time.sleep(0.1)

def action():
    keyboard.press(' ')
    time.sleep(0.1)
    keyboard.release(' ')
    #time.sleep(0.1)

video = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX
PINK_MIN = np.array([134, 142, 0], np.uint8)
PINK_MAX = np.array([162, 255, 255], np.uint8)
centroid_x,centroid_y = 0,0

while True:
    ret, cam = video.read()
    cam = cv2.flip(cam, 1)
    cv2.waitKey(1)
    # top
    img = cv2.rectangle(cam, (260, 40), (360, 80), (255, 0, 0), 2)
    cv2.putText(img, 'Up', (290, 70), font, 1, (255, 0, 0), 2, cv2.LINE_AA)

    # bottom
    img = cv2.rectangle(img, (260, 400), (360, 440), (255, 0, 0), 2)
    cv2.putText(img, 'Down', (270, 430), font, 1, (255, 0, 0), 2, cv2.LINE_AA)

    # left
    img = cv2.rectangle(img, (40, 220), (140, 260), (255, 0, 0), 2)
    cv2.putText(img, 'Left', (60, 250), font, 1, (255, 0, 0), 2, cv2.LINE_AA)

    # right
    img = cv2.rectangle(img, (460, 220), (560, 260), (255, 0, 0), 2)
    cv2.putText(img, 'Right', (470, 250), font, 1, (255, 0, 0), 2, cv2.LINE_AA)


    hsv = cv2. cvtColor(img,cv2.COLOR_BGR2HSV)
    frame_thresh = cv2.inRange(hsv,PINK_MIN,PINK_MAX)
    contours, hierarchy = cv2.findContours(frame_thresh, 1, 2)
    max_area = 0
    last_x = centroid_x
    last_y = centroid_y
    if contours:
        for i in contours:
            area = cv2.contourArea(i)
            if area > max_area:
                max_area = area
                cnt = i
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        centroid_x = (x + x + w) / 2
        centroid_y = (y + y + h) / 2
    cv2.imshow('Video', img)
    if centroid_x > 200 and centroid_x < 420:
        # up
        if centroid_y >= 0 and centroid_y <= 140:
            cv2.rectangle(cam, (260, 40), (360, 80), (0, 0, 255), 2)
            cv2.putText(img, 'Up', (290, 70), font, 1, (0, 0, 255), 2, cv2.LINE_AA)
            up()
        # down
        if centroid_y > 340 and centroid_y < 480:
            cv2.rectangle(img, (260, 400), (360, 440), (0, 0, 255), 2)
            cv2.putText(img, 'Down', (270, 430), font, 1, (0, 0, 255), 2, cv2.LINE_AA)
            down()

        # left-right move
    if centroid_y >= 160 and centroid_y <= 320:
        # left
        if centroid_x >= 0 and centroid_x <= 200:
            cv2.rectangle(img, (40, 220), (140, 260), (0, 0, 255), 2)
            cv2.putText(img, 'Left', (60, 250), font, 1, (0, 0, 255), 2, cv2.LINE_AA)
            left()
        # right
        if centroid_x>400 and centroid_x < 640:
            cv2.rectangle(img, (460, 220), (560, 260), (0, 0, 255), 2)
            cv2.putText(img, 'Right', (470, 250), font, 1, (0, 0, 255), 2, cv2.LINE_AA)
            right()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    print(cam.shape)