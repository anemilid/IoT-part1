import cv2
import os
import numpy as np
from cv_testing import *

subjects = ["", "Anusha","Harshitha","Teja"]
lbh_face_recognizer = cv2.face.createLBPHFaceRecognizer()

def detect_face(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5);
    if (len(faces) == 0):
        return None, None
    (x, y, w, h) = faces[0]
    return gray[y:y+w, x:x+h], faces[0]

def prepare_training_data(data_folder_path):

    dirs = os.listdir(data_folder_path)
    faces = []
    labels = []
    for dir_name in dirs:
        if not dir_name.startswith("s"):
            continue;
        label = int(dir_name.replace("s", ""))
        subject_dir_path = data_folder_path + "/" + dir_name
        subject_images_names = os.listdir(subject_dir_path)
        for image_name in subject_images_names:
            if image_name.startswith("."):
                continue;
            image_path = subject_dir_path + "/" + image_name
            image = cv2.imread(image_path)
            #cv2.imshow("Training on image...", image)
            cv2.waitKey(100)
            face,rect = detect_face(image)
            if face is not None:
                faces.append(face)
                labels.append(label)
    return faces, labels
def train_Model():
    
    print("Preparing data...")
    faces, labels = prepare_training_data("/home/pi/IOT/FaceRecognition/training_data")
    print("Data prepared")
    print("Total faces: ", len(faces))
    print("Total labels: ", len(labels))
    lbh_face_recognizer.train(faces, np.array(labels))
    
def draw_rectangle(img, rect):
    (x, y, w, h) = rect
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
def draw_text(img, text, x, y):
    cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)
    
def predictor(test_img):
    
    img=cv2.imread(test_img)
    if img is None:
        print "Please select a valid image"
        return "Please select a valid image"
    img = img.copy()
    face, rect= detect_face(img)
    if face is not None:   
        label= lbh_face_recognizer.predict(face)
        print label
        if(label[1]>75):
            print "The system is not able to recognise you"
            return "The system is not able to recognise you"
        else:
            label_text = subjects[label[0]]
            draw_rectangle(img, rect)
            draw_text(img, label_text, rect[0], rect[1]-5)
            #cv2.imshow("face detected",img)
            #cv2.waitKey(0)
            #cv2.destroyAllWindows()
            print "Hello! This is :"+label_text
            return label_text
    else:
        print "No face detected"
        return "No face detected"
 
    #return img



def call_All_V2(imagePath):
    #imagePath=captureImages_openCV(imagePath)
    #ubjects.append(name)
    train_Model()
    label=predictor(imagePath)
    return label

def call_All(imagePath,name):
    subjects.append(name)
    train_Model()
    label=predictor(imagePath)
    return label
    
    
if __name__=="__main__":
    call_All_V2("testing.jpg")
    

