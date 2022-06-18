#pub
FROM python:3.7.1-slim

WORKDIR /app
COPY . . 
RUN pip install -r requirements.txt 

CMD ["python", "publisher.py", "--ip", "0.0.0.0"]
