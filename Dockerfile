FROM python:3.12
ENV TZ America/Sao_Paulo
RUN apt update ; apt upgrade -y
WORKDIR /usr/app
COPY requirements.txt .
RUN pip install -r requirements.txt uvicorn
COPY . .
RUN pip install .
