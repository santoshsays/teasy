#program to encodes the unknown faces to encodings pickle file
from imutils import paths
import cv2,face_recognition,argparse,pickle 
import os,pathlib,glob,shutil,re
original = '/home/pi/tapp/unknown/'
dest= '/home/pi/tapp/d_unknown/'
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--dataset", required=True,
	help="path to input directory of faces + images")
ap.add_argument("-e", "--encodings", required=True,
	help="path to serialized db of facial encodings")
ap.add_argument("-d", "--detection-method", type=str, default="cnn",
	help="face detection model to use: either `hog` or `cnn`")
args = vars(ap.parse_args('-i unknown -e encodings.pickle -d hog'.split()))
#code to perform only not modeified user encodings
imagePaths = list(paths.list_images(args["dataset"]))
#print(imagePaths)
#code to write all the file paths to file 
for item in imagePaths:    
    with open("un_alldownload.txt","a") as f:
        f.write(item +"\n")
    f.close()
f1=open("un_alldownload.txt","r+")
f2=open("un_check.txt")
l=[] #list for file comparison 
enc_list=[] # list for encodings
for line in f1:
    l.append(line.rstrip())
for line in f2:
    if line.rstrip() in l:
        l.remove(line.rstrip())
f2=open("un_check.txt","a")
# f2_size=os.path.getsize("check.txt")
f3=open("un_encodes.txt","a")
for ele in l:
    f2.write(ele + "\n")
    f3.write(ele + "\n")   
f1.truncate(0) #delete the contents of f1
f1.close()
f2.close()
f3.close()
f3=open("un_encodes.txt","r+")
for line3 in f3:
    enc_list.append(line3.rstrip())
print(enc_list)
f3.truncate(0) #delete the contets of f3
f3.close()
if not enc_list:
    print("No new images to be encoded")
else:
    # grab the paths to the input images in our dataset
    #print("[INFO] quantifying faces...")
    # initialize the list of known encodings and known names
    knownEncodings = []
    knownNames = []
    knownId = []
    # loop over the image paths
    for (i, imagePath) in enumerate(enc_list):    
        # extract the person name from the image path
        print("[INFO] processing image {}/{}".format(i + 1,
            len(enc_list)))
        dname = imagePath.split(os.path.sep)[-2]
        ndname=re.split("\_", dname)
        id=ndname[0]
        #print(id)
        name=ndname[1]
        print(name)
        # load the input image and convert it from RGB (OpenCV ordering) to dlib ordering (RGB)
        image = cv2.imread(imagePath)
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # detect the (x, y)-coordinates of the bounding boxes
        # corresponding to each face in the input image
        boxes = face_recognition.face_locations(rgb,
            model=args["detection_method"])
        # compute the facial embedding for the face
        encodings = face_recognition.face_encodings(rgb, boxes)
        for encoding in encodings:
            knownEncodings.append(encoding)
            knownNames.append(name)
            knownId.append(id)
    # dump the facial encodings + names to disk
    print("[INFO] serializing encodings...")
    data = {"encodings": knownEncodings, "names": knownNames,"id":knownId} 
    f = open(args["encodings"], "ab")
    f.write(pickle.dumps(data))
    f.close()
    print("Encoding done sucessfully")
    #function to move all the files from orginal to dest
    # def moveallfilesindir(original, dest):   
    #     print("Started Moving Images to Destination Directry") 
    #     if os.path.isdir(original) and os.path.isdir(dest):
    #         for filepath in glob.glob(original + '/*'):          
    #             if filepath not in glob.glob(dest + '/*'):
    #                 try:
    #                     shutil.move(filepath, dest)
    #                 except OSError as error:
    #                     print()
    #     else:
    #         print("error")
    # moveallfilesindir(original,dest)   
    # #code to delete the files in the orginal path
    # delete_all_files = glob.glob(original +'/*')
    # for deletefile in delete_all_files:
    #     try:
    #         shutil.rmtree(deletefile)
    #     except OSError as error:
    #         print('already_deleted')
    # print("all done")   