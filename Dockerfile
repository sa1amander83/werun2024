FROM python:3.10-alpine3.19

COPY requirements.txt /temp/requirements.txt

COPY runapp /back
WORKDIR /back
EXPOSE 8000

#RUN #podman run -p 9000:9000 -p 9001:9001 minio/minio server /data --console-address ":9001"
RUN apk add postgresql-client build-base postgresql-dev

RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password new-user
#RUN -p 127.0.0.1:16379:6379 --name redis-celery -d redis
USER new-user

