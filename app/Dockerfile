# pull official base image
FROM python:3.11.2-slim-buster

# set working directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
  && apt-get -y install netcat gcc postgresql \
  && apt-get clean

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
COPY ./requirements-dev.txt /usr/src/app/requirements-dev.txt
RUN pip install -r requirements-dev.txt

# install pytest
RUN pip install pytest

# copy app files
COPY . .

# set entrypoint
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]



