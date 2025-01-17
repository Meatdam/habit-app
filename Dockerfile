FROM python:3.11

ENV PYTHONDONTWRITEBYCODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY /requirements.txt /

RUN pip install -r /requirements.txt --no-cache-dir

COPY . .
