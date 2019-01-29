FROM ubuntu:18.10
FROM python:3

WORKDIR /app

COPY . /app

EXPOSE 8000

CMD ["python3", "project.py"]
