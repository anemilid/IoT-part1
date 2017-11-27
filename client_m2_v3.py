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
    if check =="y":
        newImageName="Guest"+str(i)+"_c.jpg"
        a=cv2.imread(imgPath)
        cv2.imwrite(newImageName,a,[int(cv2.IMWRITE_JPEG_QUALITY),50])
        imgPath=newImageName
    print "in soc",imgPath
    f=open(imgPath,"rb")
    bytes_read=f.read()
    while(bytes_read):
        l=s.send(bytes_read)
        bytes_send=bytes_send+l
        bytes_read=f.read()
        print "bytes_send",bytes_send
    f.close()
    s.close()
    s = socket.socket() 
    s.connect((host, port))
    next_image_check=s.recv(100)
    return next_image_check

        
    
        
