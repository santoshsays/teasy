
# command to run : python3 pi_face_recognition.py --cascade haarcascade_frontalface_default.xml --encodings encodings.pickle
from imutils.video import VideoStream
from imutils.video import FPS
#import numpy as np
#import requests
import face_recognition
import argparse
import imutils
import pickle
import time
import cv2

import os
import json
import time
import ast
import datetime
import threading
import uuid

id=uuid.uuid4().hex[:8]
image_flag=0

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-c", "--cascade", required=True,
    help = "path to where the face cascade resides")
ap.add_argument("-e", "--encodings", required=True,
    help="path to serialized db of facial encodings")
args = vars(ap.parse_args())

# load the known faces and embeddings along with OpenCV's Haar
# cascade for face detection
print("[INFO] loading encodings + face detector...")
data = pickle.loads(open(args["encodings"], "rb").read())
detector = cv2.CascadeClassifier(args["cascade"])

# initialize the video stream and` allow the camera sensor to warm up
print("[INFO] starting video stream...")
#vs = VideoStream(src=0).start()
#vs=cv2.VideoCapture('http://192.168.43.57:8080/')
vs = VideoStream(usePiCamera=True).start()
time.sleep(2.0)

# start the FPS counter
fps = FPS().start()

# loop over frames from the video file stream
while True:
    # grab the frame from the threaded video stream and resize it
    # to 500px (to speedup processing)

    #imgResp = requests.get('http://192.168.43.57:8080/shot.jpg')
    #imgNp = np.array(bytearray(imgResp.content),dtype=np.uint8)
    #vs = cv2.imdecode(imgNp,cv2.IMREAD_COLOR)


    frame = vs.read()
    frame = imutils.resize(frame, width=500)

    # convert the input frame from (1) BGR to grayscale (for face
    # detection) and (2) from BGR to RGB (for face recognition)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # detect faces in the grayscale frame
    rects = detector.detectMultiScale(gray, scaleFactor=1.1,
        minNeighbors=5, minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE)

    # OpenCV returns bounding box coordinates in (x, y, w, h) order
    # but we need them in (top, right, bottom, left) order, so we
    # need to do a bit of reordering
    boxes = [(y, x + w, y + h, x) for (x, y, w, h) in rects]

    # compute the facial embeddings for each face bounding box
    encodings = face_recognition.face_encodings(rgb, boxes)
    names = []
#----------codes till face detectation -----------------
    # loop over the facial embeddings
    for encoding in encodings:
        # attempt to match each face in the input image to our known
        # encodings
        matches = face_recognition.compare_faces(data["encodings"],
            encoding)
        name = "Unknown"
        #print(name)
        # check to see if we have found a match
        if True in matches:
            # find the indexes of all matched faces then initialize a
            # dictionary to count the total number of times each face
            # was matched
            matchedIdxs = [i for (i, b) in enumerate(matches) if b]
            counts = {}

            # loop over the matched indexes and maintain a count for
            # each recognized face face
            for i in matchedIdxs:
                name = data["names"][i]
                counts[name] = counts.get(name, 0) + 1

            # determine the recognized face with the largest number
            # of votes (note: in the event of an unlikely tie Python
            # will select first entry in the dictionary)
            name = max(counts, key=counts.get)



        # update the list of names
        names.append(name)
        
        filepath=os.path.join('/home/pi/travel/piface/dataset',"%s.json"%name)
        timenow=str(datetime.datetime.now())
        travel={'id':id,'name':name,'time-starts':timenow,'location1':"Mangalore"}
        with open(filepath,'w+') as f:
            f.write("\n")
            f.write(json.dumps(travel))
            f.write("\n")

    # loop over the recognized faces
    for ((top, right, bottom, left), name) in zip(boxes, names):
        # draw the predicted face name on the image
        cv2.rectangle(frame, (left, top), (right, bottom),
            (0, 255, 0), 2)
        y = top - 15 if top - 15 > 15 else top + 15
        cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
            0.75, (0, 255, 0), 2)

    # display the image to our screen
    cv2.imshow("Travel Easy", frame)
    key = cv2.waitKey(1) & 0xFF

    #timer=threading.Timer(10.0,fetch_location)
    #timer.start()
    #timer1=threading.Timer(2.0,calculate)
    #timer1.start()

    if key==ord("r"):
        timethen=str(datetime.datetime.now())
        travel.update({'time-ends':timethen,'location2':"Surathkal"})

        with open(filepath,'a+') as f:
            f.write(json.dumps(travel))



    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break

    # update the FPS counter
    fps.update()

# stop the timer and display FPS information
fps.stop()
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()