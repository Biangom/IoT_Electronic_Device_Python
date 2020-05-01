# -*- coding: utf-8 -*-
#
# you have to import paho mqtt
import time
import paho.mqtt.client as mqtt

#class
class MQTTPublisher:
 
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

    def pub_MQTT(self,alarmFlag,alarmGPIO,alarmDesc):
        print("MQTT로 Message를 발송합니다. => ")
        
        client = mqtt.Client() #basic
        # client object create.
        client.on_connect = MQTTPublisher.on_conFunc
        client.on_message = MQTTPublisher.on_megFunc

        # publish 할때마다 호출되는 콜백함수 publish_callback 함수 설정한다.
        client.on_publish = MQTTPublisher.publish_callback

        #mqtt cloud 계정
        client.username_pw_set("uztrfyhg","zN6Oiudz0plw")
        client.connect("m16.cloudmqtt.com", 14593)

        #김성환 계정
        #client.username_pw_set("digit22","1123")
        client.connect("220.83.94.146", 1883)
        #client.loop_start()
        pubMessage = alarmFlag + "," + alarmGPIO + "," + alarmDesc
        client.publish("data/temper", pubMessage)

