import os
from firebase import firebase
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
    #print("Internet Connetion")
    fbcon = firebase.FirebaseApplication('https://digitaltravel-6cb10.firebaseio.com/', None)
    # data_to_upload={"id":123, "name": "prabal", "time-starts": "2020-05-27 00:37:40.649508", "location1": "Mangalore"}
    # result=fbcon.post('/user_data/',data_to_upload)
    #code to get all the contents from db
    getresult=fbcon.get('/userdata/',None)
    count=0
    #loop to iterate through the contents of the db
    for ids in getresult:
        count=count+1
    print(count)
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

# mostrecentKeyId=0
# mostrecentid=0
# for keyId in getresult:
#     if getresult[keyId]['id'] > mostrecentid:
#         mostrecentid=getresult[keyId]['id']
#         mostrecentKeyId=getresult[keyId]
            
# newresult=getresult[keyId]['id']
# print(newresult)
        