import RPi.GPIO as GPIO # type: ignore
from flask import Flask
from flask import send_from_directory
import os
app = Flask(__name__)

@app.route("/<path:name>")
def hello_world(name):
    return send_from_directory(
    
    )