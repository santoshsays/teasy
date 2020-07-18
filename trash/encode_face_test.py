# python3 encode_faces.py --dataset dataset --encodings encodings.pickle --detection-method hog
from imutils import paths
import face_recognition
import argparse
import pickle
import cv2
import os, pathlib, glob, shutil, re

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--dataset", required=True,
	help="path to input directory of faces + images")
ap.add_argument("-e", "--encodings", required=True,
	help="path to serialized db of facial encodings")
ap.add_argument("-d", "--detection-method", type=str, default="cnn",
	help="face detection model to use: either `hog` or `cnn`")
args = vars(ap.parse_args('-i datatest -e encodings.pickle -d hog'.split()))
#args = vars(ap.parse_args())

# grab the paths to the input images in our dataset
#code to etract the latest image in the dataset
# print("[INFO] quantifying faces...")
# filepath=glob.glob((args["dataset"]))
# latestfile=max(filepath, key=os.path.getctime)
# imagePaths = list(paths.list_images(latestfile))
# print(imagePaths)

imagePaths = list(paths.list_images(args["dataset"]))
print(imagePaths)
# listToStr = ' '.join([str(elem) for elem in imagePaths]) 
# texts=os.path.splitext(listToStr)
# ftexts=pathlib.PurePath(texts[0])
# fname=ftexts.name
# idname=re.split("\_", fname)
# id=idname[0]
# print(id)

# initialize the list of known encodings and known names
knownEncodings = []
knownNames = []
knownId=[]
# loop over the image paths
for (i, imagePath) in enumerate(imagePaths):    
	# extract the person name from the image path
	print("[INFO] processing image {}/{}".format(i + 1,
		len(imagePaths)))
	dname = imagePath.split(os.path.sep)[-2]
	#ndname=re.split("\_", dname)
	#id=ndname[0]
	#print(id)
	#name=ndname[1]
	print(dname)
 	
# 	# load the input image and convert it from RGB (OpenCV ordering)
# 	# to dlib ordering (RGB)
# 	image = cv2.imread(imagePath)
# 	rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# 	# detect the (x, y)-coordinates of the bounding boxes
# 	# corresponding to each face in the input image
# 	boxes = face_recognition.face_locations(rgb,
# 		model=args["detection_method"])
# 	# compute the facial embedding for the face
# 	encodings = face_recognition.face_encodings(rgb, boxes)
# 	for encoding in encodings:
# 		knownEncodings.append(encoding)
# 		knownNames.append(name)
# 		#knownId.append(id)
# # dump the facial encodings + names to disk
# print("[INFO] serializing encodings...")
# data = {"encodings": knownEncodings, "names": knownNames,"id":knownId} #"id":knownId
# f = open(args["encodings"], "ab")
# f.write(pickle.dumps(data))
# f.close()