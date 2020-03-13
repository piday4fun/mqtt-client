import paho.mqtt.client as mqtt
import time
import subprocess
import cv2

count = 0 

def message(client, userdata, message):
    global count 
    topic = str(message.topic)
    message = str(message.payload.decode("utf-8"))
    print(topic + message)
    subprocess.call(["/bin/stepper", "0", "1", "2", "3"])
    count +=1


myClient = mqtt.Client("yoyojacky")
myClient.connect("solasolo.oicp.net",1883)
myClient.on_message = message
myClient.subscribe("piday4fun/action", 1)
# myClient.loop_forever()
while True:
    try:
        myClient.loop(1)
    except KeyboardInterrupt:
        print(count)
        for i in range(count):
            subprocess.call(["/bin/stepper", "3", "2", "1", "0"])
        break
