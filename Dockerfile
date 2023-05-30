FROM python:3.10

WORKDIR /usr/src/app
ENV PYTHONDONTWRITEBYTHECODE 1
ENV PYTHONUNBUFFERED 1 

RUN pip install --upgrade pip
COPY ./newstand/requirements.txt .
RUN pip install -r requirements.txt

COPY ./newstand .
