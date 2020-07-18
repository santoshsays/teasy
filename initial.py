import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import urllib.request
import os
def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        return False
if not connect():
    print("No Internet")
else:
    count=0
    print("Connection Established")
    cred = credentials.Certificate('digitaltravel-6cb10-firebase-adminsdk-l5pld-97a2c4bf6a.json')
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    
    #code to check if there is new data or not
    users_ref = db.collection(u'userdata')
    docs = users_ref.stream()
    for doc in docs:
        count=count+1
    #print(count)
    #file to hold the count of the db
    file0='/home/pi/tapp/db_count.txt'
    f0=open(file0,'r+')
    for line0 in f0:
        if count > int(line0):
            with open(file0,'w')as fw:
                fw.write(str(count))
            fw.close()
            print("Started Donloading Face Data")
            os.system('python3 fireimage.py')
        elif count == int(line0):
            print("No new Face Data Found")
    f0.close()
    
    #code to check whwther there is any id in detete colletction
    d_count=0
    del_ref=db.collection(u'deleteduser')
    d_docs=del_ref.stream()
    for d_doc in d_docs:
        d_count=d_count+1
    if d_count >1:
        print("User Found for Delting")
        os.system('python3 delete_user.py')