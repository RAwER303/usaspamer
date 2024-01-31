import time
import cv2 as cv
import cv2
#from playsound import playsound
#from playsound import playsound
image = cv2.imread('rahhh.png')
a="USA RAAAAAAAAAAAAAAAAAAAAAH"
i=0
while True:
    a= a+str(i)
    i=i+1
    cv2.imshow(a, image)
    cv.waitKey(27)
    time.sleep(0.000000000000000000000000000000000000000000001)
