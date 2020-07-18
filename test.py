# filepath=glob.glob((args["dataset"]))
# print(filepath)
#latestfile=max(filepath, key=os.path.getctime)
#print(latestfile)

import random,string
from itertools import count
def run_once():
    un_name = "Usr_"+''.join(random.choice(string.ascii_lowercase) for i in range(12))
    print(un_name)
    return un_name
    run_once.func_code = (lambda:None).func_code
#un_name=run_once()

# for i in count():
#     if i==0:
#         run_once()

# name="Unknown"
# if name=="Unknown":
#     x=1
#     while x:
#         print("in while")
#         run_once()
#         x=0
    
# fp="/home/pi/tapp/account/"
# name="santosh"
# x=fp+name+".json"
# print(x)
    
# while 1:
#     if name:
#         run_once()
#         name=None
