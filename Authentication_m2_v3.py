from image_capture_v2 import *
from server_poll import *
from subprocess import call
from tts_service_amazon import *
from gesture import *
import subprocess
import os
import sys
import socket
from cv_testing import *
sys.path.insert(0,"/home/pi/IOT/FaceRecognition")
import face_recognition 

frames=5
supported_frame_rate=5
sys.path.insert(0,"/home/pi/IOT/AWS")
from client_m2_v3 import *

s = socket.socket()         
host = "ec2-54-175-3-72.compute-1.amazonaws.com"
port = 65534
#s.connect((host, port))

imagePath,avg_distance=captureImages_openCV("new")
auth=gesture_meth()
print auth
print imagePath
output=face_recognition.call_All_V2(imagePath)
print output
fileReader=open("/home/pi/IOT/AWS/id_database.txt","r")
line=fileReader.readline()
while(line):
    list_person_data=line.split(" ")
    if (list_person_data[0]==output):
        dist_range=list_person_data[2].split("-")
        print dist_range
        mini=dist_range[0]
        maxi=dist_range[1]
        print avg_distance
        print mini
        print maxi
        print "str(distance)",str(avg_distance)
        if(str(avg_distance)>=mini and str(avg_distance)<=maxi and auth=="HI"):
            print "sending connection for details"
            details=str(avg_distance)+"cm"+","+output+","+list_person_data[1]+","+list_person_data[3]+","+list_person_data[4]
            print details
            s.send(details)
            s.close()
            break
        else:
            print "not able to authorize"
            break
    else:
        line=fileReader.readline()
for i in range(0,frames): 
    imagePath,avg=captureImages_openCV(i)
    print imagePath
    if frames > supported_frame_rate:
        check="y"
    else:
        check="N"
    print output+" is home! and captured at a distance of "+str(avg_distance)+" cm"
    next_image_check=call_server_socket(imagePath,avg_distance,output,check,i)
    print "next_image_check==",next_image_check
    if(next_image_check=="NI"):
        print "next image"
        continue
    else:
        if next_image_check=="OK":
            text="Welcome Home,"+output
            tts_amazon(text)
        else:
            text="System doesnot recognize you,try again"
            tts_amazon(text)
            
        
        
        
        
        
