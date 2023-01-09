import os
import cv2

cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

# Importing the mode images into a list
imgBackground=cv2.imread('Resources/background.png')
folderModePath = 'Resources/Modes'
modePathList=os.listdir(folderModePath)   # Gives the list of png files in Modes
imgModeList=[]

for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath,path)))
# print(len(imgModeList))

while True:
    success,img=cap.read()

    imgBackground[162:162+480,55:55+640]=img  # Overlaying the image upon the background template
    imgBackground[44:44+633, 808:808 + 414] = imgModeList[0]

    # cv2.imshow("Webcam",img)
    cv2.imshow("Face Attendance", imgBackground)
    cv2.waitKey(1)
