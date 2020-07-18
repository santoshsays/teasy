import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime,random,string

cred = credentials.Certificate('digitaltravel-6cb10-firebase-adminsdk-l5pld-97a2c4bf6a.json')
firebase_admin.initialize_app(cred)
db = firestore.client()
data = {
    u'user-id': u'1',
    u'name': u'mithun',
    u'time-starts': u'2020-06-26 23:51:29.456582',
    u'location1': u'Mangalore',
    u'time-ends': u'2020-06-26 23:52:29.456582',
    u'location2': u'Surathkal',
    u'distance': u'10',
    u'bill': u'50',
    u'paid':u'false'
    #u'time':datetime.datetime.now()
}
def run_once():
    un_name =''.join(random.choice(string.ascii_uppercase) for i in range(26))
    print(un_name)
    return un_name
    run_once.func_code = (lambda:None).func_code
user_id=run_once()
db.collection(u'useraccount').document(user_id).set(data)
#db.collection(u'useraccount').document(u'user_id').set(data,merge=True)

# db.collection(u'useraccount').document(u'user_id').delete()

