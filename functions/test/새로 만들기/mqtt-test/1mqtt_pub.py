# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt    #import client library
def on_connect(client, userdata, flags, rc):
    if rc==0:
      print("connected ok")
client = mqtt.Client()             #create new instance 
client.on_connect=on_connect  #bind call back function
client.connect("172.30.1.51", 1883)            #connect to broker
client.loop_start()  #Start loop 
time.sleep(4) # Wait for connection setup to complete
#Other code here
client.loop_stop()    #Stop loop


#ock = socket.create_connection((self._host, self._port), source_address=(self._bind_address, 0))

