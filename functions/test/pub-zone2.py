# -*- coding: utf-8 -*-

# you have to import paho mqtt
import time
import paho.mqtt.client as mqtt

import RPi.GPIO as GPIO
ZONE1 = 16
LED1 = 23

ZONE2 = 20
LED2 = 24

ZONE3 = 21
LED3 = 25


GPIO.setmode(GPIO.BCM)

GPIO.setup(ZONE1, GPIO.IN )
GPIO.setup(LED1, GPIO.OUT)

GPIO.setup(ZONE2, GPIO.IN )
GPIO.setup(LED2, GPIO.OUT)

GPIO.setup(ZONE3, GPIO.IN )
GPIO.setup(LED3, GPIO.OUT)

ZONE1_flag = 0
ZONE2_flag = 0
ZONE3_flag = 0

#print("버튼을 누르세요!  (CTL-C to exit)")

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

#client.username_pw_set("mtpnvorj","ueq226Wih4fS")
#client.connect("m16.cloudmqtt.com", 16966)
#김성환 계정
client.username_pw_set("digit22","1123")
client.connect("220.83.94.146", 1883)


client.loop_start()


try:

    while True:
        t1 = "1번구역 보안설정"
        t2 = "1번구역 보안해제"
        
        t3 = "2번구역 보안설정"
        t4 = "2번구역 보안해제"

        t5 = "3번구역 보안설정"
        t6 = "3번구역 보안해제"

        #ZONE1=============================
        if GPIO.input(ZONE1)==0 and ZONE1_flag == 0:
            ZONE1_flag = 1
            GPIO.output(LED1, True)
            print ("1번구역 보안설정 ")
            client.publish("data/temper", t1)
            
        
        elif GPIO.input(ZONE1) ==1 and ZONE1_flag == 1:
            ZONE1_flag = 0
            GPIO.output(LED1, False)
            print ("1번구역 보안해제")
            client.publish("data/temper", t2)

            
         #ZONE2==============================   
        elif GPIO.input(ZONE2)==0 and ZONE2_flag == 0:
            ZONE2_flag = 1
            GPIO.output(LED2, True)
            print ("2번구역 보안설정 ")
            client.publish("data/temper", t3)
                
        elif GPIO.input(ZONE2) ==1 and ZONE2_flag == 1:
            ZONE2_flag = 0
            GPIO.output(LED2, False)
            print ("2번구역 보안해제")
            client.publish("data/temper", t4)
                    
           #ZONE3==============================





            
        



        #time.sleep(2) #20초 간격으로 계속 보내게 하기!
        
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Finished!")
    client.unsubscribe(["data/temper"])
    #client.unsubscribe(["room309/temperature", "room309/humidity"])
    client.disconnect()

import sys
sys.exit()
