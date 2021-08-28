FROM python:3.8-slim

ENV CONTAINER_HOME=/var/www

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

ADD . $CONTAINER_HOME
WORKDIR $CONTAINER_HOME

RUN pip install -r $CONTAINER_HOME/requirements.txt