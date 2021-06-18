import cv2
import numpy as np

cap = cv2.VideoCapture(0)
img = cv2.imread("pink_flowers_background.jpg")
# cv2.imshow("bg",img)

while True:
    ret, frame = cap.read()

    frame = cv2.resize(frame , (640 , 480))
    img  = cv2.resize(img,(640,480))

    u_black = np.array([104,153,70])
    l_black = np.array([30,30,0])

    # hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(frame,l_black,u_black )
    res = cv2.bitwise_and(frame,frame,mask=mask)

    f= frame - res
    f= np.where(f==0,img,f)

    cv2.imshow("original",frame)
    cv2.imshow("mask magic", f)

    if cv2.waitKey(1) & 0XFF == ord('q'):
        break
    



cap.release() 
cv2.destroyAllWindows() 
