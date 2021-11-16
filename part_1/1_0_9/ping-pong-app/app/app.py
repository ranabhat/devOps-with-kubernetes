from flask import Flask

app = Flask(__name__)

counter = 0

def output_pong():
    global counter
    output = f"pong {counter}"
    counter = counter + 1
    return output

@app.route("/pingpong")
def get_pong():
    return output_pong()