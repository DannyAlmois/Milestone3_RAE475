FROM python:latest

ADD udpserver.py /server/
ADD index.html /server/

WORKDIR /server/

