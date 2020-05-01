# -*- coding: utf-8 -*-

#시간관련 모듈 선언
import datetime

#필요한 외부 파이썬 모듈 선언
import RPi.GPIO as GPIO
from time import sleep
import MQTT_Pub as PUB
import numpy as np




#상황별 변수 설정
flag_sensors = [0, 0, 0, 0, 0, 0, 0, 0]

#MQTT로 전송할 데이터 저장 변수 
pubFLag = -1
pubGPIOIn = -1
alarmMessage = "-1"

GPIO.setmode(GPIO.BCM)

#zone GPIO
GPIO_IN_sensors = [21, 20, 16, 12, 1, 7, 8, 25]
GPIO_OUT_leds = [26, 19, 13, 6, 5, 0, 11, 9]
msg_close = [
    "1번구역에 침입발생",
    "2번구역에 침입발생",
    "3번구역에 침입발생",
    "4번구역에 침입발생",
    "5번구역에 침입발생",
    "6번구역에 침입발생",
    "7번구역에 침입발생",
    "8번구역에 침입발생" 
    ]
msg_open = [
    "1번구역 복구",
    "2번구역 복구",
    "3번구역 복구",
    "4번구역 복구",
    "5번구역 복구",
    "6번구역 복구",
    "7번구역 복구",
    "8번구역 복구"    
    ]

#호출 정보 (alarmFlag,alarmGPIO,alarmDesc)
# Flag값,GPIO입력값,Alarm내용
pubMessage = PUB.MQTTPublisher()


#상황별 GPIO 설정모드
print("상황별 GPIO 설정모드")

GPIO.setmode(GPIO.BCM)
for x in range(0, len(GPIO_IN_sensors)) :
    print(str(x) + "번구역 복구완료  (Setup)")
    GPIO.setup(GPIO_IN_sensors[x] , GPIO.IN)
    GPIO.setup(GPIO_OUT_leds[x] , GPIO.OUT)
    #pubMessage.pub_MQTT("DEV" + str(x),str(),str(),alarmMessage)
    print("Switch Setting End")

try:
    while True:
        for x in range(0, len(GPIO_IN_sensors)) :
            if GPIO.input(GPIO_IN_sensors[x]) == 0 and flag_sensors[x] == 0:
                flag_sensors[x] = 1
                print("+---------------------------------------------+")
                print("status : ")
                print(GPIO_IN_sensors[x])
                print(GPIO.input(GPIO_IN_sensors[x]))
            
                pubFLag =  flag_sensors[x]
                pubGPIOIn = GPIO_IN_sensors[x]        
                alarmMessage = msg_close[x]
                print(alarmMessage)
            
                GPIO.output(GPIO_OUT_leds[x], True)
                pubMessage.pub_MQTT("DEV" + str(x+1), str(),str(),alarmMessage)
                print("침입이 발생하였습니다print")
                print("+---------------------------------------------+")

            
            #print ("************* " + str(GPIO_IN_sensors[x]))
            #print (GPIO.input(GPIO_IN_sensors[x]))
            
            if GPIO.input(GPIO_IN_sensors[x]) == 1 and flag_sensors[x] == 1:
                flag_sensors[x] = 0
                print("+---------------------------------------------+")
                print("status : ((((((((((((((((((((((")
                print(GPIO.input(GPIO_IN_sensors[x]))
            
                pubFLag = flag_sensors[x]
                pubGPIOIn = GPIO_IN_sensors[x]
                alarmMessage = msg_open[x]
                print(alarmMessage)
            
                GPIO.output(GPIO_OUT_leds[x], False)
                pubMessage.pub_MQTT("DEV" + str(x+1), str(),str(),alarmMessage)
                print("복구완료print!! --+")
                print("+---------------------------------------------+")

except KeyboardInterrupt:
    GPIO.cleanup()
    print("테스트 종료 ~")  #clt+c
    #client.disconnect()

import sys
sys.exit()    
print (pubMessage)
#pubMessage.pub_MQTT("A","B","C")



