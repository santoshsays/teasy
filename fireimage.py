import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os, glob, pathlib, shutil, requests,re
import urllib.request
def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        return False
if not connect():
    print("No Internet")
else:
    #print("Connection Established")
    # Use a service account
    cred = credentials.Certificate('digitaltravel-6cb10-firebase-adminsdk-l5pld-97a2c4bf6a.json')
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    Dict={}
    my_dict={}
    users_ref = db.collection(u'userdata')
    docs = users_ref.stream()
    for doc in docs:
        Dict=doc.to_dict()
        my_dict=Dict["image"]
        #print(my_dict)
        for item in my_dict:
        #print(item)
            with open("fire1.txt","a+") as f:
                f.write(item + "\n")
            f.close()
    f1=open("fire1.txt","r+")
    f2=open("fire2.txt")
    f_list=[]
    d_list=[]
    for line in f1:
        #print(line)
        f_list.append(line.rstrip())
    for line in f2:
        if line.rstrip() in f_list:
            f_list.remove(line.rstrip())
    f2=open("fire2.txt","a")
    f3=open("fire3.txt","a")
    for elet in f_list:
        f2.write(elet + "\n")
        f3.write(elet + "\n")   
    f1.truncate(0) #delete the contents of f1
    f1.close()
    f2.close()
    f3.close()
    f3=open("fire3.txt","r+")
    for line3 in f3:
        d_list.append(line3.rstrip())
    #print(d_list)
    f3.truncate(0) #delete the contets of f3
    f3.close()
    if not d_list:
        #pass
        print("No new images to be Download")
    else:
        #print("We have images to be Download")        
        original = '/home/pi/tapp/firebase/'
        dest =  '/home/pi/tapp/dataset/'
        for url in d_list:
            #print(url)
            name = url.split('/')[-1]
            fname=re.split("\?",name)
            filename=fname[0]+".jpg"
            #print(filename)
            r = requests.get(url, allow_redirects=True)
            open(original+filename, 'wb').write(r.content)
        def createdirandmovefile(original):
            if os.path.isdir(original):
                for given_name in glob.glob(original +'/*.jpg'):
                    only_filename = os.path.splitext(given_name)
                    my_path = pathlib.PurePath(only_filename[0])
                    dir_with_id = my_path.name
                    folder_name = re.split("\-", dir_with_id)
                    #user_id = folder_name[0]
                    new_folder_name = folder_name[0]
                    makefolder = os.path.join(original,new_folder_name)
                    try:
                        os.makedirs(makefolder,exist_ok=True)
                    except OSError as error:
                        print('file_exist')
                    shutil.move(given_name,makefolder)
            else:
                print('error')
        createdirandmovefile(original)
        #function to move all the files from orginal to dest
        def moveallfilesindir(original, dest):    
            if os.path.isdir(original) and os.path.isdir(dest):
                for filepath in glob.glob(original + '/*'):          
                    if filepath not in glob.glob(dest + '/*'):
                        try:
                            shutil.move(filepath, dest)
                        except OSError as error:
                            print()
            else:
                print("error")
        moveallfilesindir(original,dest)
        #code to delete the files in the orginal path
        delete_all_files = glob.glob(original +'/*')
        for deletefile in delete_all_files:
            try:
                shutil.rmtree(deletefile)
            except OSError as error:
                print('already_deleted')
        #code to call the encoding program 
        print("Caling Encoding")
        os.system('python3 encode_faces.py')
       
    
            