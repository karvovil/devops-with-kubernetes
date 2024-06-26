# Use an official Python 3.11.5 runtime as a parent image
FROM python:3.11.5

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . /app

RUN chmod +x app.py

CMD ["python", "app.py"]