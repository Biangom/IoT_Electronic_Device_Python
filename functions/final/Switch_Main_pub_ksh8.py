# -*- coding: utf-8 -*-

#시간관련 모듈 선언
import datetime

#필요한 외부 파이썬 모듈 선언
import RPi.GPIO as GPIO
from time import sleep
import MQTT_Pub as PUB





#상황별 변수 설정
flag_SENSOR1 = 0     #0 = 보안 해제 , 1 = 보안설정
flag_SENSOR2 = 0     #0 = 문이 열림 , 1 = 문이 닫힘
flag_SENSOR3 = 0
flag_SENSOR4 = 0
flag_SENSOR5 = 0
flag_SENSOR6 = 0
flag_SENSOR7 = 0
flag_SENSOR8 = 0

#MQTT로 전송할 데이터 저장 변수 
pubFLag = -1
pubGPIOIn = -1
alarmMessage = "-1"
    
#zone1 GPIO21
GPIO_IN_SENSOR1 = 21  #GPIO_IN_SENSOR1 = 21
GPIO_OUT_LED1 = 26 # led 출력
MESSAGE_SENSOR1_CLOSE = "1번구역에 침입발생"
MESSAGE_SENSOR1_OPEN = "1번구역 복구"

#zone2 GPIO20
GPIO_IN_SENSOR2 = 20
GPIO_OUT_LED2 = 19 #led 출력
MESSAGE_SENSOR2_CLOSE = "2번구역에 침입발생"
MESSAGE_SENSOR2_OPEN = "2번구역 복구"

#zone3 GPIO16
GPIO_IN_SENSOR3 = 16
GPIO_OUT_LED3 = 13 #led 출력
MESSAGE_SENSOR3_CLOSE = "3번구역에 침입발생"
MESSAGE_SENSOR3_OPEN = "3번구역 복구 "

#zone4 GPIO12
GPIO_IN_SENSOR4 = 12
GPIO_OUT_LED4 = 6 #led 출력
MESSAGE_SENSOR4_CLOSE = "4번구역에 침입발생"
MESSAGE_SENSOR4_OPEN = "4번구역 복구"

#zone5 GPIO7
GPIO_IN_SENSOR5 = 1
GPIO_OUT_LED5 = 5 #led 출력
MESSAGE_SENSOR5_CLOSE = "5번구역에 침입발생"
MESSAGE_SENSOR5_OPEN = "5번구역 복구"

#zone6 GPIO8
GPIO_IN_SENSOR6 = 7
GPIO_OUT_LED6 = 11 #led 출력
MESSAGE_SENSOR6_CLOSE = "6번구역에 침입발생"
MESSAGE_SENSOR6_OPEN = "6번구역 복구"

#zone7 GPIO25
GPIO_IN_SENSOR7 = 8
GPIO_OUT_LED7 = 27 #led 출력
MESSAGE_SENSOR7_CLOSE = "7번구역에 침입발생"
MESSAGE_SENSOR7_OPEN = "7번구역 복구"

#zone8 GPIO24
GPIO_IN_SENSOR8 = 25
GPIO_OUT_LED8 = 17 #led 출력
MESSAGE_SENSOR8_CLOSE = "8번구역에 침입발생"
MESSAGE_SENSOR8_OPEN = "8번구역 복구"

#호출 정보 (alarmFlag,alarmGPIO,alarmDesc)
# Flag값,GPIO입력값,Alarm내용
pubMessage = PUB.MQTTPublisher()
#Test Sample 
#pubMessage.pub_MQTT("ATEST","BTEST","CTEST")

#상황별 GPIO 설정모드
print("상황별 GPIO 설정모드")

GPIO.setmode(GPIO.BCM)
GPIO.setup([21,20,16,12,1,7,8,25], GPIO.OUT, initial=GPIO.LOW)
GPIO.setup([26,19,13,6,5,11,27,17], GPIO.OUT, initial=GPIO.HIGH)

#zone1 스위치 GPIO 설정 (Setup)
print("1번구역 복구완료  (Setup)")
GPIO.setup(GPIO_IN_SENSOR1, GPIO.IN )
GPIO.setup(GPIO_OUT_LED1, GPIO.OUT)
pubMessage.pub_MQTT(str(),str(),alarmMessage)
print("Switch Setting End")

#zone2 스위치 GPIO 설정 (Setup)
print("2번구역 복구완료 (Setup)")
GPIO.setup(GPIO_IN_SENSOR2, GPIO.IN)
GPIO.setup(GPIO_OUT_LED2, GPIO.OUT)
pubMessage.pub_MQTT(str(),str(),alarmMessage)
print("Switch Setting End")

#zone3 스위치 GPIO 설정 (Setup)
print("3번구역 복구완료 (Setup)")
GPIO.setup(GPIO_IN_SENSOR3, GPIO.IN)
GPIO.setup(GPIO_OUT_LED3, GPIO.OUT)
pubMessage.pub_MQTT(str(),str(),alarmMessage)
print("Switch Setting End")

#zone4 스위치 GPIO 설정 (Setup)
print("4번구역 복구완료 (Setup)")
GPIO.setup(GPIO_IN_SENSOR4, GPIO.IN)
GPIO.setup(GPIO_OUT_LED4, GPIO.OUT)
pubMessage.pub_MQTT(str(),str(),alarmMessage)
print("Switch Setting End")

#zone5 스위치 GPIO 설정 (Setup)
print("5번구역 복구완료 (Setup)")
GPIO.setup(GPIO_IN_SENSOR5, GPIO.IN)
GPIO.setup(GPIO_OUT_LED5, GPIO.OUT)
pubMessage.pub_MQTT(str(),str(),alarmMessage)
print("Switch Setting End")

#zone6 스위치 GPIO 설정 (Setup)
print("6번구역 복구완료 (Setup)")
GPIO.setup(GPIO_IN_SENSOR6, GPIO.IN)
GPIO.setup(GPIO_OUT_LED6, GPIO.OUT)
pubMessage.pub_MQTT(str(),str(),alarmMessage)
print("Switch Setting End")

#zone7 스위치 GPIO 설정 (Setup)
print("7번구역 복구완료 (Setup)")
GPIO.setup(GPIO_IN_SENSOR7, GPIO.IN)
GPIO.setup(GPIO_OUT_LED7, GPIO.OUT)
pubMessage.pub_MQTT(str(),str(),alarmMessage)
print("Switch Setting End")

#zone8 스위치 GPIO 설정 (Setup)
print("8번구역 복구완료 (Setup)")
GPIO.setup(GPIO_IN_SENSOR8, GPIO.IN)
GPIO.setup(GPIO_OUT_LED8, GPIO.OUT) #(GPIO_OUT_SENSOR8, GPIO.OUT, initial=0)
pubMessage.pub_MQTT(str(),str(),alarmMessage)
print("Switch Setting End")


      
try:
    while True:
        
#zone1 close  ========>
        
        if GPIO.input(GPIO_IN_SENSOR1) == 0 and flag_SENSOR1 == 0:            
            flag_SENSOR1 = 1
            pubFLag = flag_SENSOR1 
            pubGPIOIn = GPIO_IN_SENSOR1          
            alarmMessage = MESSAGE_SENSOR1_CLOSE
            
            print(alarmMessage)
            
            GPIO.output(GPIO_OUT_LED1, True)
            pubMessage.pub_MQTT(str(),str(),alarmMessage)
            
            #print("1번구역에 침입이 발생하였습니다print")
            
#Zone1 open ========>
            
        elif GPIO.input(GPIO_IN_SENSOR1) == 1 and flag_SENSOR1 == 1:
            flag_SENSOR1 = 0
            pubFLag = flag_SENSOR1
            pubGPIOIn = GPIO_IN_SENSOR1
            alarmMessage = MESSAGE_SENSOR1_OPEN
            
            print(alarmMessage)
            
            GPIO.output(GPIO_OUT_LED1, False)
            pubMessage.pub_MQTT(str(),str(),alarmMessage)
            
            #print("1번구역복구완료print!!")

#Zone2 close  ========>
            
        if GPIO.input(GPIO_IN_SENSOR2) == 0 and flag_SENSOR2 == 0:
            flag_SENSOR2 = 1
            pubFLag = flag_SENSOR2
            pubGPIOIn = GPIO_IN_SENSOR2
            alarmMessage = MESSAGE_SENSOR2_CLOSE
            
            print(alarmMessage)
            
            GPIO.output(GPIO_OUT_LED2, True)
            pubMessage.pub_MQTT(str(),str(),alarmMessage)
            
            print("2번구역에 침입이 발생하였습니다")
            
#Zone2 open  ========>
            
        elif GPIO.input(GPIO_IN_SENSOR2) == 1 and flag_SENSOR2 == 1:
            flag_SENSOR2 = 0           
            pubFLag = flag_SENSOR2
            pubGPIOIn = GPIO_IN_SENSOR2
            alarmMessage = MESSAGE_SENSOR2_OPEN
            print(alarmMessage)
            
            GPIO.output(GPIO_OUT_LED2, False)
            pubMessage.pub_MQTT(str(),str(),alarmMessage)

            print("2번구역 복구완료!print")
            
#Zone3 close  ========>
            
        if GPIO.input(GPIO_IN_SENSOR3) == 0 and flag_SENSOR3 == 0:            
            flag_SENSOR3 = 1
            pubFLag = flag_SENSOR3            
            pubGPIOIn = GPIO_IN_SENSOR3          
            alarmMessage = MESSAGE_SENSOR3_CLOSE
            
            print(alarmMessage)
            
            GPIO.output(GPIO_OUT_LED3, True)
            pubMessage.pub_MQTT(str(),str(),alarmMessage)
            
            print("3번구역에 침입이 발생하였습니다")
            
#Zone3 open  ========>
            
        elif GPIO.input(GPIO_IN_SENSOR3) == 1 and flag_SENSOR3 == 1:
            flag_SENSOR3 = 0
            pubFLag = flag_SENSOR3
            pubGPIOIn = GPIO_IN_SENSOR3
            alarmMessage = MESSAGE_SENSOR3_OPEN
            
            print(alarmMessage)
            
            GPIO.output(GPIO_OUT_LED3, False)
            pubMessage.pub_MQTT(str(),str(),alarmMessage)
            
            print("3번구역 복구완료!print")
            
#Zone4 close  ========>
            
        if GPIO.input(GPIO_IN_SENSOR4) == 0 and flag_SENSOR4 == 0:            
            flag_SENSOR4 = 1
            pubFLag = flag_SENSOR4            
            pubGPIOIn = GPIO_IN_SENSOR4          
            alarmMessage = MESSAGE_SENSOR4_CLOSE
            
            print(alarmMessage)
            
            GPIO.output(GPIO_OUT_LED4, True)
            pubMessage.pub_MQTT(str(),str(),alarmMessage)
            
            print("4번구역에 침입이 발생하였습니다!print")
            
#Zone4 open ========>
            
        elif GPIO.input(GPIO_IN_SENSOR4) == 1 and flag_SENSOR4 == 1:
            flag_SENSOR4 = 0
            pubFLag = flag_SENSOR4
            pubGPIOIn = GPIO_IN_SENSOR4
            alarmMessage = MESSAGE_SENSOR4_OPEN
            
            print(alarmMessage)
            
            GPIO.output(GPIO_OUT_LED4, False)
            pubMessage.pub_MQTT(str(),str(),alarmMessage)
            
            print("4번구역 복구완료")            

#Zone5 close ========>
            
        if GPIO.input(GPIO_IN_SENSOR5) == 0 and flag_SENSOR5 == 0:            
            flag_SENSOR5 = 1
            pubFLag = flag_SENSOR5            
            pubGPIOIn = GPIO_IN_SENSOR5          
            alarmMessage = MESSAGE_SENSOR5_CLOSE
            
            print(alarmMessage)
            
            GPIO.output(GPIO_OUT_LED5, True)
            pubMessage.pub_MQTT(str(),str(),alarmMessage)
            
            print("5번구역에 침입이 발생하였습니다!print")
            
#Zone5 open ========>
            
        elif GPIO.input(GPIO_IN_SENSOR5) == 1 and flag_SENSOR5 == 1:
            flag_SENSOR5 = 0
            pubFLag = flag_SENSOR5
            pubGPIOIn = GPIO_IN_SENSOR5
            alarmMessage = MESSAGE_SENSOR5_OPEN
            
            print(alarmMessage)
            
            GPIO.output(GPIO_OUT_LED5, False)
            pubMessage.pub_MQTT(str(),str(),alarmMessage)
            
            print("5번구역 복구완료!print") 

#Zone6 close ========>
            
        if GPIO.input(GPIO_IN_SENSOR6) == 0 and flag_SENSOR6 == 0:            
            flag_SENSOR6 = 1
            pubFLag = flag_SENSOR6            
            pubGPIOIn = GPIO_IN_SENSOR6          
            alarmMessage = MESSAGE_SENSOR6_CLOSE
            
            print(alarmMessage)
            
            GPIO.output(GPIO_OUT_LED6, True)
            pubMessage.pub_MQTT(str(),str(),alarmMessage)
            
            print("6번구역에 침입이 발생하였습니다!print")
            
#Zone6 open ========>
            
        elif GPIO.input(GPIO_IN_SENSOR6) == 1 and flag_SENSOR6 == 1:
            flag_SENSOR6 = 0
            pubFLag = flag_SENSOR6
            pubGPIOIn = GPIO_IN_SENSOR6
            alarmMessage = MESSAGE_SENSOR6_OPEN
            
            print(alarmMessage)
            
            GPIO.output(GPIO_OUT_LED6, False)
            pubMessage.pub_MQTT(str(),str(),alarmMessage)
            
            print("6번구역 복구완료!print")

#Zone7 close ========>
            
        if GPIO.input(GPIO_IN_SENSOR7) == 0 and flag_SENSOR7 == 0:            
            flag_SENSOR7 = 1
            pubFLag = flag_SENSOR7            
            pubGPIOIn = GPIO_IN_SENSOR7          
            alarmMessage = MESSAGE_SENSOR7_CLOSE
            
            print(alarmMessage)
            
            GPIO.output(GPIO_OUT_LED7, True)
            pubMessage.pub_MQTT(str(),str(),alarmMessage)
            
            print("7번구역에 침입이 발생하였습니다!print")
            
#Zone7 open ========>
            
        elif GPIO.input(GPIO_IN_SENSOR7) == 1 and flag_SENSOR7 == 1:
            flag_SENSOR7 = 0
            pubFLag = flag_SENSOR7
            pubGPIOIn = GPIO_IN_SENSOR7
            alarmMessage = MESSAGE_SENSOR7_OPEN
            
            print(alarmMessage)
            
            GPIO.output(GPIO_OUT_LED7, False)
            pubMessage.pub_MQTT(str(),str(),alarmMessage)
            
            print("7번구역 복구완료!print")             

#Zone8 close========>
            
        if GPIO.input(GPIO_IN_SENSOR8) == 0 and flag_SENSOR8 == 0:            
            flag_SENSOR8 = 1
            pubFLag = flag_SENSOR8            
            pubGPIOIn = GPIO_IN_SENSOR8          
            alarmMessage = MESSAGE_SENSOR8_CLOSE
            
            print(alarmMessage)
            
            GPIO.output(GPIO_OUT_LED8, True)
            pubMessage.pub_MQTT(str(),str(),alarmMessage)
            
            print("8번구역에 침입이 발생하였습니다!print")
            
#Zone8 open ========>
            
        elif GPIO.input(GPIO_IN_SENSOR8) == 1 and flag_SENSOR8 == 1:
            flag_SENSOR8 = 0
            pubFLag = flag_SENSOR8
            pubGPIOIn = GPIO_IN_SENSOR8
            alarmMessage = MESSAGE_SENSOR8_OPEN
            
            print(alarmMessage)
            
            GPIO.output(GPIO_OUT_LED8, False)
            pubMessage.pub_MQTT(str(),str(),alarmMessage)
            
            print("8번구역 복구완료!print")
            
#=============================================================            
            #sleep(300) #5분 간격으로 계속 보내게 하기!
except KeyboardInterrupt:
    GPIO.cleanup()
    print("테스트 종료 ~")  #clt+c
    #client.disconnect()



import sys
sys.exit()    
print (pubMessage)
#pubMessage.pub_MQTT("A","B","C")


       
            

            
            
