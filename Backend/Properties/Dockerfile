# base image
FROM python:3.12

# setup environment variable
ENV DockerHOME=/app/src
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# set work directory
WORKDIR $DockerHOME

# install dependencies
RUN pip install --upgrade pip

# copy requirements to your docker home directory.
COPY requirements.txt $DockerHOME

# run this command to install all dependencies
RUN pip install -r requirements.txt