#import RPi.GPIO as GPIO # type: ignore
from flask import Flask
from flask import send_from_directory,redirect, url_for
import launch from hardware
import os
app = Flask(__name__,static_folder='public')



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
    launch()


app.run()