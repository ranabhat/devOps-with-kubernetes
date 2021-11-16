import uuid
import pickle
from flask import Flask

app = Flask(__name__)

random_string = uuid.uuid1()
path = "/usr/src/app/files/timestamp.txt"

def read_timestamp():
    try:
        with open(path, 'rb') as data:
            timestamp = pickle.load(data)
            return timestamp[0]
    except IOError:
        return 
    except EOFError:
        return 

def output_timestamp_hash(timestamp, hash):
    if timestamp is None:
        return f""
    output = f"{timestamp}: {hash}"
    return output

@app.route("/")
def get_time_stamp():
    return output_timestamp_hash(read_timestamp(), random_string)