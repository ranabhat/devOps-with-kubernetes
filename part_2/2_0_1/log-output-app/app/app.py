import uuid
from datetime import datetime
from flask import Flask
from flask import render_template
import requests
 
app = Flask(__name__)

random_string = uuid.uuid1()

@app.route("/")
def get_log_output():
    response = requests.get(f"http://log-output-ping-pong-app-svc:2346/pingpong") #https://requests.readthedocs.io/en/master/
    response_value_dict = response.text
    output = {
        "timestamp": datetime.now(),
        "hash": random_string,
        "pong_count": response_value_dict
    }

    return render_template('index.html', **output)