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
        
        client = mqtt.Client() #basic
        # client object create.
        client.on_connect = MQTTPublisher.on_conFunc
        client.on_message = MQTTPublisher.on_megFunc

        # publish 할때마다 호출되는 콜백함수 publish_callback 함수 설정한다.
        client.on_publish = MQTTPublisher.publish_callback

        #김충환 계정
        #client.username_pw_set("dwkrotfi","eJAzIgto7XCv")
        #client.connect("m15.cloudmqtt.com", 19865)

        #김성환 계정
        #client.username_pw_set("mtpnvorj","ueq226Wih4fS")
        client.connect("220.83.94.146", 1883)

        pubMessage = alarmFlag + "," + alarmGPIO + "," + alarmDesc
        client.publish("data/temper", pubMessage)
        
        
        
        #client.loop_start()

        #try:
        #    while True:
                #Test용 코드
                #t = "test-" 
                #a = a +1
                # temp/random 이라는 토픽에 t라는 데이터를 보낸다
                #client.publish("temp/random", t + str(a) )
                #time.sleep(3) #20초 간격으로 계속 보내게 하기!
                
        #except KeyboardInterrupt:
        #    print("Finished!")
        #    #client.unsubscribe(["temp/random"])
        #    #client.unsubscribe(["room309/temperature", "room309/humidity"])
        #    client.disconnect()
