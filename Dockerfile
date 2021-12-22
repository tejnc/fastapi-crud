FROM python:3.9-slim-bullseye

# set environment variables
ENV PYTHONWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

# set working directory
WORKDIR /code

# copy depencencies
COPY requirements.txt /code/

RUN pip install --upgrade pip
RUN apt-get -y update

# install dependencies
RUN pip install -r requirements.txt

# copy project
COPY . /code/