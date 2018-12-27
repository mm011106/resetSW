# -*- coding:utf-8 -*-
#
import RPi.GPIO as GPIO
import time 

GPIO.setmode(GPIO.BCM)
pin = 17

def callBackTest(channel):
    print("callback")
    sw_counter=0
    while True:
        sw_status = GPIO.input(pin)
        sw_counter = sw_counter + 1
        if sw_status == 0:
            if sw_counter >= 300:
                print("長押し検知！")
          # os.system("sudo shutdown -h now")
                break
        else:
            print("短押し検知")
            break

        time.sleep(0.01)
    return sw_counter

GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)
GPIO.add_event_detect(pin, GPIO.FALLING, callback=callBackTest, bouncetime=500) 

try:
    while(True):
        time.sleep(1)

except KeyboardInterrupt:
    print("break")
    GPIO.cleanup()
