FROM locustio/locust:latest

WORKDIR /app

COPY locustfile.py .

CMD ["locust", "-f", "locustfile.py"]

