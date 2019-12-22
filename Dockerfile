FROM python:3.6.8

EXPOSE 9000

WORKDIR /usr/src

COPY . .

RUN pip install -r requirements.txt
