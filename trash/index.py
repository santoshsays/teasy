# python3 main.py --cascade haarcascade_frontalface_default.xml --encodings encodings.pickle
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
# import some PyQt5 modules
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt
from imutils.video import VideoStream
from imutils.video import FPS
from playsound import playsound
import numpy as np
import requests
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
 #from login import Ui_MainWindow
class Ui_MainWindow1(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 810)
        MainWindow.setStyleSheet("\n"
        "\n"
        "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.start_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_btn.setEnabled(True)
        self.start_btn.setGeometry(QtCore.QRect(630, 10, 91, 41))
        self.start_btn.setStyleSheet("QPushButton{\n"
        "font-size:16px;\n"
        "color:white;\n"
        "font-weight:bold;\n"
        "background-color:#44A08D;\n"
        "}\n"
        "QPushButton:hover\n"
        "{\n"
        "background: #03bb85;\n"
        "color: white;\n"
        "}\n"
        "")
        self.start_btn.setObjectName("start_btn")
        self.start_btn.clicked.connect(self.controlTimer1)
        #self.start_btn.clicked.connect(self.controlTimer2)
        self.stop_btn = QtWidgets.QPushButton(self.centralwidget)
        self.stop_btn.setEnabled(True)
        self.stop_btn.setGeometry(QtCore.QRect(720, 10, 91, 41))
        self.stop_btn.setStyleSheet("QPushButton{\n"
        "font-size:16px;\n"
        "color:white;\n"
        "font-weight:bold;\n"
        "background-color:#44A08D;\n"
        "}\n"
        "QPushButton:hover\n"
        "{\n"
        "background: #03bb85;\n"
        "color: white;\n"
        "}\n"
        "")
        self.stop_btn.setObjectName("stop_btn")
        self.stop_btn.clicked.connect(self.closecamera)
        self.logout_btn = QtWidgets.QPushButton(self.centralwidget)
        self.logout_btn.setEnabled(True)
        self.logout_btn.setGeometry(QtCore.QRect(810, 10, 101, 41))
        self.logout_btn.setStyleSheet("QPushButton{\n"
        "font-size:16px;\n"
        "color:white;\n"
        "font-weight:bold;\n"
        "background-color:#44A08D;\n"
        "}\n"
        "QPushButton:hover\n"
        "{\n"
        "background: #03bb85;\n"
        "color: white;\n"
        "}\n"
        "")
        self.logout_btn.setObjectName("logout_btn")
        #self.logout_btn.clicked.connect(self.logoutwindow)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 141, 791))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dashboard = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.dashboard.setStyleSheet("QLabel{\n"
        "background:#263238;\n"
        "color:white;\n"
        "font-size:24px;\n"
        "\n"
        "}\n"
        "QLabel:hover{\n"
        "color:#44A08D;\n"
        "}")
        self.dashboard.setText("")
        self.dashboard.setObjectName("dashboard")
        self.verticalLayout.addWidget(self.dashboard)
        self.camera1 = QtWidgets.QLabel(self.centralwidget)
        self.camera1.setGeometry(QtCore.QRect(150, 280, 500, 500))
        self.camera1.setText("")
        self.camera1.setObjectName("camera1")
        self.camera2 = QtWidgets.QLabel(self.centralwidget)
        self.camera2.setGeometry(QtCore.QRect(700, 280, 500, 500))
        self.camera2.setText("")
        self.camera2.setObjectName("camera2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(287, 150, 101, 41))
        self.label_2.setStyleSheet("QLabel{\n"
        "color:#263238;\n"
        "\n"
        "font-size:14px;\n"
        "\n"
        "}")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(650, 150, 121, 41))
        self.label_3.setStyleSheet("QLabel{\n"
        "color:#263238;\n"
        "\n"
        "font-size:14px;\n"
        "\n"
        "}")
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 0, 771, 59))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(99)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("QLabel{\n"
        "background:#263238;\n"
        "color:white;\n"
        "font-size:24px;\n"
        "\n"
        "}\n"
        "QLabel:hover{\n"
        "mp4'olor:#44A08D;\n"
        "}")
        self.label.setObjectName("label")
        self.verticalLayoutWidget.raise_()
        self.camera1.raise_()
        self.camera2.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label.raise_()
        self.start_btn.raise_()
        self.stop_btn.raise_()
        self.logout_btn.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.start_btn.setText(_translate("MainWindow", "S T A R T"))
        self.stop_btn.setText(_translate("MainWindow", "S T O P"))
        self.logout_btn.setText(_translate("MainWindow", "L O G O U T"))
        self.label_2.setText(_translate("MainWindow", "C A M E R A - I"))
        self.label_3.setText(_translate("MainWindow", "C A M E R A - II"))
        self.label.setText(_translate("MainWindow", "       Travel Easy  "))

# class RecordVideo(QtCore.QObject):
#     image_data = QtCore.pyqtSignal(np.ndarray)

#     def __init__(self, camera_port=0, parent=None):
#         super().__init__(parent)
#         self.camera = cv2.VideoCapture(camera_port)

#         self.timer = QtCore.QBasicTimer()

#     def start_recording(self):
#         self.timer.start(0, self)

#     def timerEvent(self, event):
#         if (event.timerId() != self.timer.timerId()):
#             return

#         read, data = self.camera.read()
#         if read:
#             self.image_data.emit(data)

 
class Prog(QtWidgets.QMainWindow, Ui_MainWindow1):
       
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.timer1 = QTimer()    
        #self.timer2 = QTimer()
        # set timer timeout callback function
        self.timer1.timeout.connect(self.opencamera1)
        #self.timer2.timeout.connect(self.opencamera2)
    
              
    
    def opencamera1(self):
       
        frame = self.cap1.read()
        frame = imutils.resize(frame, width=500)
        # convert the input frame from (1) BGR to grayscale (for face
        # detection) and (2) from BGR to RGB (for face recognition)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        image = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(image)
         # show image in img_label
        self.camera1.setPixmap(pixmap)        

        # convert image file into pixmap
        self.pixmap_image = QtGui.QPixmap.fromImage(image)
    # view camera
    def controlTimer1(self):
        # if timer is stopped 
        #self.cap1=VideoStream(usePiCamera=True).start()      
        self.cap1 = cv2.VideoCapture(0)
        # time.sleep(2.0)
        # self.cap1.set(5, 30)  #set FPS
        # self.cap1.set(3, 640) #set width
        # self.cap1.set(4, 480) #set height            
       
        self.timer1.start(1000./24)
        # if not self.timer.isActive():
        #     # create video capture
        #     # self.cap = cv2.VideoCapture(0)
        #     # start timer
        #     self.timer.start(20)    
    def face_recognition():
        # construct the argument parser and parse the arguments
        ap = argparse.ArgumentParser()
        ap.add_argument("-c", "--cascade", required=True,
            help = "path to where the face cascade resides")
        
        ap.add_argument("-e", "--encodings", required=True,
            help="path to serialized db of facial encodings")
             
        args = vars(ap.parse_args('-c haarcascade_frontalface_default.xml -e encodings.pickle'.split()))
           
        data = pickle.loads(open(args["encodings"], "rb").read())
        detector = cv2.CascadeClassifier(args["cascade"])       
        # read image in BGR format 
     
        # detect faces in the grayscale frame
        rects = detector.detectMultiScale(gray, scaleFactor=1.1,
            minNeighbors=5, minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE)
        
        # OpenCV returns bounding box coordinates in (x, y, w, h) order
        # but we need them in (top, right, bottom, left) order, so we
         # need to do a bit of reordering
        boxes = [(y, x + w, y + h, x) for (x, y, w, h) in rects]

        # compute the facial embeddings for each face bounding box
        encodings = face_recognition.face_encodings(frame, boxes)
        names = []
        #id=[]
        
        # loop over the facial embeddings
        for encoding in encodings:
            # attempt to match each face in the input image to our known
            # encodings
            matches = face_recognition.compare_faces(data["encodings"],
                encoding)
            print(matches)
            name = "Unknown"
            
        
             # check to see if we have found a match
            if True in matches:
                # find the indexes of all matched faces then initialize a
                # dictionary to count the total number of times each face
                # was matched
                matchedIdxs = [i for (i, b) in enumerate(matches) if b]
                print(matchedIdxs)
                counts = {}

                # loop over the matched indexes and maintain a count for
                # each recognized face face
                for i in matchedIdxs:
                    name = data["names"][i]
                    print(name)
                    counts[name] = counts.get(name, 0) + 1

                # determine the recognized face with the largest number
                # of votes (note: in the event of an unlikely tie Python
                # will select first entry in the dictionary)
                name = max(counts, key=counts.get)
            
            # update the list of names
            names.append(name)

            filepath=os.path.join('/home/pi/tapp/account',"%s.json"%name)
            timenow=str(datetime.datetime.now())
            travel={'id':id,'name':name,'time-starts':timenow,'location1':"Mangalore"}
            j=json.dumps(travel,default=lambda x: None)
            with open(filepath,'w+') as f:
                f.write(j)
            
            #playsound('verify.wav')   
        
        # loop over the recognized faces
        for ((top, right, bottom, left), name) in zip(boxes, names):
            # draw the predicted face name on the image
            paint=cv2.rectangle(frame, (left, top), (right, bottom),
                (0, 255, 0), 2)


            #create painter instance with pixmap
            self.painterInstance = QtGui.QPainter(self.pixmap_image)

            # set rectangle color and thickness
            self.penRectangle = QtGui.QPen(QtCore.Qt.green)
            self.penRectangle.setWidth(2)

            # draw rectangle on painter
            self.painterInstance.setPen(self.penRectangle)
            self.painterInstance.drawRect(left,top,left,top)
            self.painterInstance.end()
            # set pixmap onto the label widget

            
            y = top - 15 if top - 15 > 15 else top + 15
            cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
                0.75, (0, 255, 0), 2)
            
            self.painterInstance1 = QtGui.QPainter(self.pixmap_image)
            self.penText=QtGui.QPen(QtCore.Qt.green)
            self.penText.setWidth(2)
            
            
            #to draw the name of recognized person
            self.painterInstance1.setPen(self.penText)   
            
            self.painterInstance1.drawText(left,y,name)
            self.painterInstance1.end()
        
        
            self.camera1.setPixmap(self.pixmap_image)
            self.camera1.show()
       
   

        
     
    def opencamera2(self):        
        # construct the argument parser and parse the arguments
        ap = argparse.ArgumentParser()
        ap.add_argument("-c", "--cascade", required=True,
            help = "path to where the face cascade resides")
        
        ap.add_argument("-e", "--encodings", required=True,
            help="path to serialized db of facial encodings")
             
        args = vars(ap.parse_args('-c haarcascade_frontalface_default.xml -e encodings.pickle'.split()))
           
        data = pickle.loads(open(args["encodings"], "rb").read())
        detector = cv2.CascadeClassifier(args["cascade"])   
        
        # read image in BGR format
        frame1 = self.cap2.read()
        frame1 = imutils.resize(frame1, width=500)
        #frame = imutils.resize(cap2, width=500)
        gray1= cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
        frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB)
        image1 = QImage(frame1, frame1.shape[1], frame1.shape[0], QImage.Format_RGB888)
        pixmap1 = QPixmap.fromImage(image1)
        
        # show image in img_label
        self.camera2.setPixmap(pixmap1)
          
         # convert image file into pixmap
        self.pixmap_image1 = QtGui.QPixmap.fromImage(image1)
       
        # detect faces in the grayscale frame
        rects = detector.detectMultiScale(gray1, scaleFactor=1.1,
            minNeighbors=5, minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE)

        # OpenCV returns bounding box coordinates in (x, y, w, h) order
        # but we need them in (top, right, bottom, left) order, so we
        # need to do a bit of reordering
        boxes = [(y, x + w, y + h, x) for (x, y, w, h) in rects]

        # compute the facial embeddings for each face bounding box
        encodings = face_recognition.face_encodings(frame1, boxes)
        names = []

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
            
            filepath=os.path.join('/home/pi/tapp/account',"%s.json"%name)
            timethen=str(datetime.datetime.now())
            
            #code to READ the data came from camera1 file creation
            with open(filepath,'r') as f:
                content=f.read()
                travel=json.loads(content)

            #code to WRITE the time-ends of journey
            with open(filepath,'w') as f:
                travel.update({'time-ends':timethen})
                f.write(json.dumps(travel,default=lambda x: None))

            #code to READ to find the time in seconds difference
            with open(filepath,'r')as f:
                con=f.read()
                mycon=json.loads(con)
                l1=mycon["time-starts"]
                t1=datetime.datetime.strptime(l1,'%Y-%m-%d %H:%M:%S.%f')
                l2=mycon["time-ends"]
                t2=datetime.datetime.strptime(l2,'%Y-%m-%d %H:%M:%S.%f')
                second=int((t2-t1).total_seconds())
                #print(int(second))

            #function to fetch location2 of customers according to time in second
            def fetch_location(seconds):

                if seconds >=0 & seconds <=60:
                    location2="Surathkal"

                elif seconds >60 & seconds <=120:
                    location2="Manipal"
                elif seconds >120 & seconds <=180:
                    location2="Udupi"

                #print(location2)
                return location2

            location2=fetch_location(second)

            #code to READ the data from file for location2 updation
            with open(filepath,'r') as f:
                content=f.read()
                travel=json.loads(content)

            #code to WRITE the data to file for location2 updation
            with open(filepath,'w') as f:
                travel.update({'location2':location2})
                f.write(json.dumps(travel,default=lambda x: None))

            #code to READ the data from file for fare calculation
            with open(filepath,'r')as f:
                con=f.read()
                mycon=json.loads(con)
                loct1=mycon["location1"]
                loct2=mycon["location2"]

            #dictionary that holds the value in kilometer of each place
            our_location={'Mangalore':0,'Surathkal':10,'Manipal':30,'Udupi':50}

            loc1=int(our_location.get(loct1))
            #print(loc1)
            loc2=int(our_location.get(loct2))
            #print(loc2)

            rate=10
            distance=loc2-loc1
            bill=distance*rate
            #print(bill)

            #code to WRITE the data to file for distance and bill
            with open(filepath,'w') as f:
                travel.update({'distance':distance,'bill':bill})
                f.write(json.dumps(travel,default=lambda x: None))


            #timer=threading.Timer(10.0,fetch_location)
            #timer.start()

        # loop over the recognized faces
        for ((top, right, bottom, left), name) in zip(boxes, names):
            # draw the predicted face name on the image
            cv2.rectangle(frame1, (left, top), (right, bottom),
                (0, 255, 0), 2)
            
            #create painter instance with pixmap
            self.painterInstance2 = QtGui.QPainter(self.pixmap_image1)

            # set rectangle color and thickness
            self.penRectangle = QtGui.QPen(QtCore.Qt.green)
            self.penRectangle.setWidth(2)

            # draw rectangle on painter
            self.painterInstance2.setPen(self.penRectangle)
            self.painterInstance2.drawRect(left,top,left+10,top+10)
            self.painterInstance2.end()
            # set pixmap onto the label widget

            
            y = top - 15 if top - 15 > 15 else top + 15
            cv2.putText(frame1, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
                0.75, (0, 255, 0), 2)
            
            self.painterInstance3 = QtGui.QPainter(self.pixmap_image1)
            self.penText=QtGui.QPen(QtCore.Qt.green)
            self.penText.setWidth(2)
            
            
            #to draw the name of recognized person
            self.painterInstance3.setPen(self.penText)   
            
            self.painterInstance3.drawText(left,y,name)
            self.painterInstance3.end()
        
        
            self.camera2.setPixmap(self.pixmap_image1)
            self.camera2.show()
           
          
    
    def controlTimer2(self):
        url="http://192.168.43.57:8080"
        self.cap2=VideoStream(url+"/video").start()
         
        # self.cap2 = cv2.VideoCapture(url+"/video")
        # self.cap2.set(5, 30)  #set FPS
        # self.cap2.set(3, 640) #set width
        # self.cap2.set(4, 480) #set height             
        # imgResp = requests.get('http://192.168.43.57:8080/shot.jpg')
        # imgNp = np.array(bytearray(imgResp.content),dtype=np.uint8)
        # self.cap= cv2.imdecode(imgNp,cv2.IMREAD_COLOR)
        self.timer2.start(1000./24)
    
           
  
    #close camera on stop buttom
    def closecamera(self):
        self.timer1.stop()
        # release video capture
        self.cap1.release()
        
        self.timer2.stop()
        self.cap2.release()
         
    # def logoutwindow(self):
    #     self.window=QtWidgets.QMainWindow()
    #     self.ui=Ui_MainWindow()
    #     self.ui=setupUi(self.window)
    #     MainWindow.hide()
    #     self.window.showMaximized()         
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MyProg = Prog()
    MyProg.show()
    MyProg.showMaximized()
    # MainWindow = QtWidgets.QMainWindow()
    # ui = Ui_MainWindow1()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    sys.exit(app.exec_())

