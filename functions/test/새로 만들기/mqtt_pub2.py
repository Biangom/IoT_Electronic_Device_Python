# -*- coding: utf-8 -*-

# you have to import paho mqtt
import time
import paho.mqtt.client as mqtt

# When pulbish excute 
def publish_callback(client,userdata,result):             #create function for callback
    print("data published \n")

def on_conFunc(client, userdata, flags, rc):
    print("connected with result code " + str(rc))
    client.subscribe("data/temper")

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

client.username_pw_set("zkgnbgnk","ll-C0D2DoA2F")
client.connect("m15.cloudmqtt.com", 18971)
client.loop_start()

try:
    while True:
        t = "문자전송테스트"
        # temp/random 이라는 토픽에 t라는 데이터를 보낸다
        client.publish("temp/random", t)

        time.sleep(20) #20초 간격으로 계속 보내게 하기!
        
except KeyboardInterrupt:
    print("Finished!")
    client.unsubscribe(["data/temper"])
    #client.unsubscribe(["room309/temperature", "room309/humidity"])
    client.disconnect()

