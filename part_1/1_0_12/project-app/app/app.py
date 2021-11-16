from flask import Flask
from flask import render_template
import requests
import os
import shutil
import pickle
from datetime import datetime

image_storage_volume_path = "/usr/src/app/files/image_name.jpg"

day_storage_file_path = "/usr/src/app/files/day.txt"

image_path = "/usr/src/app/static/image_name.jpg"

app = Flask(__name__)

image_url = "https://picsum.photos/1200"

current_day = 0

def read_current_day(file_path):
    try:
        with open(file_path, 'rb') as data:
            day = pickle.load(data)
            return day[0]
    except IOError:
        return 
    except EOFError:
        return 
    except FileNotFoundError:
        return

def write_current_day(file_path, day):
    with open(file_path, 'wb') as data:
        pickle.dump([day], data)

def check_if_different_day(file_path):
    global current_day
    today = datetime.now().day
    if current_day and (current_day == today):
        return False

    elif current_day and (current_day != today):
        write_current_day(file_path, today)
        current_day = today
        return True

    elif not current_day and read_current_day(file_path) is None:
        write_current_day(file_path, today)
        current_day = today
        return True

    elif not current_day and read_current_day(file_path) == today:
        current_day = today
        return False

    elif not current_day and read_current_day(file_path) != today:
        write_current_day(file_path, today)
        current_day = today
        return True

    elif current_day and read_current_day(file_path) is None:
        write_current_day(file_path, today)
        if current_day == today:
            return False
        else:
            current_day = today
            return True

def write_image(image_path, image_url):
    img_data = requests.get(image_url)
    with open(image_path, 'wb') as handler:
        handler.write(img_data.content)

def check_if_image_exists(path):
    return os.path.exists(path)

def action_if_img_exists_only_in_volume():
    shutil.copy2('/usr/src/app/files/image_name.jpg', '/usr/src/app/static/image_name.jpg')
    return

def action():
    if check_if_different_day(day_storage_file_path) or (not check_if_image_exists(image_path) and not check_if_image_exists(image_storage_volume_path)):
        write_image(image_storage_volume_path, image_url)
        action_if_img_exists_only_in_volume()
    elif not check_if_image_exists(image_path) and check_if_image_exists(image_storage_volume_path):
        action_if_img_exists_only_in_volume()
    return


@app.route("/")
def introduce():
    action()
    return render_template('introduction.html')
