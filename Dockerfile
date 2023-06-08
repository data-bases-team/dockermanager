FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

WORKDIR /dockermanager

COPY req.txt req.txt
RUN pip3 install -r req.txt

COPY . /dockermanager

EXPOSE 8001
