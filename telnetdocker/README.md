FROM python:2.7

ADD telnetserver.py
ADD telnetclient.py

WORKDIR /telnetdocker/

