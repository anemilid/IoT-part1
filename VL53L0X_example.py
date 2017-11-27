import time
import VL53L0X

def getDistance():
    tof = VL53L0X.VL53L0X()

    tof.start_ranging(VL53L0X.VL53L0X_BETTER_ACCURACY_MODE)

    timing = tof.get_timing()
    if (timing < 20000):
        timing = 20000
    #print ("Timing %d ms" % (timing/1000))
    sum=0;
    for count in range(1,51):
        distance = tof.get_distance()
        if (distance > 0):
            sum+=distance;
            #print ("%d mm, %d cm, %d" % (distance, (distance/10), count))
        time.sleep(timing/1000000.00)
    avg_distance=(sum/50);
    avg_distance=avg_distance/10

    tof.stop_ranging()
    return avg_distance

