import os

os.system('python3 pi_face_recognition.py --cascade haarcascade_frontalface_default.xml --encodings encodings.pickle && python3 webcam_recognition.py --cascade haarcascade_frontalface_default.xml --encodings encodings.pickle')

