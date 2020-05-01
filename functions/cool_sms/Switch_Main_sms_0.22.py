# -*- coding: utf-8 -*-

#시간관련 모듈 선언
import datetime

#필요한 외부 파이썬 모듈 선언
import RPi.GPIO as GPIO
from time import sleep
#import MQTT_Pub as PUB

#======================== sms  sdk sms 모듈호출
import sys
sys.path.insert(0, "../../")

from sdk.api.message import Message
from sdk.exceptions import CoolsmsException

#문자발송제한변수
flag_sms_send_count = 0
CONST_SMS_MAX_SEND_VALUE = 2 #문자를 최대 5번 전송한다.

# Alarm발생시간 및 경과시간
CONST_ALARM_ELASPED_TIME = 1 #30분 후에 다시 SMS발송한다.
alarm_start_time = datetime.datetime.now() -  datetime.timedelta(hours=2)
alarm_elapsed_time = ""
alarm_check_flag = False
alarm_before_gpio = 0
alarm_before_flag = 0


#상황별 변수 설정
flag_Security = 0 #0 = 보안 해제 , 1 = 보안설정
flag_Door = 0     #0 = 문이 열림 , 1 = 문이 닫힘

#MQTT로 전송할 데이터 저장 변수 
#pubFLag = -1
#pubGPIOIn = -1
alarmMessage = "-1"
    
#zone1 GPIO
GPIO_IN_SECURITY = 16
GPIO_OUT_SECURITY = 23 # led 출력
MESSAGE_SECURITY_SETUP = "화재감지기 복구!!"
MESSAGE_SECURITY_INTRUSION = "화재감지기 작동!!"

#zone2 GPIO
GPIO_IN_DOOR = 20
GPIO_OUT_DOOR = 24 #led 출력
MESSAGE_DOOR_CLOSE = "상용전원 공급중!!"
MESSAGE_DOOR_OPEN = "정전발생!"

#호출 정보 (alarmFlag,alarmGPIO,alarmDesc)
# Flag값,GPIO입력값,Alarm내용
#pubMessage = PUB.MQTTPublisher()
#Test Sample 
#pubMessage.pub_MQTT("ATEST","BTEST","CTEST")

#상황별 GPIO 설정모드
print("상황별 GPIO 설정모드")
GPIO.setmode(GPIO.BCM)

#보안 스위치 GPIO 설정 (Setup)
print("화재감지기 복구설정 완료  (Setup)")
GPIO.setup(GPIO_IN_SECURITY, GPIO.IN )
GPIO.setup(GPIO_OUT_SECURITY, GPIO.OUT)

#문 스위치 GPIO 설정 (Setup)
print("정전 복구설정 완료 (Setup)")
GPIO.setup(GPIO_IN_DOOR, GPIO.IN)
GPIO.setup(GPIO_OUT_DOOR, GPIO.OUT, initial=0)

print("Switch Setting End")

# set api key, api secret
api_key = "NCSBQ9QL4QIB6AHB"
api_secret = "NO3K7ATJ8B8FKZNWKBNHPDRXUQQTYSE6"

## 4 params(to, from, type, text) are mandatory. must be filled
params = dict()
params['type'] = 'sms' # Message type ( sms, lms, mms, ata )
params['to'] = '01074704184' # Recipients Number 
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
    
    print("SMS를 발송합니다.")
    alarm_sms_send = False

    if alarm_sms_send:
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
#============================================================= zone1 close       
        if GPIO.input(GPIO_IN_SECURITY) == 0 and flag_Security == 0:            
            flag_Security = 1
            #pubFLag = flag_Security            
            #pubGPIOIn = GPIO_IN_SECURITY            
            alarmMessage = MESSAGE_SECURITY_SETUP
            print(alarmMessage)            
            GPIO.output(GPIO_OUT_SECURITY, True)
            
            smsSend("화재감지기가 복구되었습니다.!!",GPIO_IN_SECURITY,flag_Security)
            print("화재감지기가 작동하였습니다.!!")
#============================================================zone1 open           
        elif GPIO.input(GPIO_IN_SECURITY) == 1 and flag_Security == 1:
            flag_Security = 0
            #pubGPIOIn = GPIO_IN_SECURITY
            alarmMessage = MESSAGE_SECURITY_INTRUSION
            print(alarmMessage)           
            GPIO.output(GPIO_OUT_SECURITY, False)

            smsSend("화재감지기가 작동하였습니다.!!",GPIO_IN_SECURITY,flag_Security)  #복구되었습니다.!!"
            print("화재감지기가 복구되었습니다.!!")
#========================================================= zone2 close           
        if GPIO.input(GPIO_IN_DOOR) == 0 and flag_Door == 0:
            flag_Door = 1
            #pubFLag = flag_Door
            #pubGPIOIn = GPIO_IN_DOOR
            alarmMessage = MESSAGE_DOOR_CLOSE
            print(alarmMessage) 
            GPIO.output(GPIO_OUT_DOOR, True)
            
            smsSend("상용전원 공급중입니다!!",GPIO_IN_DOOR,flag_Door)
            #print("상용전원 공급중입니다!!")
#=================================================================== zone2 open            
        elif GPIO.input(GPIO_IN_DOOR) == 1 and flag_Door == 1:
            flag_Door = 0           
            #pubFLag = flag_Door
            #pubGPIOIn = GPIO_IN_DOOR
            alarmMessage = MESSAGE_DOOR_OPEN
            print(alarmMessage) 
            GPIO.output(GPIO_OUT_DOOR, False)

            smsSend("정전발생! 정전발생!",GPIO_IN_DOOR,flag_Door)
            #print("정전발생! 정전발생!")
            
            #sleep(300) #20초 간격으로 계속 보내게 하기!
except KeyboardInterrupt:
    GPIO.cleanup()
    print("테스트 종료 ~")  #clt+c
    #client.disconnect()



import sys
sys.exit()    
#print (pubMessage)
#pubMessage.pub_MQTT("A","B","C")


       
            

            
            
