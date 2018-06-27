import cv2
import numpy as np

kernel = np.ones((9,9),np.uint8)

def updateTh(x):
    pass

cv2.namedWindow('Beetroot', cv2.WINDOW_NORMAL)
cv2.createTrackbar('Sat','Beetroot',22,255,updateTh)
cv2.createTrackbar('Gray','Beetroot',22,255,updateTh)
cv2.createTrackbar('GoodBad','Beetroot',28,500,updateTh)
cv2.namedWindow('Saturation', cv2.WINDOW_NORMAL)
cv2.namedWindow('Threshold', cv2.WINDOW_NORMAL)

cap = cv2.VideoCapture(1)

while(True):
    ret, img = cap.read()

    img = img[:, 0:520]

    height, width, channels = img.shape

    print(str(width) + "x" + str(height))

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    grayTh = cv2.getTrackbarPos('Gray', 'Beetroot')
    ret, gray = cv2.threshold(gray, grayTh, 255, cv2.THRESH_BINARY_INV)


    cv2.imshow("Threshold", gray)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h,s,v = cv2.split(hsv)

    s = cv2.bitwise_and(s,s,mask=gray)
    low = cv2.getTrackbarPos('Sat', 'Beetroot')

    ret, s = cv2.threshold(s, low, 255, cv2.THRESH_BINARY)
    s = cv2.erode(s, kernel, iterations=3)
    s = cv2.dilate(s, kernel, iterations=3)

    ret, contours, hierarchy = cv2.findContours(s,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    maxSize = 0
    id = 0
    maxId = 0
    for cnt in contours:
        if cv2.contourArea(cnt) > maxSize:
            maxSize = cv2.contourArea(cnt)
            maxId = id
        id = id + 1
    #print(maxSize)
    #print(maxId)
    goodBad = cv2.getTrackbarPos('GoodBad', 'Beetroot')
    if maxSize > goodBad*100:
        #print("This is bad")
        cv2.circle(img,(20, 20), 20, (0,0,225),-1)
    else:
        #print("This is good")
        cv2.circle(img,(20, 20), 20, (0,225,0),-1)
    try:
        M = cv2.moments(contours[maxId])
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        cv2.circle(img, (cX, cY), 7, (255, 255, 255), -1)
    except:
        print("Did not find anything")
    cv2.drawContours(img, contours, maxId, (0,255,0), 3)

    cv2.imshow("Beetroot", img)
    cv2.imshow("Saturation", s)

    k = cv2.waitKey(10) & 0x00FF
    if (k == 27):
        print("Quit")
        break

cv2.destroyAllWindows()
