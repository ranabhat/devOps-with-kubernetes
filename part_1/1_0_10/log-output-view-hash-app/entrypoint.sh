#!/bin/sh
echo "Server started in port 5000"

gunicorn -b 0.0.0.0:5000 app:app