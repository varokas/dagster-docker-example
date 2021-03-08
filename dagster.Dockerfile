FROM python:3.8

RUN pip install dagster dagster-postgres dagit

RUN mkdir /dagster
COPY dagster.yaml /dagster/dagster.yaml



RUN mkdir /app
WORKDIR /app

