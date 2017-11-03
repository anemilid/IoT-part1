import socket
def call_server_socket(imgPath,distance,output):
    list_person_data=[]
    s = socket.socket()         
    host = "ec2-54-175-3-72.compute-1.amazonaws.com"
    port = 65535
    s.connect((host, port))
    fileReader=open("/home/pi/IOT/AWS/id_database.txt","r")
    line=fileReader.readline()
    while(line):
        list_person_data=line.split(" ")
        if (list_person_data[0]==output):
            dist_range=list_person_data[2].split("-")
            print dist_range
            mini=dist_range[0]
            maxi=dist_range[1]
            print distance
            print mini,maxi
            if(str(distance)>=mini and str(distance)<=maxi):
                print "matched"
                f=open(imgPath,"rb")
                bytes_read=f.read()
                while(bytes_read):
                    s.send(bytes_read)
                    bytes_read=f.read()
                f.close()
                s.close()
                s = socket.socket() 
                s.connect((host, port))
                details=str(distance)+"cm"+","+output+","+list_person_data[1]+","+list_person_data[3]+","+list_person_data[4]
                s.send(details)
                s.close()
                return "1"
                print "sent image"
            else:
                return "0"
                print "please try again"
        else:
            print "trying for next match"
            line=fileReader.readline()
    return "0"
            
                
            
        
    
        
