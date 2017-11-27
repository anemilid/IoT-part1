import socket
import os
import cv2
def call_server_socket(imgPath,distance,output,check,i):
    list_person_data=[]
    s = socket.socket()         
    host = "ec2-54-175-3-72.compute-1.amazonaws.com"
    port = 65534
    s.connect((host, port))
    auth_status="NA"
    bytes_send=0
    while(line):
        list_person_data=line.split(" ")
        if (list_person_data[0]==output):
            dist_range=list_person_data[2].split("-")
            print dist_range
            mini=dist_range[0]
            maxi=dist_range[1]
            print distance
            print mini
            print maxi
            print "str(distance)",str(distance)
            if(str(distance)>=mini and str(distance)<=maxi):
                print "matched"
                size=os.path.getsize(imgPath)
                print "size=",size
                if check =="y":
                    newImageName="Guest"+str(i)+"_c.jpg"
                    a=cv2.imread(imgPath)
                    cv2.imwrite(newImageName,a,[int(cv2.IMWRITE_JPEG_QUALITY),50])
                f=open(newImageName,"rb")
                bytes_read=f.read()
                while(bytes_read):
                    l=s.send(bytes_read)
                    bytes_send=bytes_send+l
                    bytes_read=f.read()
                print "bytes_send",bytes_send
                f.close()
                s.close()
                print "sending connection for details"
                s = socket.socket() 
                s.connect((host, port))
                print "sending connection for details"
                details=str(distance)+"cm"+","+output+","+list_person_data[1]+","+list_person_data[3]+","+list_person_data[4]
                s.send(details)
                print "waiitng for signal"
                next_image_check=s.recv(100)
                print "got it"
                return next_image_check
                #print "sent image"
            else:
                return ""
                print "please try again"
        else:
            print "trying for next match"
            line=fileReader.readline()
    return ""

        
    
        
