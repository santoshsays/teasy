import os, glob, pathlib, shutil, requests,re
#image_url="https://firebasestorage.googleapis.com/v0/b/digitaltravel-6cb10.appspot.com/o/1_mithun-0?alt=media&token=df65980d-28c8-44c7-a1fa-73f36a62b9a6"
# img_data = requests.get(image_url).content
# with open('image_name.jpg', 'wb') as handler:
#     handler.write(img_data)

original = '/home/pi/tapp/datatest/'
url ='https://firebasestorage.googleapis.com/v0/b/digitaltravel-6cb10.appspot.com/o/1_mithun-0?alt=media&token=df65980d-28c8-44c7-a1fa-73f36a62b9a6'
name = url.split('/')[-1]
fname=re.split("\?",name)
filename=fname[0]+".jpg"
print(filename)

r = requests.get(url, allow_redirects=True)
open(original+filename, 'wb').write(r.content)
print("done")

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
print("file in to folder")