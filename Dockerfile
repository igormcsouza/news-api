FROM python:3.7-slim

RUN pip install --upgrade pip

COPY requirements.txt /opt/requirements.txt
RUN pip install -r /opt/requirements.txt

WORKDIR /app
COPY app.py /app/app.py
COPY test_app.py /app/test_app.py

CMD uvicorn app:app --port $PORT
