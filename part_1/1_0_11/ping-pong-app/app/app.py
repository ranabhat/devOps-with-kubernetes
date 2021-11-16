from flask import Flask
import pickle

app = Flask(__name__)


path = "/usr/src/app/files/pong_count.txt"


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


def write_pong_count(count, file):
    with open(file, 'wb') as data:
        pickle.dump([count], data)

counter = 0 if (read_pong() is None or not read_pong()) else read_pong()

def output_pong():
    global counter
    counter = counter + 1
    output = f"pong {counter}"
    write_pong_count(counter, path)
    return output

@app.route("/pingpong")
def get_pong():
    return output_pong()