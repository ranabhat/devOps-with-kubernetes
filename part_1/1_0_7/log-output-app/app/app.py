import uuid
from datetime import datetime
from flask import Flask

app = Flask(__name__)

random_string = uuid.uuid1()

def output_string():
    output = f"{datetime.now()}: {random_string}"
    return output

@app.route("/")
def get_time_stamp():
    return output_string()