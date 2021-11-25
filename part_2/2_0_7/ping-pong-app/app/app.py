from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Counter(db.Model):
    __tablename__ = "counters"

    id = db.Column(db.Integer, primary_key=True)
    counter = db.Column(db.Integer)


    def __init__(self, counter):
        self.counter = counter

db.create_all()

if  not db.session.query(Counter).all():
    db.session.add(Counter(counter=0))
    db.session.commit()


def output_pong():
    db_counter = Counter.query.get(1)
    db_counter.counter = db_counter.counter + 1
    output_value = db_counter.counter
    #print(f"db counter {db_counter.counter}")
    db.session.commit()
    output = f"pong {output_value}"
    return output

@app.route("/pingpong")
def get_pong():
    return output_pong()
