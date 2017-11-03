from image_capture import *
from server_poll import *
from subprocess import call
from tts_service_amazon import *
import subprocess
import os
import sys
import socket
sys.path.insert(0,"/home/pi/pi-detector/scripts/")
sys.path.insert(0,"/home/pi/pi-detector/scripts/")
host = "ec2-54-175-3-72.compute-1.amazonaws.com"
port = 65535

sys.path.insert(0,"/home/pi/IOT/AWS")
from clientV2 import *
imagePath,distance=capture_Images()
from facematch import *
output=main(imagePath,"home")
if output=="No face matches detected":
    print output

elif output=="No faces detected":
    print output
else:
    print output+" is home! and captured at a distance of "+str(distance)+" cm"
    auth_status=call_server_socket(imagePath,distance,output)
    if(auth_status=="1"):
        while True:
            try:
                subprocess.call(["scp","-i","/home/pi/IOT/VL53L0X_rasp_python/iot_server_anusha.pem","ec2-user@ec2-54-175-3-72.compute-1.amazonaws.com:/home/ec2-user/auth_status.txt","/home/pi/IOT/VL53L0X_rasp_python/python/auth_status.txt"])
                if(os.path.exists("/home/pi/IOT/VL53L0X_rasp_python/python/auth_status.txt")):
                    break
            except:
                print "continue"
        with open("/home/pi/IOT/VL53L0X_rasp_python/python/auth_status.txt","r") as file:
            text=file.read()
        os.remove("/home/pi/IOT/VL53L0X_rasp_python/python/auth_status.txt")
        s=socket.socket()
        s.connect((host,port))
        s.send("1")
        s.close()
        if text=="OK":
            text="Welcome Home,"+output
            tts_amazon(text)
        else:
            text="System doesnot recognize you,try again"
            tts_amazon(text)
        print "before deleting"
        
        
        
        
        
