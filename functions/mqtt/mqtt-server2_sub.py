# -*- coding: utf-8 -*-

# you have to import paho mqtt
import time
import paho.mqtt.client as mqtt

# When pulbish excute 
def publish_callback(client,userdata,result):             #create function for callback
    print("data published \n")

def on_conFunc(client, userdata, flags, rc):
    print("connected with result code " + str(rc))
    client.subscribe("temp")



def on_megFunc(client, userdata, msg):
    data = str(msg.payload)
    
    if data == "aaa": 
        print("moter stop")
    elif data == "def":
        print("moter on ")
    else:
        print("Topic: " + msg.topic + " Message: " + data)


client = mqtt.Client() #basic
# client object create.
client.on_connect = on_conFunc
client.on_message = on_megFunc

# publish 할때마다 호출되는 콜백함수 publish_callback 함수 설정한다.
client.on_publish = publish_callback

client.username_pw_set("digit22","1234")
client.connect("220.83.94.146", 1883)


try:
    client.loop_forever()
        
except KeyboardInterrupt:
    print("Finished!")
    client.unsubscribe(["temp"])
    #client.unsubscribe(["room309/temperature", "room309/humidity"])
    client.disconnect()
