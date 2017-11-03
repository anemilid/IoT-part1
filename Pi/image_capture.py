from subprocess import call
import os
import time
from VL53L0X_example import *

def capture_Images():
    
    imagename="Guest"+str(time.time())+"jpg"
    call(["fswebcam",imagename])
    avg_distance=getDistance()
    return imagename,avg_distance
    
    
if __name__=="__main__":
    capture_Images();
