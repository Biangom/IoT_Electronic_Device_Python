# -*- coding: utf-8 -*-

# you have to import paho mqtt
import time
import paho.mqtt.client as mqtt

# When pulbish excute 
def publish_callback(client,userdata,result):             #create function for callback
    print("data published \n")

def on_conFunc(client, userdata, flags, rc):
    print("connected with result code " + str(rc))
    client.subscribe("python/test")

def on_megFunc(client, userdata, msg):
    data = str(msg.payload)
    
    print(result)
    print("Topic: " + msg.topic + " Message: " + str(msg.payload))


client = mqtt.Client() #basic
# client object create.
client.on_connect = on_conFunc
client.on_message = on_megFunc

# publish 할때마다 호출되는 콜백함수 publish_callback 함수 설정한다.
client.on_publish = publish_callback

client.username_pw_set("digit22","1234")


client.connect("121.191.61.155", 1880)
client.loop_start()

try:
    #while True:
        t = "파이썬 문자테스트와 mqtt서버 테스트완료2"
        # temp/random 이라는 토픽에 t라는 데이터를 보낸다
        client.publish("python/test", t)

        #time.sleep(20) #20초 간격으로 계속 보내게 하기!
        
except KeyboardInterrupt:
    print("Finished!")
    client.unsubscribe(["python/test"])
    #client.unsubscribe(["room309/temperature", "room309/humidity"])
    client.disconnect()

import sys
sys.exit()

