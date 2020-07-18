import os, glob, pathlib, shutil, re
original = '/home/pi/tapp/datatest/'
#original = '/home/pi/tapp/unknown/'
#function to create direcoty for image file and move file in that
def createdirandmovefile(original):
    if os.path.isdir(original):
        for given_name in glob.glob(original +'/*.jpg'):
            only_filename = os.path.splitext(given_name)
            print(only_filename)
            my_path = pathlib.PurePath(only_filename[0])
            print(my_path)
            dir_with_id = my_path.name
            print(dir_with_id)
            folder_name = re.split("\-", dir_with_id)
            new_folder_name = folder_name[0]
            print(new_folder_name)
            #user_id = folder_name[1]
            makefolder = os.path.join(original,new_folder_name)
            try:
                os.makedirs(makefolder,exist_ok=True)
            except OSError as error:
                print('file_exist')
            #target=makefolder
            shutil.move(given_name,makefolder)
    else:
        print('error')
createdirandmovefile(original)

def createdirandmovefile1(original):
    if os.path.isdir(original):
        for given_name in glob.glob(original +'/*.jpg'):
            only_filename = os.path.splitext(given_name)
            print(only_filename)
            my_path = pathlib.PurePath(only_filename[0])
            print(my_path)
            new_folder_name = my_path.name
            print(new_folder_name)
            makefolder = os.path.join(original,new_folder_name)
            try:
                os.makedirs(makefolder,exist_ok=True)
            except OSError as error:
                print('file_exist')
            target=makefolder
            shutil.move(given_name,target)
    else:
        print('error')
#createdirandmovefile1(original)