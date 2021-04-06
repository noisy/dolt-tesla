FROM python:3.8
ENV PYTHONUNBUFFERED 1
ENV DOLT_VERSION=0.25.0

RUN apt update \
    && apt update \
    && apt install -y curl \
    && curl -L https://github.com/dolthub/dolt/releases/download/v${DOLT_VERSION}/install.sh | bash

WORKDIR /tesla
COPY requirements.txt /tesla/requirements.txt
RUN pip install -r requirements.txt
COPY . /tesla
