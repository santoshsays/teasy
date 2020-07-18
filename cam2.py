#python program to run second camera and send account report to db
from imutils.video import VideoStream
import cv2,face_recognition,imutils
import argparse,pickle
import os,time,datetime,json,ast,random,string
from itertools import count
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
#code to configure the firebase admin
cred = credentials.Certificate('digitaltravel-6cb10-firebase-adminsdk-l5pld-97a2c4bf6a.json')
firebase_admin.initialize_app(cred)
db = firestore.client()
#code for declaring Argument Parser
ap = argparse.ArgumentParser()
ap.add_argument("-c", "--cascade", required=True,
    help = "path to where the face cascade resides")
ap.add_argument("-e", "--encodings", required=True,
    help="path to serialized db of facial encodings")
args = vars(ap.parse_args('-c haarcascade_frontalface_default.xml -e encodings.pickle'.split()))          
data = pickle.loads(open(args["encodings"], "rb").read())
detector = cv2.CascadeClassifier(args["cascade"])
#url="http://192.168.43.30:8080"
#vs = VideoStream(url+"/video").start()
vs = VideoStream(0).start()
time.sleep(2.0)
while True:
    frame = vs.read()
    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    rects = detector.detectMultiScale(gray, scaleFactor=1.1,
        minNeighbors=5, minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE)
    # OpenCV returns bounding box coordinates in (x, y, w, h) order
    # but we need them in (top, right, bottom, left) order, so we
    # need to do a bit of reordering
    boxes = [(y, x + w, y + h, x) for (x, y, w, h) in rects]
    encodings = face_recognition.face_encodings(rgb, boxes)
    names = []
    # loop over the facial embeddings
    for encoding in encodings:
        # attempt to match each face in the input image to our known encodings
        matches = face_recognition.compare_faces(data["encodings"],encoding)
        name = "Unknown"
        # check to see if we have found a match
        if True in matches:
            # find the indexes of all matched faces then initialize a
            # dictionary to count the total number of times each face was matched
            matchedIdxs = [i for (i, b) in enumerate(matches) if b]
            counts = {}
            # loop over the matched indexes and maintain a count for each recognized face face
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
        f.close()
        #code to WRITE the time-ends of journey
        with open(filepath,'w') as f:
            travel.update({'time-ends':timethen})
            f.write(json.dumps(travel,default=lambda x: None))
        f.close()
        #code to READ to find the time in seconds difference
        with open(filepath,'r')as f:
            con=f.read()
            mycon=json.loads(con)
            l1=mycon["time-starts"]
            t1=datetime.datetime.strptime(l1,'%Y-%m-%d %H:%M:%S.%f')
            l2=mycon["time-ends"]
            t2=datetime.datetime.strptime(l2,'%Y-%m-%d %H:%M:%S.%f')
            seconds=int((t2-t1).total_seconds())
            print(int(seconds))
        f.close()
        #function to fetch location2 of customers according to time in second
        def fetch_location(seconds):
            if seconds >=0 & seconds <=60:
                location2="Surathkal"
            if seconds >60 & seconds <=120:
                location2="Manipal"
            if seconds >120 & seconds <=180:
                location2="Udupi"
            if seconds >180:
                location2="Batkal"
            return location2
        location2=fetch_location(seconds)
        print(location2)
        #code to READ the data from file for location2 updation
        with open(filepath,'r') as f:
            content=f.read()
            travel=json.loads(content)
        f.close()
        #code to WRITE the data to file for location2 updation
        with open(filepath,'w') as f:
            travel.update({'location2':location2})
            f.write(json.dumps(travel,default=lambda x: None))
        f.close()
        #code to READ the data from file for fare calculation
        with open(filepath,'r')as f:
            con=f.read()
            mycon=json.loads(con)
            loct1=mycon["location1"]
            loct2=mycon["location2"]
        f.close()
        #dictionary that holds the value in kilometer of each place
        our_location={'Mangalore':0,'Surathkal':10,'Manipal':30,'Udupi':50,'Batkal':70}
        loc1=int(our_location.get(loct1))
        loc2=int(our_location.get(loct2))
        rate=5 # Rs 5 per Km
        distance=loc2-loc1
        bill=distance*rate
        #code to WRITE the data to file for distance and bill
        with open(filepath,'w') as f:
            travel.update({'distance':distance,'bill':bill})
            f.write(json.dumps(travel,default=lambda x: None))
        f.close()
        #code to READ the data to file for bill & name
        with open(filepath,'r') as f:
            f_con=f.read()
            f_data=json.loads(f_con)
            show_bill=f_data["bill"]
            show_name=f_data["name"]
            print(show_bill)
        f.close()
        #code to send the data to cloud firestore
        # for i in count():
        #     if i==0:
        fp="/home/pi/tapp/account/"
        with open(fp+show_name+".json","r") as fs:
            fs_r=fs.read()
            fs_data=json.loads(fs_r)
            #send_id=fs_data["id"]
            data = {
                u'user-id': fs_data["id"],
                u'name': fs_data["name"],
                u'time-starts': fs_data["time-starts"],
                u'location1': fs_data["location1"],
                u'time-ends': fs_data["time-ends"],
                u'location2': fs_data["location2"],
                u'distance': fs_data["distance"],
                u'bill': fs_data["bill"],
                u'paid':u'false'
            } 
        fs.close()  
        #code to generate  26 CHARACTERS Random Document name
        def run_once():
            un_name =''.join(random.choice(string.ascii_uppercase) for i in range(26))
            print(un_name)
            return un_name
            run_once.func_code = (lambda:None).func_code
        user_id=run_once()         
        db.collection(u'useraccount').document(user_id).set(data)
        print("Data Sent to Firebase")
        #db.collection(u'useraccount').document(send_id).set(data)    
    # loop over the recognized faces
    for ((top, right, bottom, left), name) in zip(boxes, names): 
        pay=str(show_bill)
        cv2.rectangle(frame, (left, top), (right, bottom),
            (0, 255, 0), 2)
        y = top - 15 if top - 15 > 15 else top + 15
        cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
            0.75, (0, 255, 0), 2)
        x = bottom + 15 if bottom + 15 > 15 else bottom - 15
        #time.sleep(2.0)
        cv2.putText(frame, pay, (left, x), cv2.FONT_HERSHEY_SIMPLEX,
            0.75, (0, 255,0), 2)       
    # display the image to our screen
    cv2.imshow("Camera II", frame)
    cv2.moveWindow("Camera II", 840,200)    
    #cv2.resizeWindow(winname, width, height)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
cv2.destroyAllWindows()
vs.stop()