# Using python alpine official image from Docker hub
FROM python:3.7-alpine

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Use /usr/src/app as our workdir. The following instructions will be executed in this location.
WORKDIR /usr/src/app

# Copy all the contents from this location (./app) to /usr/src/app/ creating /usr/src/app/<all_contents_from_repo>
COPY ./app .

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -D appuser && \
    chown -R appuser /usr/src/app

CMD ["python3", "app.py"]