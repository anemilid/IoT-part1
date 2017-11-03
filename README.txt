Author: ANUSHA NEMILIDINNE
UH email address: anemilidinne@uh.edu
Your ID: 1619484

Implementation details:

Prerequisites:

1.Set up amazon AWS account
2.Launch ec2 instance
3.Create IAM user roles and adding policy permissions.
4.creation of buckets.

Hardware:

1.raspberry pi 2
2.VL53L0X time of flight distance sensor
3.webcam
4.8 GB memory card

IDE used:

1.python 2.7
2.Android studio

APIs used:

1.Amazon Rekognition API
2.Amazon TTS service polly

Libraries used:

1.boto3
2.VL53L0X_rasp_python
3.python-v4l2capture

Android project file: 

1. SocketClient-master

Python files:

1.server_v2.py
2.Authentication_V2.py
3.image_capture.py
4.tts_service_amazon.py
5.clientV2.py
6.facematch.py(Modified)
7.VL53L0X_example.py(Modified)

Database:

1.id_database.txt


Execution flow:

1.The server_v2.py is executed on amazon ec2 server and will be listening for the connection requests from raspberrypi client program Authentication_V2.py.
2.After the communication from pi to server, the server listens for incoming connection requests from android application SocketClient-master.
3.After the communication between the server and android app, the pi keeps polling for the authentication status and plays the synthesized audio speech on the audio port of pi.

Limitations:

1.The refresh rate requirement to be provided by the user is not implemented in this milestone.The development of the requirement is in progress.
2.For amazon face rekognition API, I have implemented it using openCV 3.2.0, but later implemented it using the github repo which used AMAZON AWS FACE REKOGNITION API and modified it according to my requirement.

source: https://github.com/af001/pi-detector






 
