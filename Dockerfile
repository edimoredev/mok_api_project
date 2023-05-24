# Establece la imagen base
FROM python:3.10-alpine

RUN mkdir /mok_api_project

WORKDIR /mok_api_project

RUN apk update \
  && apk add --no-cache gcc musl-dev postgresql-dev python3-dev libffi-dev \
  && pip install --upgrade pip


COPY requirements.txt /mok_api_project/
RUN pip install -r requirements.txt

EXPOSE 5000

COPY . /mok_api_project/

CMD ["python", "main.py"]