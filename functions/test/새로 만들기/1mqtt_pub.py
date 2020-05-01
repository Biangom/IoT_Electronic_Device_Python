# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt

mqtt = mqtt.Client("python_pub") #Mqtt Client 오브젝트 생성
mqtt.connect("m15.cloudmqtt.com", 19738) #MQTT 서버에 연결

mqtt.publish("temp/random", "led") #토픽과 메세지 발행
mqtt.publish("nodemcu", "led off")

mqtt.loop(2) #timeout 2sec.


Close

