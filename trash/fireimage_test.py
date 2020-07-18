import pyrebase
import os, glob, pathlib, shutil, re
import urllib.request
#code to check internet connection is there or not
def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        return False
# test
if not connect():
    print("No Internet")

else:
    print("Connection Established")
    #configuration files for firebase connection
    config ={
        "apiKey": "AIzaSyDgAIVv_SWz8FC95IBeH3J0iivg3381spE",
        "authDomain": "travelsystem-cc1001.firebaseapp.com",
        "databaseURL": "https://travelsystem-cc1001.firebaseio.com",
        "projectId": "travelsystem-cc1001",
        "storageBucket": "travelsystem-cc1001.appspot.com",
        "serviceAccount": "/home/pi/tapp/travelsystem-cc1001-firebase-adminsdk-53xdy-0848a10b6f.json",
        "messagingSenderId": "1043451675138",
        "appId": "1:1043451675138:web:a9c1768ea4013f4775dd1b",
        "measurementId": "G-P3L6218XWX"
        }
    #initiializing firebase connection
    firebase=pyrebase.initialize_app(config)
    storage=firebase.storage()
    #path for downloading all the images from db
    original = '/home/pi/tapp/firebase/'
    #path to store the final image folder to pass for encodings
    dest =  '/home/pi/tapp/dataset/'
    #code to donwload the data from firebase
    all_files = storage.child().list_files()
    for file in all_files:
        try:
            file.download_to_filename(original + file.name)
        except:
            print('Download Failed')
    # function to create direcoty for image file and move file in that
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
    print("all done")
    #code to call the encoding program 
    os.system('python3 encodes_faces_test.py')
    print("caling done")




