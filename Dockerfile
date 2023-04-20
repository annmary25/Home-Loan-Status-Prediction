FROM python:3.10-slim-buster
WORKDIR /HOME-LOAN-STATUS-PREDICTION
COPY . /HOME-LOAN-STATUS-PREDICTION
RUN apt update -y 
RUN apt-get update && pip install -r requirements.txt
CMD ["python3", "app.py"]

