from image_capture_v2 import *
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
port = 65534
frames=5
supported_frame_rate=3
sys.path.insert(0,"/home/pi/IOT/AWS")
from client_m2_v2 import *
from facematch import *
for i in range(0,frames):
    imagePath,distance=capture_Images(i)
    output=main(imagePath,"home")
    if frames > supported_frame_rate:
        check="y"
    else:
        check="N"
    if output=="No face matches detected":
        print output

    elif output=="No faces detected":
        print output
    else:
        print output+" is home! and captured at a distance of "+str(distance)+" cm"
        next_image_check=call_server_socket(imagePath,distance,output,check,i)
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
            
        
        
        
        
        
