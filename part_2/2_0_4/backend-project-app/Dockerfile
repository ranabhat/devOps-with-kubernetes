# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim-buster

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Use /usr/src/app as our workdir. The following instructions will be executed in this location.
WORKDIR /usr/src/app

# Copy requirements.txt from this location (.) to /usr/src/app/ creating /usr/src/app/<all_contents_from_repo>
COPY requirements.txt .

# httptools doesn't have wheel files published on PyPI, only source files, 
# so install g++ prior to installing fastapi[all], and remove it later.
RUN set -ex \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
        g++ \
    && python -m pip install --no-cache-dir -r requirements.txt \
    && apt-get purge -y --auto-remove g++ \
    && apt-get purge -y --auto-remove \
    && rm -rf /var/lib/apt/lists/*


COPY . /usr/src/app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /usr/src/app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "-k", "uvicorn.workers.UvicornWorker", "app.main:app"]
