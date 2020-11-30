import cv2

video = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    ret,cam = video.read()
    cam = cv2.flip(cam,1)
    cv2.waitKey(1)
    #top
    img = cv2.rectangle(cam,(260,40),(360,80),(255,0,0), 2)
    cv2.putText(img,'Up',(290,70),font,1,(255,0,0),2,cv2.LINE_AA)

    #bottom
    img = cv2.rectangle(img,(260,400),(360,440),(255,0,0), 2)
    cv2.putText(img, 'Down', (270, 430), font, 1, (255, 0, 0), 2, cv2.LINE_AA)

    #left
    img = cv2.rectangle(img,(40,220),(140,260),(255,0,0), 2)
    cv2.putText(img, 'Left', (60, 250), font, 1, (255, 0, 0), 2, cv2.LINE_AA)

    #right
    img = cv2.rectangle(img, (460, 220), (560, 260), (255, 0, 0), 2)
    cv2.putText(img, 'Right', (470, 250), font, 1, (255, 0, 0), 2, cv2.LINE_AA)
    
    cv2.imshow('Video', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    #print(cam.shape)