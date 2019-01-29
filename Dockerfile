#pull python image
FROM python:3.6

#make a working directory called app
WORKDIR /app

#copy contents of source into the app directory
COPY . /app

#expose containers port
EXPOSE 8000

#run the project script
CMD ["python3", "project.py"]
