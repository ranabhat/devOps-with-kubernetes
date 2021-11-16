import uuid
import time
from datetime import datetime

random_string = uuid.uuid1()

def output_string():
    print(f"{datetime.now()} {random_string}")
    return 

output_string()
while True:
    time.sleep(5)
    output_string()