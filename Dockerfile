FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY Makefile /app/
RUN apt-get update && apt-get install -y make

COPY ./src /app/

EXPOSE 8000

ENTRYPOINT ["make", "runserver"]