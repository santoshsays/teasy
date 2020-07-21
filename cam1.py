#code to run the cam-I : python3 cam1.py
from imutils.video import VideoStream
import cv2,face_recognition,imutils
import argparse,pickle
import os,time,datetime,json,random,string
from itertools import count
#code to pass the argument to the program
ap = argparse.ArgumentParser()
ap.add_argument("-c", "--cascade", required=True, help = "path to where the face cascade resides")
ap.add_argument("-e", "--encodings", required=True, help="path to serialized db of facial encodings")
args = vars(ap.parse_args('-c haarcascade_frontalface_default.xml -e encodings.pickle'.split()))          
data = pickle.loads(open(args["encodings"], "rb").read())
detector = cv2.CascadeClassifier(args["cascade"])
#vs = VideoStream(usePiCamera=True).start()
vs=cv2.VideoCapture(0)
time.sleep(2.0)
main_time=str(datetime.datetime.now())
while True:
    ret,frame = vs.read()
    #frame = imutils.resize(frame, width=500)
    frame = cv2.resize(frame, (500, 400), interpolation = cv2.INTER_CUBIC) 
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
    get_id={}
    get_name={}
    get_id=data["id"]
    get_name=data["names"]
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
            get_index=get_name.index(name)
            id=get_id[get_index]    
        # update the list of names
        names.append(name)
        #code for creating files for verified users 
        if name !="Unknown":
            filepath=os.path.join('/home/pi/tapp/account',"%s.json"%name)
            #update code starts from here
            timenow=str(datetime.datetime.now())
            l1=main_time  
            t1=datetime.datetime.strptime(l1,'%Y-%m-%d %H:%M:%S.%f')
            l2=timenow
            t2=datetime.datetime.strptime(l2,'%Y-%m-%d %H:%M:%S.%f')
            final_time=int(t1-t2).total_seconds())
            def fetch_location(final_time):
                if final_time in range(0,61):
                    location1="Mangalore"
                if final_time in range(61,121):
                    location1="Surathkal"
                if final_time in range(121,181):
                    location1="Manipal"
                if final_time in range(181,241)
                    location1="Udupi"
                return location1
            location1=fetch_location(final_time)
            
            travel={'id':id,'name':name,'time-starts':timenow,'location1':location1,'paid':"false"}
            j=json.dumps(travel,default=lambda x: None)
            with open(filepath,'w+') as f:
                f.write(j)
            f.close()
            with open(filepath,'r') as f:
                f_con=f.read()
                f_mycon=json.loads(f_con)
                show_loc=f_mycon["location1"]
            f.close()
    
        if name=="Unknown":
            un_name="Unknown"
            un_path = '/home/pi/tapp/unknown/'
            cv2.imwrite(os.path.join(un_path , un_name+'.jpg'), frame)
            print("image saved")
            filepath=os.path.join('/home/pi/tapp/account',"%s.json"%un_name)
            timenow=str(datetime.datetime.now())
            travel={'id':"Un",'name':un_name,'time-starts':timenow,'location1':"Mangalore"}
            j=json.dumps(travel,default=lambda x: None)
            with open(filepath,'w+') as f:
                f.write(j)   
            f.close()
            with open(filepath,'r') as f:
                f_con=f.read()
                f_mycon=json.loads(f_con)
                show_loc=f_mycon["location1"]
            f.close()           

    # loop over the recognized faces
    for ((top, right, bottom, left), name) in zip(boxes, names):
        if name !="Unknown":       
            cv2.rectangle(frame, (left, top), (right, bottom),
                (0, 255, 0), 2)
            y = top - 15 if top - 15 > 15 else top + 15
            cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
                0.75, (0, 255, 0), 2)
            x = bottom + 15 if bottom + 15 > 15 else bottom - 15
            cv2.putText(frame, show_loc, (left, x), cv2.FONT_HERSHEY_SIMPLEX,
                0.75, (0, 255, 0), 2)
        else:
            cv2.rectangle(frame, (left, top), (right, bottom),
                (0,0,255), 2)
            y = top - 15 if top - 15 > 15 else top + 15
            cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
                0.75, (0,0,255), 2)
            x = bottom + 15 if bottom + 15 > 15 else bottom - 15
            cv2.putText(frame, show_loc, (left, x), cv2.FONT_HERSHEY_SIMPLEX,
                0.75, (0,0,255), 2)        
    # display the image to our screen
    cv2.imshow("CameraI", frame)
    cv2.moveWindow("CameraI", 310,200)    
    #cv2.namedWindow('CameraI',cv2.WND_PROP_FULLSCREEN)
    #cv2.setWindowProperty('CameraI', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)   
    #cv2.resizeWindow("Camera I", 500, 500)   
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
    #un_name=run_once()
vs.release()
cv2.destroyAllWindows()
#vs.stop()
