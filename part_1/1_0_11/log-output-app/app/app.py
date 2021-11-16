import uuid
from datetime import datetime
import pickle
from flask import Flask
from flask import render_template
 
app = Flask(__name__)

path = "/usr/src/app/files/pong_count.txt"

random_string = uuid.uuid1()

def read_pong():
    try:
        with open(path, 'rb') as data:
            pong_count = pickle.load(data)
            return pong_count[0]
    except IOError:
        return 
    except EOFError:
        return 
    except FileNotFoundError:
        return

@app.route("/")
def get_log_output():

    output = {
        "timestamp": datetime.now(),
        "hash": random_string,
        "pong_count": read_pong()
    }

    return render_template('index.html', **output)