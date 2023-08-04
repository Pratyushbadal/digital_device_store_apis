# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT ["gunicorn", \
        "device_server.wsgi:application" ]

CMD ["--bind=0.0.0.0:8000", \
     "--timeout=180", \
     "--enable-stdio-inheritance", \
     "--worker-class=gthread", \
     "--workers=1", \
     "--threads=2", \
     "--log-level=debug"]
