#!/bin/sh
echo "Server started in port 5001"

gunicorn -b 0.0.0.0:5001 app:app