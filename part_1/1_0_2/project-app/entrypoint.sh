#!/bin/sh
echo "Server started in port 5000"

gunicorn -b 127.0.0.1:5000 app:app