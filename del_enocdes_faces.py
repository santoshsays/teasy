import pickle,argparse,re
ap = argparse.ArgumentParser()
ap.add_argument("-e", "--encodings", required=True,
	help="path to serialized db of facial encodings")
args = vars(ap.parse_args('-e un_encodings.pickle'.split())) 

d_name={}
d_encod={}
d_id={}
#f_enc = open(args["encodings"], "rb+")
f_enc = open("un_encodings.pickle","rb+")
e_data=pickle.load(f_enc)

d_encod=e_data["encodings"]
d_name=e_data["names"]
d_id=e_data["id"]
print(d_name)
for d_item in d_name:
    find_name=(re.search("^Unknown_.*",d_item)).group()
    print(find_name)
    try:
        del_index=d_name.index(find_name)
        del d_encod[del_index]
        del d_name[del_index]
        del d_id[del_index]
    except ValueError:
        print("List does not contain value")           
f_enc.close()

#code to write remainig data in pickle file
f = open(args["encodings"], "wb")
f.write(pickle.dumps(e_data))
print("Writing remainig encoded data")
f.close()
#code to see the remainig data in pickle file
c_name={}
c_enc = open(args["encodings"], "rb")
c_data=pickle.load(c_enc)
print("Openning for checking remainig encoded data")
c_name=c_data["names"]
print(c_name)
c_enc.close()