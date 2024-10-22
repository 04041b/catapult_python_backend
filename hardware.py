import RPi.GPIO as GPIO          
from time import sleep

#enable?    
in1 = 5
in2 = 6
#specify use board number
GPIO.setmode(GPIO.BCM)
#GPIO are output ports
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
#output
def launch():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
sleep(1)

def stop():
    GPIO.output(in2,GPIO.LOW)

def gracefully_shutdown():
    GPIO.cleanup()
    
