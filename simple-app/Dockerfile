FROM python:3.9-slim

WORKDIR /opt/demo/
COPY /app .

RUN pip install -r requirements.txt

ENTRYPOINT python app.py