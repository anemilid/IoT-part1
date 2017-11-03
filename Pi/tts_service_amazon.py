from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import os
import sys
import subprocess
from tempfile import gettempdir

def tts_amazon(text):
    
    session = Session(profile_name="default")
    polly = session.client("polly")
    try:
        response = polly.synthesize_speech(Text=text, OutputFormat="mp3",
        VoiceId="Salli")
    except (BotoCoreError, ClientError) as error:
        print(error)
        sys.exit(-1)
    if "AudioStream" in response:
        with closing(response["AudioStream"]) as stream:
            output = os.path.join(gettempdir(), "authentication_status.mp3")
            print output
            try:
                with open(output, "wb") as file:
                    file.write(stream.read())
            except IOError as error:
                print(error)
                sys.exit(-1)
    else:
        print("Could not stream audio")
        sys.exit(-1)
        
    if sys.platform == "win32":
        os.startfile(output)
    else:
        print "here"
        opener = "open" if sys.platform == "darwin" else "xdg-open"
    subprocess.call([opener, output])
    subprocess.call("exit 1",shell=True)

if __name__=="__main__":
    tts_amazon("hi anusha home!")
