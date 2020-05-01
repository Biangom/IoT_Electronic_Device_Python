# -*- coding: utf-8 -*-

#시간관련 모듈 선언
import datetime

#필요한 외부 파이썬 모듈 선언
import RPi.GPIO as GPIO
from time import sleep
import MQTT_Pub as PUB

#======================== sms  sdk sms 모듈호출
import sys
sys.path.insert(0, "../../")

from sdk.api.message import Message
from sdk.exceptions import CoolsmsException

#문자발송제한변수
flag_sms_send_count = 0
CONST_SMS_MAX_SEND_VALUE = 3 #문자를 최대 3번 전송한다.

# Alarm발생시간 및 경과시간
CONST_ALARM_ELASPED_TIME = 5 #5분 후에 다시 SMS발송한다.
alarm_start_time = datetime.datetime.now()
alarm_elapsed_time = ""
alarm_check_flag = False
alarm_before_gpio = 0
alarm_before_flag = 0


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
#pubFLag = -1
#pubGPIOIn = -1
alarmMessage = "-1"
    
#zone1 GPIO21
GPIO_IN_SENSOR1 = 21  #GPIO_IN_SENSOR1 = 21
GPIO_OUT_LED1 = 26 # led 출력
MESSAGE_SENSOR1_CLOSE = "1번구역에 침입이 발생하였습니다"
MESSAGE_SENSOR1_OPEN = "1번구역 복구"

#zone2 GPIO20
GPIO_IN_SENSOR2 = 20
GPIO_OUT_LED2 = 19 #led 출력
MESSAGE_SENSOR2_CLOSE = "2번구역에 침입이 발생하였습니다"
MESSAGE_SENSOR2_OPEN = "2번구역 복구"

#zone3 GPIO16
GPIO_IN_SENSOR3 = 16
GPIO_OUT_LED3 = 13 #led 출력
MESSAGE_SENSOR3_CLOSE = "3번구역에 침입이 발생하였습니다"
MESSAGE_SENSOR3_OPEN = "3번구역 복구 "

#zone4 GPIO12
GPIO_IN_SENSOR4 = 12
GPIO_OUT_LED4 = 6 #led 출력
MESSAGE_SENSOR4_CLOSE = "4번구역에 침입이 발생하였습니다"
MESSAGE_SENSOR4_OPEN = "4번구역 복구"

#zone5 GPIO7
GPIO_IN_SENSOR5 = 7
GPIO_OUT_LED5 = 5 #led 출력
MESSAGE_SENSOR5_CLOSE = "5번구역에 침입이 발생하였습니다"
MESSAGE_SENSOR5_OPEN = "5번구역 복구"

#zone6 GPIO8
GPIO_IN_SENSOR6 = 8
GPIO_OUT_LED6 = 11 #led 출력
MESSAGE_SENSOR6_CLOSE = "6번구역에 침입이 발생하였습니다"
MESSAGE_SENSOR6_OPEN = "6번구역 복구"

#zone7 GPIO25
GPIO_IN_SENSOR7 = 25
GPIO_OUT_LED7 = 9 #led 출력
MESSAGE_SENSOR7_CLOSE = "7번구역에 침입이 발생하였습니다"
MESSAGE_SENSOR7_OPEN = "7번구역 복구"

#zone8 GPIO24
GPIO_IN_SENSOR8 = 24
GPIO_OUT_LED8 = 10 #led 출력
MESSAGE_SENSOR8_CLOSE = "8번구역에 침입이 발생하였습니다"
MESSAGE_SENSOR8_OPEN = "8번구역 복구"

#호출 정보 (alarmFlag,alarmGPIO,alarmDesc)
# Flag값,GPIO입력값,Alarm내용
pubMessage = PUB.MQTTPublisher()
#Test Sample 
#pubMessage.pub_MQTT("ATEST","BTEST","CTEST")

#상황별 GPIO 설정모드
print("상황별 GPIO 설정모드")

GPIO.setmode(GPIO.BCM)
#GPIO.setup([21,20,16,12,7,8,25,24], GPIO.OUT, initial=GPIO.HIGH)
#GPIO.setup([26,19,13,6,5,11,9,10], GPIO.OUT, initial=GPIO.LOW)

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
GPIO.setup(GPIO_OUT_LED8, GPIO.OUT,initial=0) #(GPIO_OUT_LED8, GPIO.OUT, initial=0)
pubMessage.pub_MQTT(str(),str(),alarmMessage)
print("Switch Setting End")

# set api key, api secret
api_key = "NCSBQ9QL4QIB6AHB"
api_secret = "NO3K7ATJ8B8FKZNWKBNHPDRXUQQTYSE6"

## 4 params(to, from, type, text) are mandatory. must be filled
params = dict()
params['type'] = 'sms' # Message type ( sms, lms, mms, ata )
params['to'] = '01074704184' # Recipients Number 
#params['to'] = '01065231138' # Recipients Number - 김충환TEST용
params['from'] = '0438788405' # Sender number


#function : send message
def smsSend(message,parm_gpio_value,parm_flag_value):

    #전역변수를 Local에서 사용 선언
    global alarm_before_gpio
    global alarm_before_flag
    global flag_sms_send_count
    global CONST_SMS_MAX_SEND_VALUE 
    global CONST_ALARM_ELASPED_TIME
    global alarm_start_time
    global alarm_elapsed_time 
    global alarm_check_flag
    global alarm_before_gpio
    global alarm_before_flag
    global pubMessage

    alarm_sms_send = False

    #현재시간보다 CONST_ALARM_ELASPED_TIME시간(분단위) 시간(분)을 구한다.
    alarm_elapsed_time = datetime.datetime.now() - datetime.timedelta(minutes=CONST_ALARM_ELASPED_TIME)
    
    #이전에 Check된 GPIO와 현재 GPIO가 다를경우 강제로 SMS로 발송한다. (Flag값 포함)
    #즉! 새로운 알람발생시 강제로 SMS발송
    
    if alarm_before_gpio != parm_gpio_value and alarm_before_flag != parm_flag_value:
        print("이전과 다른 GPIO신호로 인해 SMS를 발송합니다.")
        alarm_before_gpio = parm_gpio_value
        alarm_before_flag = parm_flag_value
        alarm_sms_send = True
        alarm_check_flag = False
        alarm_start_time = datetime.datetime.now()
        alarm_elapsed_time = datetime.datetime.now()
        flag_sms_send_count = 0
    else: #이전과 같은 GPIO 및 Flag 같을경우 Alarm시작시간을 기록하고 Alarm발생 Check Count한다.
        if alarm_check_flag == False:
            alarm_start_time = datetime.datetime.now()
            alarm_check_flag = True
            alarm_sms_send = True        
    
    if alarm_check_flag:
        print("이전과 같은 GPIO신호로 인해 SMS 발송여부를 점검합니다.")
        #alarm발생시간부터 1시간이 경과하면 문자를 발송하지 않는다.
        if alarm_start_time < alarm_elapsed_time:
           alarm_sms_send = False
        else:
        #아직 경과시간이 지나지 않았다면 SMS를 발송한다.
            if flag_sms_send_count < CONST_SMS_MAX_SEND_VALUE:
                flag_sms_send_count += 1
                alarm_sms_send = True
            else:
                alarm_sms_send = False
    
   
    #alarm_sms_send = False

    if alarm_sms_send:
        #문자를 발송할때 MQTT로도 Message를 발송한다.
        pubMessage.pub_MQTT(str(parm_flag_value),str(parm_gpio_value),message)
        print("SMS를 발송합니다.")
        params['text'] = message # Message
        cool = Message(api_key, api_secret)
        try:
            response = cool.send(params)
            print("Success Count : %s" % response['success_count'])
            print("Error Count : %s" % response['error_count'])
            print("Group ID : %s" % response['group_id'])

            if "error_list" in response:
                print("Error List : %s" % response['error_list'])

        except CoolsmsException as e:
            print("Error Code : %s" % e.code)
            print("Error Message : %s" % e.msg)

            cool = Message(api_key, api_secret)

            try:
                response = cool.send(params)
                print("Success Count : %s" % response['success_count'])
                print("Error Count : %s" % response['error_count'])
                print("Group ID : %s" % response['group_id'])

                if "error_list" in response:
                    print("Error List : %s" % response['error_list'])
                        
            except CoolsmsException as e:
                print("Error Code : %s" % e.code)
                print("Error Message : %s" % e.msg)




try:
    while True:
#==============================================================zone1 close       
        if GPIO.input(GPIO_IN_SENSOR1) == 0 and flag_SENSOR1 == 0:            
            flag_SENSOR1 = 1
            #pubFLag = flag_SENSOR1 
            #pubGPIOIn = GPIO_IN_SENSOR1          
            alarmMessage = MESSAGE_SENSOR1_CLOSE
            print(alarmMessage)
            
            GPIO.output(GPIO_OUT_LED1, True)
            pubMessage.pub_MQTT(str(),str(),alarmMessage)
            
            #smsSend("화재감지기가 작동하였습니다!!",GPIO_IN_SENSOR1,flag_SENSOR1)
            print("화재감지기가 작동하였습니다!!print")
#==============================================================zone1 open           
        elif GPIO.input(GPIO_IN_SENSOR1) == 1 and flag_SENSOR1 == 1:
            flag_SENSOR1 = 0
            #pubFLag = flag_SENSOR1
            #pubGPIOIn = GPIO_IN_SENSOR1
            alarmMessage = MESSAGE_SENSOR1_OPEN
            print(alarmMessage)
            
            GPIO.output(GPIO_OUT_LED1, False)
            pubMessage.pub_MQTT(str(),str(),alarmMessage)
            
            #smsSend("화재감지기가 복구되었습니다!!",GPIO_IN_SENSOR1,flag_SENSOR1)  #복구되었습니다.!!"
            print("화재감지기가 복구되었습니다print!!")
#==============================================================zone2 close           
        if GPIO.input(GPIO_IN_SENSOR2) == 0 and flag_SENSOR2 == 0:
            flag_SENSOR2 = 1
            #pubFLag = flag_SENSOR2
            #pubGPIOIn = GPIO_IN_SENSOR2
            alarmMessage = MESSAGE_SENSOR2_CLOSE
            print(alarmMessage)
            
            GPIO.output(GPIO_OUT_LED2, True)
            pubMessage.pub_MQTT(str(),str(),alarmMessage)
            
            #smsSend("정전발생! 정전발생!",GPIO_IN_SENSOR2,flag_SENSOR2)
            print("정전발생! 정전발생!")
#==============================================================zone2 open            
        elif GPIO.input(GPIO_IN_SENSOR2) == 1 and flag_SENSOR2 == 1:
            flag_SENSOR2 = 0           
            #pubFLag = flag_SENSOR2
            #pubGPIOIn = GPIO_IN_SENSOR2
            alarmMessage = MESSAGE_SENSOR2_OPEN
            print(alarmMessage)
            
            GPIO.output(GPIO_OUT_LED2, False)
            pubMessage.pub_MQTT(str(),str(),alarmMessage)

            #smsSend("상용전원 공급중입니다!!",GPIO_IN_SENSOR2,flag_SENSOR2)
            print("상용전원 공급중입니다!!")
#============================================================= zone3 close       
        if GPIO.input(GPIO_IN_SENSOR3) == 0 and flag_SENSOR3 == 0:            
            flag_SENSOR3 = 1
            #pubFLag = flag_SENSOR3            
            #pubGPIOIn = GPIO_IN_SENSOR3          
            alarmMessage = MESSAGE_SENSOR3_CLOSE
            print(alarmMessage)
            
            GPIO.output(GPIO_OUT_LED3, True)
            pubMessage.pub_MQTT(str(),str(),alarmMessage)
            
            #smsSend("3번구역 복구완료",GPIO_IN_SENSOR3,flag_SENSOR3)
            print("3번구역에 침입이 발생하였습니다")
#=============================================================zone3 open           
        elif GPIO.input(GPIO_IN_SENSOR3) == 1 and flag_SENSOR3 == 1:
            flag_SENSOR3 = 0
            #pubFLag = flag_SENSOR3
            #pubGPIOIn = GPIO_IN_SENSOR3
            alarmMessage = MESSAGE_SENSOR3_OPEN
            print(alarmMessage)
            
            GPIO.output(GPIO_OUT_LED3, False)
            pubMessage.pub_MQTT(str(),str(),alarmMessage)
            
            #smsSend("3번구역에 침입이 발생하였습니다",GPIO_IN_SENSOR3,flag_SENSOR3)
            print("3번구역 복구완료!print")
#============================================================= zone4 close       
        if GPIO.input(GPIO_IN_SENSOR4) == 0 and flag_SENSOR4 == 0:            
            flag_SENSOR4 = 1
            #pubFLag = flag_SENSOR4            
            #pubGPIOIn = GPIO_IN_SENSOR4          
            alarmMessage = MESSAGE_SENSOR4_CLOSE
            print(alarmMessage)
            
            GPIO.output(GPIO_OUT_LED4, True)
            pubMessage.pub_MQTT(str(),str(),alarmMessage)
            
            #smsSend("4번구역에 침입이 발생하였습니다",GPIO_IN_SENSOR4,flag_SENSOR4)
            print("4번구역에 침입이 발생하였습니다!print")
#=============================================================zone4 open           
        elif GPIO.input(GPIO_IN_SENSOR4) == 1 and flag_SENSOR4 == 1:
            flag_SENSOR4 = 0
            #pubFLag = flag_SENSOR4
            #pubGPIOIn = GPIO_IN_SENSOR4
            alarmMessage = MESSAGE_SENSOR4_OPEN
            print(alarmMessage)
            
            GPIO.output(GPIO_OUT_LED4, False)
            pubMessage.pub_MQTT(str(),str(),alarmMessage)
            
            #smsSend("4번구역 복구완료",GPIO_IN_SENSOR4,flag_SENSOR4)
            print("4번구역 복구완료")            

#============================================================= zone5 close       
        if GPIO.input(GPIO_IN_SENSOR5) == 0 and flag_SENSOR5 == 0:            
            flag_SENSOR5 = 1
            #pubFLag = flag_SENSOR5            
            #pubGPIOIn = GPIO_IN_SENSOR5          
            alarmMessage = MESSAGE_SENSOR5_CLOSE
            print(alarmMessage)
            
            GPIO.output(GPIO_OUT_LED5, True)
            pubMessage.pub_MQTT(str(),str(),alarmMessage)
            
            #smsSend("5번구역에 침입이 발생하였습니다",GPIO_IN_SENSOR5,flag_SENSOR5)
            print("5번구역에 침입이 발생하였습니다!print")
#=============================================================zone5 open           
        elif GPIO.input(GPIO_IN_SENSOR5) == 1 and flag_SENSOR5 == 1:
            flag_SENSOR5 = 0
            #pubFLag = flag_SENSOR5
            #pubGPIOIn = GPIO_IN_SENSOR5
            alarmMessage = MESSAGE_SENSOR5_OPEN
            print(alarmMessage)
            
            GPIO.output(GPIO_OUT_LED5, False)
            pubMessage.pub_MQTT(str(),str(),alarmMessage)
            
            #smsSend("5번구역 복구완료",GPIO_IN_SENSOR5,flag_SENSOR5)
            print("5번구역 복구완료!print") 

#============================================================= zone6 close       
        if GPIO.input(GPIO_IN_SENSOR6) == 0 and flag_SENSOR6 == 0:            
            flag_SENSOR6 = 1
            #pubFLag = flag_SENSOR6            
            #pubGPIOIn = GPIO_IN_SENSOR6          
            alarmMessage = MESSAGE_SENSOR6_CLOSE
            print(alarmMessage)
            
            GPIO.output(GPIO_OUT_LED6, True)
            pubMessage.pub_MQTT(str(),str(),alarmMessage)
            
            #smsSend("6번구역에 침입이 발생하였습니다",GPIO_IN_SENSOR6,flag_SENSOR6)
            print("6번구역에 침입이 발생하였습니다!print")
#=============================================================zone6 open           
        elif GPIO.input(GPIO_IN_SENSOR6) == 1 and flag_SENSOR6 == 1:
            flag_SENSOR6 = 0
            #pubFLag = flag_SENSOR6
            #pubGPIOIn = GPIO_IN_SENSOR6
            alarmMessage = MESSAGE_SENSOR6_OPEN
            print(alarmMessage)
            
            GPIO.output(GPIO_OUT_LED6, False)
            pubMessage.pub_MQTT(str(),str(),alarmMessage)
            
            #smsSend("6번구역 복구완료",GPIO_IN_SENSOR6,flag_SENSOR6)
            print("6번구역 복구완료!print")

#============================================================= zone7 close       
        if GPIO.input(GPIO_IN_SENSOR7) == 0 and flag_SENSOR7 == 0:            
            flag_SENSOR7 = 1
            #pubFLag = flag_SENSOR7            
            #pubGPIOIn = GPIO_IN_SENSOR7          
            alarmMessage = MESSAGE_SENSOR7_CLOSE
            print(alarmMessage)
            
            GPIO.output(GPIO_OUT_LED7, True)
            pubMessage.pub_MQTT(str(),str(),alarmMessage)
            
            #smsSend("7번구역에 침입이 발생하였습니다",GPIO_IN_SENSOR7,flag_SENSOR7)
            print("7번구역에 침입이 발생하였습니다!print")
#=============================================================zone7 open           
        elif GPIO.input(GPIO_IN_SENSOR7) == 1 and flag_SENSOR7 == 1:
            flag_SENSOR7 = 0
            #pubFLag = flag_SENSOR7
            #pubGPIOIn = GPIO_IN_SENSOR7
            alarmMessage = MESSAGE_SENSOR7_OPEN
            print(alarmMessage)
            
            GPIO.output(GPIO_OUT_LED7, False)
            pubMessage.pub_MQTT(str(),str(),alarmMessage)
            
            #smsSend("7번구역 복구완료",GPIO_IN_SENSOR7,flag_SENSOR7)
            print("7번구역 복구완료!print")             

#============================================================= zone8 close       
        if GPIO.input(GPIO_IN_SENSOR8) == 0 and flag_SENSOR8 == 0:            
            flag_SENSOR8 = 1
            #pubFLag = flag_SENSOR8            
            #pubGPIOIn = GPIO_IN_SENSOR8          
            alarmMessage = MESSAGE_SENSOR8_CLOSE
            print(alarmMessage)
            
            GPIO.output(GPIO_OUT_LED8, True)
            pubMessage.pub_MQTT(str(),str(),alarmMessage)
            
            #smsSend("8번구역에 침입이 발생하였습니다",GPIO_IN_SENSOR8,flag_SENSOR8)
            print("8번구역에 침입이 발생하였습니다!print")
#=============================================================zone8 open           
        elif GPIO.input(GPIO_IN_SENSOR8) == 1 and flag_SENSOR8 == 1:
            flag_SENSOR8 = 0
            #pubFLag = flag_SENSOR8
            #pubGPIOIn = GPIO_IN_SENSOR8
            alarmMessage = MESSAGE_SENSOR8_OPEN
            print(alarmMessage)
            
            GPIO.output(GPIO_OUT_LED8, False)
            pubMessage.pub_MQTT(str(),str(),alarmMessage)
            
            #smsSend("8번구역 복구완료",GPIO_IN_SENSOR8,flag_SENSOR8)
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


       
            

            
            
