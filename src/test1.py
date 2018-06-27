import cv2
from load_data import *

data = BeetRootData(
    path='./../data/',
    name_stem='beet',
    dataset='Train',
    format='.jpg'
)
kernel = np.ones((9,9),np.uint8)

def updateTh(x):
    pass

cv2.namedWindow('Beetroot', cv2.WINDOW_NORMAL)
cv2.createTrackbar('Low','Beetroot',22,255,updateTh)
cv2.namedWindow('Good', cv2.WINDOW_NORMAL)
cv2.namedWindow('Bad', cv2.WINDOW_NORMAL)

i = 0
while(i < 50):
    name = "../data/Train/beet" + str(i) + ".jpg"
    state = data.is_good(i)
    img = cv2.imread(name, 1)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h,s,v = cv2.split(hsv)

    low = cv2.getTrackbarPos('Low', 'Beetroot')

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
    print(maxSize)
    print(maxId)
    if maxSize > 28000:
        print("This is bad")

    else:
        print("This is good")
    cv2.drawContours(img, contours, maxId, (0,255,0), 3)
    #circles = cv2.HoughCircles(s,cv2.HOUGH_GRADIENT,1,20, param1=50,param2=30,minRadius=0,maxRadius=0)
    #circles = np.uint16(np.around(circles))
    #for j in circles[0,:]:
    #    cv2.circle(img,(j[0],j[1]),j[2],(0,255,0),2)
    cv2.imshow("Beetroot", img)

    if state:
        cv2.imshow("Bad", s)
        print("Database says its bad")
    else:
        cv2.imshow("Good", s)
        print("Database says its good")
    k = cv2.waitKey(0) & 0x00FF
    if (k == 27):
        print("Quit")
        break
    else:
        i = i + 1

cv2.destroyAllWindows()
