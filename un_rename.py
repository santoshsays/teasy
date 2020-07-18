#code to rename the unkonw name in increasing  order
import os,pathlib,glob,shutil,re,json,time
original = '/home/pi/tapp/unknown/'
finals = '/home/pi/tapp/account/'

originalf = '/home/pi/tapp/unknown/Unknown.jpg'
finalsf = '/home/pi/tapp/account/Unknown.json'
# function to create directry for image file and move file in that
def createdirandmovefile1(original,finals):
    if os.path.isdir(original) & os.path.isdir(finals):
        org=glob.glob(original +'/Unknown.jpg')
        fin=glob.glob(finals +'/Unknown.json')
        for given_name,act_name in zip(org,fin):
            with open("un_count.txt","r+")as f:
                for prev_count in f:
                    last_count=int(prev_count)+1
            f.close()
            #code to rename the json file
            a_name=os.path.splitext(act_name)[0]
            a_ext=os.path.splitext(act_name)[1]
            only_a_name=a_name +"-"+ prev_count
            only_id="Un"+prev_count 
            updt_name = pathlib.PurePath(os.path.splitext(only_a_name)[0]).name
            n_a_name=a_name +"-"+ prev_count + a_ext
            #code to change name in dictionary as file
            with open(act_name,'r')as fr:
                content=fr.read()
                trvl=json.loads(content)
            fr.close()
            with open(act_name,'w') as fw:
                trvl.update({'name':updt_name})
                trvl.update({'id':only_id})
                fw.write(json.dumps(trvl,default=lambda x: None))
            fw.close()  
            #code to rename the json file
            os.rename(act_name,n_a_name)
 
            #code to rename the image file        
            f_name=os.path.splitext(given_name)[0]
            f_ext=os.path.splitext(given_name)[1]
            n_f_name=f_name +"-"+ prev_count + f_ext
            os.rename(given_name,n_f_name)
            
            #code to  extract foldername from file & make DIR
            folder_name = pathlib.PurePath(os.path.splitext(n_f_name)[0]).name
            foldr_name=only_id+"_"+folder_name
            print(foldr_name)
            makefolder = os.path.join(original,foldr_name)
            try:
                os.makedirs(makefolder,exist_ok=True)
            except OSError as error:
                print('file_exist')
            shutil.move(n_f_name,makefolder)
            
            #code to upate the counter value for the file_name
            with open("un_count.txt",'w') as f1:
                f1.write(str(last_count))
            f1.close()
    else:
        print('error')
if glob.glob(originalf):
    if glob.glob(finalsf): 
        createdirandmovefile1(original,finals)
        print("Image and json file renamed.. Calling for Enocding")
        #time.sleep(2.0)
        #os.system('python3 enodes_unknown.py')
else:
    print("No Unknown Faces")
