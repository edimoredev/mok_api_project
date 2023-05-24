FROM python:3.10-alpine

ENV PYTHONUNBUFFERED 1


RUN apk update \
  && apk add --no-cache gcc musl-dev postgresql-dev python3-dev libffi-dev \
  && pip install --upgrade pip

RUN mkdir /mok_api_project

WORKDIR /mok_api_project


COPY requirements.txt /mok_api_project/
RUN pip install -r requirements.txt


COPY . /mok_api_project/
