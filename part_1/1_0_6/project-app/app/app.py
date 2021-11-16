from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def introduce():
    return render_template('introduction.html')
