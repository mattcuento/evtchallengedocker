FROM ubuntu:18.10
FROM python:3

WORKDIR /app

COPY . /app

CMD ["/bin/bash", "start.sh"]
