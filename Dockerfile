FROM python:alpine3.7

COPY src /app/src
COPY requirements.txt /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD python -m src
