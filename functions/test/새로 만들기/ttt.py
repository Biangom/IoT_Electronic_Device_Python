# -*- coding: utf-8 -*-
import paho.mqtt.client as paho
broker="172.30.1.51", 1883
port=1883
def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
    pass
client1= paho.Client("control1")                           #create client object
client1.on_publish = on_publish                          #assign function to callback
client1.connect("172.30.1.51", 1883)                                 #establish connection
ret= client1.publish("house/bulb1","on")                   #publish
