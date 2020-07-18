import os,schedule,time

originalf = '/home/pi/tapp/unknown/Unknown.jpg'
finalsf = '/home/pi/tapp/account/Unknown.json'
#code to call initial.py to check if there is new data
def check_for_new_data():
    print("I'm working...")
    os.system('python3 initial.py')
#schedule.every(5).minutes.do(check_for_new_data)
#code to check if there is uknownn face
def check_unknown_face():
    # print("checking for Unknown Faces")
    os.system('python3 un_rename.py')
#schedule.every(10).seconds.do(check_unknown_face)
#code to call del_enocdes_faces.py at 6-clock everyday
def del_unknown_face():
    print("Started Deleting Unkown Faces")
    os.system('python3 del_encodes_faces.py')
schedule.every().day.at("18:00").do(del_unknown_face)
schedule.every().day.at("18:05").do(del_unknown_face)
schedule.every().day.at("18:10").do(del_unknown_face)
while 1:
    schedule.run_pending()
    time.sleep(1)
# schedule.every(1).minutes.do(job)
# schedule.every().hour.do(job)