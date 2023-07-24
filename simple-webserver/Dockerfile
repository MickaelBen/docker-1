FROM python:3.9-slim

WORKDIR /usr/src/app

COPY index.html .

CMD ["python", "-m", "http.server", "8000" "-b" "192.168.11.10"]