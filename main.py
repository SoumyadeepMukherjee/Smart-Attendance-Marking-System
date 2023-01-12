import os
import cv2
import pickle
import cvzone
import face_recognition
import numpy as np

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

# Load the encoding file
print("Loading Encode File...")
file=open('EncodeFile.p','rb')
encodeListKnownWithIds=pickle.load(file)
file.close()
encodeListKnown, studentIds = encodeListKnownWithIds
print(studentIds)
print("Encode File Loaded...")

while True:
    success,img=cap.read()

    imgS=cv2.resize(img,(0,0), None, 0.25, 0.25)   # Scaling down the image to 1/4th
    imgS=cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)

    faceCurrFrame=face_recognition.face_locations(imgS)
    encodeCurrFrame=face_recognition.face_encodings(imgS,faceCurrFrame)

    imgBackground[162:162+480,55:55+640]=img  # Overlaying the image upon the background template
    imgBackground[44:44+633, 808:808 + 414] = imgModeList[0]

    for encodeFace,faceLoc in zip(encodeCurrFrame,faceCurrFrame):
        matches=face_recognition.compare_faces(encodeListKnown,encodeFace)
        faceDis=face_recognition.face_distance(encodeListKnown,encodeFace)   # Lower the face distance , better the match
        # print("Matches:",matches)
        # print("Face Distance:",faceDis)

        matchIndex=np.argmin(faceDis)
        # print("Match Index",matchIndex)

        if matches[matchIndex]:
            print("Known Face Detected!")
            y1,x2,y2,x1=faceLoc
            y1,x2,y2,x1=y1*4,x2*4,y2*4,x1*4    # Scaling up 4 times coz it was scaled down previously
            bbox= 55+x1,162+y1,x2-x1,y2-y1     # Creating the bounding box
            imgBackground=cvzone.cornerRect(imgBackground,bbox,rt=0)


    # cv2.imshow("Webcam",img)
    cv2.imshow("Face Attendance", imgBackground)
    cv2.waitKey(1)
