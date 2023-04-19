FROM python:3.10-slim-buster
WORKDIR /HOME-LOAN-STATUS-PREDICTION
COPY . /HOME-LOAN-STATUS-PREDICTION
RUN apt update -y && apt install awscli -y
RUN pip install -r requirements.txt
CMD python app.py

