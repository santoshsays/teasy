#program to delete the encoded images of deactivated user as in firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import pickle,argparse
ap = argparse.ArgumentParser()
ap.add_argument("-e", "--encodings", required=True,
	help="path to serialized db of facial encodings")
args = vars(ap.parse_args('-e encodings.pickle'.split()))
        
cred = credentials.Certificate('digitaltravel-6cb10-firebase-adminsdk-l5pld-97a2c4bf6a.json')
firebase_admin.initialize_app(cred)
db = firestore.client()
dict_1 ={}
dict_2={}

d_name={}
d_encod={}
d_id={}
del_count=0
d_ref=db.collection(u'deleteduser')
del_docs=d_ref.stream()
for del_doc in del_docs:
    del_count=del_count+1
    dict_1=del_doc.to_dict()
    dict_2=dict_1["user-id"]
    #print(dict_2) 
    f_emp = open(args["encodings"], "rb+")
    e_data=pickle.load(f_emp)
    d_encod=e_data["encodings"]
    d_name=e_data["names"]
    d_id=e_data["id"]
    #print(d_id)
    try:
        del_index=d_id.index(dict_2)
        del d_encod[del_index]
        del d_name[del_index]
        del d_id[del_index]
        print("user-id: " + dict_2 + " delted")
    except ValueError:
        print("List does not contain value")   
    f_emp.close()    
    f = open(args["encodings"], "wb")
    f.write(pickle.dumps(e_data))
    print("Writing remainig encoded data")
    f.close()
#code to see the remainig data in pickle file
c_name={}
c_id={}
c_emp = open(args["encodings"], "rb")
c_data=pickle.load(c_emp)
print("Openning for checking remainig encoded data")
c_name=c_data["names"]
print(c_name)
c_id=c_data["id"]
print(c_id)
#code to delete the all documents from firebase
coll_ref=db.collection(u'deleteduser')
batch_size=del_count
def delete_collection(coll_ref, batch_size):
    docs = coll_ref.limit(batch_size).stream()
    deleted = 0
    for doc in docs:
        print(f'Deleting doc {doc.id} => {doc.to_dict()}')
        doc.reference.delete()
        deleted = deleted + 1
    if deleted >= batch_size:
        return delete_collection(coll_ref, batch_size)
if batch_size>1:   
    delete_collection(coll_ref, batch_size)
else:
    print("Nothing to delete")
