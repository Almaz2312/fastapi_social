FROM python:3.10-slim-bullseye
ENV PYTHONBUFFERED=1

WORKDIR /fastapi_dweeter

RUN pip install --upgrade pip
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt


COPY . .
