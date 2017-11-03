import socket
import time
import os
host = socket.gethostname()
s = socket.socket()
port = 65535
s.bind((host, port))
f=open("guest.jpg","wb")
s.listen(5)
while True:
   f=open("guest.jpg","wb")
   c, addr = s.accept()
   while True:
       data=c.recv(1000)
       if not data:
           break
       f.write(data)
   f.close()
   c.close()
   c,addr=s.accept()
   f=open("details.txt","w")
   details=c.recv(100)
   print details
   f.write(details)
   f.close()
   c.close()
   c, addr = s.accept()
   print "connection from client"
   with open('guest.jpg', 'rb') as inf:
       jpgdata = inf.read()
       c.send(jpgdata)
   inf.close()
   c.close()
   c, addr = s.accept()
   with open('details.txt', 'r') as inf:
       textdata = inf.read()
       print textdata
       c.send(textdata)
   inf.close()
   c.close()
   c, addr = s.accept()
   with open('auth_status.txt', 'w') as inf:
       textdata = c.recv(100)
       print textdata
       #textdata=textdata.decode("utf8")
       if textdata == '1':
           inf.write("OK")
       else:
           inf.write("CANCEL")
       print textdata
   inf.close()
   c.close()
   c, addr = s.accept()
   print "got connection for deleting the file"
   read_boolean=c.recv(100)
   print read_boolean
   if read_boolean=="1":
       print "deleting"
       os.remove("/home/ec2-user/auth_status.txt")
