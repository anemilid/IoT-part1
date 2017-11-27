from subprocess import call
import os
import time
from VL53L0X_example import *

def capture_Images(i):
    
    imagename="Guest"+str(i)+".jpg"
    call(["fswebcam",imagename])
    avg_distance=getDistance()
    return imagename,avg_distance

def compress_image(imagename,i):
    import cv2
    newImageName="Guest"+str(i)+"_c.jpg"
    a=cv2.imread(r"imagename")
    cv2.imwrite(newImageName,a,[int(cv2.IMWRITE_JPEG_QUALITY),50])
    return newImageName
    
    
if __name__=="__main__":
    capture_Images();

