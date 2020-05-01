# -*- coding: utf-8 -*-

#필요한 외부 파이썬 모듈 선언
import RPi.GPIO as GPIO
from time import sleep
import MQTT_Pub as PUB

#상황별 변수 설정
flag_Security = 0 #0 = 보안 해제 , 1 = 보안설정
flag_Door = 0     #0 = 문이 열림 , 1 = 문이 닫힘

#MQTT로 전송할 데이터 저장 변수 
pubFLag = -1
pubGPIOIn = -1
alarmMessage = "-1"
    
#보안 스위치 GPIO
GPIO_IN_SECURITY = 15
GPIO_OUT_SECURITY = 17
MESSAGE_SECURITY_SETUP = "보안이 설정되었습니다.!!"
MESSAGE_SECURITY_INTRUSION = "침입이 감지되었습니다.!"

#문 스위치 GPIO
GPIO_IN_DOOR = 20
GPIO_OUT_DOOR = 24
MESSAGE_DOOR_CLOSE = "문이 닫혔습니다.! "
MESSAGE_DOOR_OPEN = "문이 열렸습니다.! "


#호출 정보 (alarmFlag,alarmGPIO,alarmDesc)
# Flag값,GPIO입력값,Alarm내용
pubMessage = PUB.MQTTPublisher()
#Test Sample 
#pubMessage.pub_MQTT("ATEST","BTEST","CTEST")

#상황별 GPIO 설정모드
print("상황별 GPIO 설정모드")
GPIO.setmode(GPIO.BCM)

#보안 스위치 GPIO 설정 (Setup)
print("보안 스위치 GPIO 설정 (Setup)")
GPIO.setup(GPIO_IN_SECURITY, GPIO.IN )
GPIO.setup(GPIO_OUT_SECURITY, GPIO.OUT)

#문 스위치 GPIO 설정 (Setup)
print("문 스위치 GPIO 설정 (Setup)")
GPIO.setup(GPIO_IN_DOOR, GPIO.IN)
GPIO.setup(GPIO_OUT_DOOR, GPIO.OUT, initial=0)


print("Switch Setting End")


try:
    
    while True:
        
        if GPIO.input(GPIO_IN_SECURITY) == 0 and flag_Security == 0:            
            flag_Security = 1
            pubFLag = flag_Security            
            pubGPIOIn = GPIO_IN_SECURITY            
            alarmMessage = MESSAGE_SECURITY_SETUP
            print(alarmMessage)            
            GPIO.output(GPIO_OUT_SECURITY, True)
            

            pubMessage.pub_MQTT(str(),str(),alarmMessage)  
            #pubMessage.pub_MQTT(str(pubFLag),str(pubGPIOIn),alarmMessage)
            
        elif GPIO.input(GPIO_IN_SECURITY) == 1 and flag_Security == 1:
            flag_Security = 0
            pubGPIOIn = GPIO_IN_SECURITY
            alarmMessage = MESSAGE_SECURITY_INTRUSION
            print(alarmMessage)           
            GPIO.output(GPIO_OUT_SECURITY, False)

            pubMessage.pub_MQTT(str(),str(),alarmMessage)     
            
        elif GPIO.input(GPIO_IN_DOOR) == 0 and flag_Door == 0:
            flag_Door = 1
            pubFLag = flag_Door
            pubGPIOIn = GPIO_IN_DOOR
            alarmMessage = MESSAGE_DOOR_CLOSE
            print(alarmMessage) 
            GPIO.output(GPIO_OUT_DOOR, True)

            pubMessage.pub_MQTT(str(),str(),alarmMessage)     
            
        elif GPIO.input(GPIO_IN_DOOR) == 1 and flag_Door == 1:
            flag_Door = 0           
            pubFLag = flag_Door
            pubGPIOIn = GPIO_IN_DOOR
            alarmMessage = MESSAGE_DOOR_OPEN
            print(alarmMessage) 
            GPIO.output(GPIO_OUT_DOOR, False)

            pubMessage.pub_MQTT(str(),str(),alarmMessage)                        

except KeyboardInterrupt:
    GPIO.cleanup()
    print("테스트 종료 ~")


#print (pubMessage)
    
#pubMessage.pub_MQTT("A","B","C")


       
            

            
            
