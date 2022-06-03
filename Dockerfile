# PYTHON3.9.13
# DJANGO 4.0.4
# PostgreSQL 14.3

FROM python:3.9.13-alpine
#MAINTAINER AARHUS TECH Skoleoplaering

ENV PYTHONUNBUFFERED 1

# Copy the req file
COPY ./requirements.txt /requirements.txt 
# ... and install it into out Docker
RUN pip install -r /requirements.txt

# Copy the files from local into the Docker image
RUN mkdir /frontend
WORKDIR /frontend
COPY ./frontend /frontend

# We don't want the root user so ...
RUN adduser -D user
USER user
