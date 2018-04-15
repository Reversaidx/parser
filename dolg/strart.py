from flask import Flask
import dolg
from flask import request, send_file
import readline
import os
import subprocess
import datetime, time
from time import sleep
app = Flask(__name__)
kurwa=''
@app.route('/')
def index():
    return 'Index Page'
@app.route('/dolg')
def dolgs():
    return dolg.dolg()
if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=3020)