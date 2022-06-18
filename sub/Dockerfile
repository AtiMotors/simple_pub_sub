#sub
FROM python:3.7.1-slim

WORKDIR /app
COPY . . 
RUN pip install -r requirements.txt 

# when using docker-compose, this command can be overwritten
CMD ["python", "subscriber.py", "--ip", "0.0.0.0"]
