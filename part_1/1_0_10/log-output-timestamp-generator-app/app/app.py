import uuid
import time
import pickle
from datetime import datetime

random_string = uuid.uuid1()
path = "/usr/src/app/files/timestamp.txt"

def output_string():
    output_string = datetime.now()
    return output_string

def write_time_stamp(timestamp, file):
    with open(file, 'wb') as data:
        pickle.dump([timestamp], data)

while True:
    time.sleep(5)
    write_time_stamp(output_string(), path)