FROM python:latest
COPY requirements.txt .
RUN pip install -r requirements.txt
# RUN apt-get update -y; apt-get install redis-tools -y
ADD scripts/* /server/
WORKDIR /server/
