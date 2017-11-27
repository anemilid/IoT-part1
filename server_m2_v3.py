import socket
import time
import os
host = socket.gethostname()
s = socket.socket()
port = 65534
s.bind((host, port))
f=open("guest.jpg","wb")
s.listen(5)
bytes_rec=0
frames=5
while True:
   conn,addr=s.accept()
   print "got connection for sending details"
   f=open("details.txt","w")
   details=conn.recv(100)
   print details
   f.write(details)
   f.close()
   conn.close()
   for i in range(0,frames):
       f=open("guest"+str(i)+".jpg","wb")
       c2, addr = s.accept()
       while True:
           data=c2.recv(1000)
           bytes_rec=bytes_rec+len(data)
           if not data:
               break
           f.write(data)
       f.close()
       print "bytes_rec",bytes_rec
       print "size of image received",os.path.getsize("guest.jpg")
       c1,addr=s.accept()
       print "hereeee"
       if(i!=0):
           c6.send("0")
       c3, addr = s.accept()
       print "helllooooooo!!"
       print "connection from client"
       with open("guest"+str(i)+".jpg", 'rb') as inf:
           jpgdata = inf.read()
           c3.send(jpgdata)
       inf.close()
       c3.close()
       if(i!=4):
           print i
           c6,addr=s.accept()
           print "got coonection for wait"
           c6.send("1")
           print "sending 1"
           c1.send("NI")
           print "sent NA"
   c3.close()
   c6.close()
   c4,addr=s.accept()
   print "got connection for sending details"
   with open('details.txt', 'r') as inf:
       textdata = inf.read()
       print textdata
       c4.send(textdata)
   c4.close()
   c5, addr = s.accept()
   with open('auth_status.txt', 'w') as inf:
       textdata = c5.recv(100)
       print textdata
       #textdata=textdata.decode("utf8")
       if textdata == '1':
           inf.write("OK")
       else:
           inf.write("CANCEL")
       print textdata
   inf.close()
   c5.close()
   f=open('auth_status.txt', 'r')
   auth_status=f.read()
   c1.send(auth_status)
   c1.close()
