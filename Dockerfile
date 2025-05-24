FROM python:alpine

LABEL environment=Production
LABEL author=Ramkumar
LABEL version=1.0
LABEL description="Store API Services"

COPY . /app

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

ARG HOST=0.0.0.0
ARG PORT=8000

ENV UVICORN_HOST=${HOST:-0.0.0.0}
ENV UVICORN_PORT=${PORT:-8000}

ENTRYPOINT [ "python", "main.py" ]