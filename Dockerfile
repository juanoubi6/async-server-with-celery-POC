FROM python:3.6.8

EXPOSE 9000

RUN mkdir -p /usr/src
WORKDIR /usr/src

COPY requirements.txt /usr/src
RUN pip install -r requirements.txt

COPY . .
