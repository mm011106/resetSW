# -*- coding:utf-8 -*-
#!/usr/bin/python2.7
#
#　シャットダウンスイッチのハンドリング
#　use GPIO 17 as input, upll-up
#
#  GPIO17を3秒程度 Lo に保持すると、シャットダウンプロセスを起動するスクリプト
#　短時間の押下では反応しないようになっている

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
pin = 17

def gpioInterrupt(channel):
    print("Capture the falling edge !")
    sw_counter=0

    while True:
        sw_status = GPIO.input(pin)
        sw_counter = sw_counter + 1
        
        if sw_status == 0:
            if sw_counter >= 300:
                # in case the signal fixed to "Low" in 3sec
                print(".. Will you stop, Dave? Stop, Dave. I'm afraid.....")
          # os.system("sudo shutdown -h now")
                break
        else:
            # in case the signal got back to stedy state within 3sec
            print("I'm sorry Dave, I'm afraid You can't do that")
            break

        time.sleep(0.01)
    return sw_counter

# make the 'pin' input and pulled up.
GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)
# capture the falling edge of the signal, estimated bounce would be 0.5s and call a funcgtion
GPIO.add_event_detect(pin, GPIO.FALLING, callback=gpioInterrupt, bouncetime=500)

try:
    while(True):
        time.sleep(10)

except KeyboardInterrupt:
    print("break")
    GPIO.cleanup()
