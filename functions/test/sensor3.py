# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

ZONE1 = 16
ZONE2 = 20
ZONE3 = 21

LED1 = 23
LED2 = 24
LED3 = 25

ZONE1_flag = 0
ZONE2_flag = 0
ZONE3_flag = 0

GPIO.setmode(GPIO.BCM)

GPIO.setup(ZONE1, GPIO.IN )
GPIO.setup(LED1, GPIO.OUT)

GPIO.setup(ZONE2, GPIO.IN )
GPIO.setup(LED2, GPIO.OUT)

GPIO.setup(ZONE3, GPIO.IN )
GPIO.setup(LED3, GPIO.OUT)

#print("1,2번구역 보안이 해제되었습니다.")

#print("버튼을 누르세요!  (CTL-C to exit)")

# If switch pressed on, sw_flag = 1
try:
    
    
	
    while True:

#=============================================zone1        
        if GPIO.input(ZONE1)==0 and ZONE1_flag == 0:
            ZONE1_flag = 1
            GPIO.output(LED1, True)
            print ("1번구역 보안설정")
            
        elif GPIO.input(ZONE1) ==1 and ZONE1_flag == 1:
            ZONE1_flag = 0
            GPIO.output(LED1, False)
            print ("1번구역 보안해제")
#=============================================zone2
        if GPIO.input(ZONE2)==0 and ZONE2_flag == 0:
            ZONE2_flag = 1
            GPIO.output(LED2, True)
            print ("2번구역 보안설정")

        elif GPIO.input(ZONE2) ==1 and ZONE2_flag == 1:
            ZONE2_flag = 0
            GPIO.output(LED2, False)
            print ("2번구역 보안해제")
#=============================================zone3
        if GPIO.input(ZONE3)==0 and ZONE3_flag == 0:
            ZONE3_flag = 1
            GPIO.output(LED3, True)
            print ("3번구역 보안설정")

        elif GPIO.input(ZONE3) ==1 and ZONE3_flag == 1:
            ZONE3_flag = 0
            GPIO.output(LED3, False)
            print ("3번구역 보안해제")



            
        time.sleep(2)        

except KeyboardInterrupt:
    GPIO.cleanup()
    print("Finished!")

import sys
sys.exit()

 
