# import pickle,argparse,re
# ap = argparse.ArgumentParser()
# ap.add_argument("-e", "--encodings", required=True,
# 	help="path to serialized db of facial encodings")
# args = vars(ap.parse_args('-e encodings.pickle'.split())) 
# c_name={}
# c_enc = open(args["encodings"], "rb")
# c_data=pickle.load(c_enc)
# print("Openning for checking remainig encoded data")
# c_name=c_data["names"]
# print(c_name)
# c_enc.close()
import os
from firebase import firebase
fbcon = firebase.FirebaseApplication('https://digitaltravel-6cb10.firebaseio.com/', None)
data_to_upload={"id":123, "name": "prabal", "time-starts": "2020-05-27 00:37:40.649508", "location1": "Mangalore"}
result=fbcon.post('/user_data/',data_to_upload)