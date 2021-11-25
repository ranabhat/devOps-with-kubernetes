# Using python alpine official image from Docker hub
FROM python:3.9.5-slim-buster

# By default, listen on port 5000
EXPOSE 5000/tcp

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Use /usr/src/app as our workdir. The following instructions will be executed in this location.
WORKDIR /usr/src/app

# Copy requirements.txt from this location (.) to /usr/src/app/ creating /usr/src/app/<all_contents_from_repo>
COPY requirements.txt .

RUN set -ex \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
        g++  \
    && python -m pip install --no-cache-dir -r requirements.txt \
    && apt-get purge -y --auto-remove g++ \
    && apt-get purge -y --auto-remove \
    && rm -rf /var/lib/apt/lists/*

# add entrypoint.sh
COPY entrypoint.sh .
RUN chmod +x /usr/src/app/entrypoint.sh

# Copy all the contents from this location (./app) to /usr/src/app/ creating /usr/src/app/<all_contents_from_repo>
COPY ./app .

RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /usr/src/app
USER appuser

# run server
CMD ["/usr/src/app/entrypoint.sh"]