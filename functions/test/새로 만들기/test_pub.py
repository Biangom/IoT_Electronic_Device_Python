# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt
import time

def publish_callback(client,userdata,result):             #create function for callback
    print("data published \n")

# 클라이언트 생성
client = mqtt.Client()

# publish 할때마다 호출되는 콜백함수 publish_callback 함수 설정한다.
client.on_publish = publish_callback

# publish할 주소와 포트번호 연결
client.connect("test.mosquitto.org", 1883)
client.loop_start()

try:
    while True:
        t = "33"
        # temp/random 이라는 토픽에 t라는 데이터를 보낸다
        client.publish("temp/random", t)
        time.sleep(2) #2초 간격으로 계속 보내게 하기!

except KeyboardInterrupt:
    print("Finished!")
    client.loop_stop()
    client.disconnect()
