import paho.mqtt.client as mqtt
import time
import subprocess

def message(client, userdata, message):
    topic = str(message.topic)
    message = str(message.payload.decode("utf-8"))
    print(topic + message)

myClient = mqtt.Client("yoyojacky")
myClient.connect("solasolo.oicp.net",1883)
myClient.subscribe("piday4fun/action")
myClient.on_message = message
myClient.loop_start()

try:
    while True:
        #temp = subprocess.getoutput('vcgencmd measure_temp') 
        #myClient.publish("Piday4fun", "{}".format(temp))
        if myClient.subscribe("piday4fun/action"):
            subprocess.call(["/bin/stepper", "0", "1", "2", "3"])
        else:
            subprocess.call(["bin/stepper","3","2","1","0"])
        time.sleep(1)
except KeyboardInterrupt:
    print("byebye!")

