# Establece la imagen base
# FROM python:3.10-alpine

# RUN mkdir /mok_api_project

# WORKDIR /mok_api_project

# RUN apk update \
#   && apk add --no-cache gcc musl-dev postgresql-dev python3-dev libffi-dev \
#   && pip install --upgrade pip


# COPY requirements.txt /mok_api_project/
# RUN pip install -r requirements.txt

# EXPOSE 5000

# COPY . /mok_api_project/

# CMD ["python", "main.py"]
FROM python:3.9-alpine

RUN apk update \
  && apk add --virtual build-deps gcc python3-dev musl-dev \
  && apk add postgresql-dev

RUN mkdir /mok_api_project
WORKDIR /mok_api_project

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /mok_api_project/

# CMD ["python", "main.py"]