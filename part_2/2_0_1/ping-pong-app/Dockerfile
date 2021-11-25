# Using python alpine official image from Docker hub
FROM python:3.7-alpine

# By default, listen on port 5001
EXPOSE 5001/tcp

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Use /usr/src/app as our workdir. The following instructions will be executed in this location.
WORKDIR /usr/src/app

# Copy requirements.txt from this location (.) to /usr/src/app/ creating /usr/src/app/<all_contents_from_repo>
COPY requirements.txt .

RUN pip install -r requirements.txt && \
    adduser -D appuser && \
    chown -R appuser /usr/src/app

# add entrypoint.sh
COPY entrypoint.sh .
RUN chmod +x /usr/src/app/entrypoint.sh

# Copy all the contents from this location (./app) to /usr/src/app/ creating /usr/src/app/<all_contents_from_repo>
COPY ./app .

# run server
CMD ["/usr/src/app/entrypoint.sh"]