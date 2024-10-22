import RPi.GPIO as GPIO # type: ignore
from flask import Flask
from flask import send_from_directory,redirect, url_for
from hardware import launch
import os
from time import sleep
app = Flask(__name__,static_folder='public')

in1 = 5
in2 = 6
GPIO.setmode(GPIO.BCM)
#GPIO are output ports
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)

@app.route("/")
def indexhtml():
    return send_from_directory(app.static_folder,"index.html")

@app.route("/<path:name>")
def hello_world(name):
    print(name)

    return send_from_directory(
    app.static_folder,name
    )

@app.route("/api/launch")
def run_launch():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    sleep(1)
    GPIO.output(in2,GPIO.LOW)
    return "success"


app.run()