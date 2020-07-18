import sys
import os

import cv2
import argparse
import numpy as np
import face_recognition
#import imutils
import pickle
import json
import time
import ast
import datetime

from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui

# to get the video from camera
class RecordVideo(QtCore.QObject):
    image_data = QtCore.pyqtSignal(np.ndarray)

    def __init__(self, camera_port=0, parent=None):
        super().__init__(parent)
        self.camera = cv2.VideoCapture(camera_port)
        self.camera.set(5, 30)  #set FPS
        self.camera.set(3, 480) #set width
        self.camera.set(4, 480) #set heigh
        self.timer = QtCore.QBasicTimer()

    def start_recording(self):
        self.timer.start(0, self)

    def timerEvent(self, event):
        if (event.timerId() != self.timer.timerId()):
            return

        read, data = self.camera.read()
        if read:
            self.image_data.emit(data)
            
  
# to detet the face 
class FaceDetectionWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        ap = argparse.ArgumentParser()
        ap.add_argument("-c", "--cascade", required=True,
            help = "path to where the face cascade resides")
        # ap.add_argument("-e", "--encodings", required=True,
        #     help="path to serialized db of facial encodings")
        #args = vars(ap.parse_args('-c haarcascade_frontalface_default.xml -e encodings.pickle'.split()))
        args = vars(ap.parse_args('-c haarcascade_frontalface_default.xml'.split()))
        
        #self.datas = pickle.loads(open(args["encodings"], "rb").read())
        self.classifier = cv2.CascadeClassifier(args["cascade"])
        
        self.image = QtGui.QImage()
        self._red = (0, 0, 255)
        self._width = 2
        self._min_size = (30, 30)

    def detect_faces(self, image: np.ndarray):
        # haarclassifiers work better in black and white
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray_image = cv2.equalizeHist(gray_image)

        faces = self.classifier.detectMultiScale(gray_image,scaleFactor=1.3,minNeighbors=4,minSize=(30,30),flags=cv2.CASCADE_SCALE_IMAGE)

        return faces
       
    def image_data_slot(self, image_data):
        faces = self.detect_faces(image_data)
        for (x, y, w, h) in faces:
            cv2.rectangle(image_data,
                          (x, y),
                          (x+w, y+h),
                          self._red,
                          self._width)

        self.image = self.get_qimage(image_data)
        if self.image.size() != self.size():
            self.setFixedSize(self.image.size())

        self.update()

    def get_qimage(self, image: np.ndarray):
        height, width, colors = image.shape
        bytesPerLine = 3 * width
        QImage = QtGui.QImage

        image = QImage(image.data,
                       width,
                       height,
                       bytesPerLine,
                       QImage.Format_RGB888)

        image = image.rgbSwapped()
        return image

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawImage(0, 0, self.image)
        self.image = QtGui.QImage()

    # def face_recognition(self, image: np.ndarray):
    #     frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    #     encodings = face_recognition.face_encodings(frame)
    #     names = []
    #     # loop over the facial embeddings
    #     for encoding in encodings:
    #         # attempt to match each face in the input image to our known
    #         # encodings
    #         matches = face_recognition.compare_faces(self.datas["encodings"],
    #             encoding)
    #         print(matches)
    #         name = "Unknown"
            
        
    #          # check to see if we have found a match
    #         if True in matches:
    #             # find the indexes of all matched faces then initialize a
    #             # dictionary to count the total number of times each face
    #             # was matched
    #             matchedIdxs = [i for (i, b) in enumerate(matches) if b]
    #             print(matchedIdxs)
    #             counts = {}

    #             # loop over the matched indexes and maintain a count for
    #             # each recognized face face
    #             for i in matchedIdxs:
    #                 name = self.datas["names"][i]
    #                 print(name)
    #                 counts[name] = counts.get(name, 0) + 1

    #             # determine the recognized face with the largest number
    #             # of votes (note: in the event of an unlikely tie Python
    #             # will select first entry in the dictionary)
    #             name = max(counts, key=counts.get)
            
    #         # update the list of names
    #         names.append(name)
    
    #         filepath=os.path.join('/home/pi/tapp/account',"%s.json"%name)
    #         timenow=str(datetime.datetime.now())
    #         travel={'id':id,'name':name,'time-starts':timenow,'location1':"Mangalore"}
    #         j=json.dumps(travel,default=lambda x: None)
    #         with open(filepath,'w+') as f:
    #             f.write(j)        
class Thread(QtCore.QThread,QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        QtCore.QThread.__init__(self, *args, **kwargs)
        super().__init__()
        
        ap = argparse.ArgumentParser()
        # ap.add_argument("-c", "--cascade", required=True,
        #     help = "path to where the face cascade resides")
        ap.add_argument("-e", "--encodings", required=True,
            help="path to serialized db of facial encodings")
        #args = vars(ap.parse_args('-c haarcascade_frontalface_default.xml -e encodings.pickle'.split()))
        args = vars(ap.parse_args('-e encodings.pickle'.split()))
        #args = vars(ap.parse_args('-c haarcascade_frontalface_default.xml'.split()))
        
        self.datas = pickle.loads(open(args["encodings"], "rb").read())
        #self.classifier = cv2.CascadeClassifier(args["cascade"])
        
        self.image = QtGui.QImage()
        print(self.image)
        self._red = (0, 0, 255)
        self._width = 2
        #self._min_size = (30, 30)
        
    def run(self,image: np.ndarray):
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        encodings = face_recognition.face_encodings(frame)
        names = []
        # loop over the facial embeddings
        for encoding in encodings:
            # attempt to match each face in the input image to our known
            # encodings
            matches = face_recognition.compare_faces(self.datas["encodings"],
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
                    name = self.datas["names"][i]
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

    # def run(self,image: np.ndarray):
    #     self.face_recognition(self,image: np.ndarray)


 
    
class MainWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.th = Thread(self)
        self.th.start() 
        #fp = haarcascade_filepath
        self.face_detection_widget = FaceDetectionWidget()

        # TODO: set video port
        self.record_video = RecordVideo()

        image_data_slot = self.face_detection_widget.image_data_slot
        self.record_video.image_data.connect(image_data_slot)

        # face_recg=self.face_detection_widget.face_recognition
        # self.record_video.image_data.connect(face_recg)
        
        layout = QtWidgets.QVBoxLayout()

        layout.addWidget(self.face_detection_widget)
        self.run_button = QtWidgets.QPushButton('Start')
        layout.addWidget(self.run_button)

        self.run_button.clicked.connect(self.record_video.start_recording)
        self.setLayout(layout)
    
    def closeEvent(self, event):
        self.th.stop()
        self.th.wait()
        super().closeEvent(event)

# def main(haar_cascade_filepath):
#     app = QtWidgets.QApplication(sys.argv)

#     main_window = QtWidgets.QMainWindow()
#     main_widget = MainWidget()
#     main_window.setCentralWidget(main_widget)
#     main_window.show()
#     sys.exit(app.exec_())

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    main_window = QtWidgets.QMainWindow()
    main_widget = MainWidget()
    main_window.setCentralWidget(main_widget)
    main_window.show()
    #main_window.showMaximized()
    sys.exit(app.exec_())

    
# if __name__ == '__main__':
#     script_dir = path.dirname(path.realpath(__file__))
#     cascade_filepath = path.join(script_dir,
#                                  '..',
#                                  'data',
#                                  'haarcascade_frontalface_default.xml')

#     cascade_filepath = path.abspath(cascade_filepath)
#     main(cascade_filepath)