FROM python:3.10-alpine3.19

COPY requirements.txt /temp/requirements.txt

COPY back /back
WORKDIR /back
EXPOSE 8000


RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password new-user

USER new-user

