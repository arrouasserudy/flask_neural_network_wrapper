FROM python:3.6

LABEL version="0.1"

ENV PYTHONDONTWRITEBYTECODE 1
ENV FLASK_APP "backend/app.py"
ENV FLASK_ENV "production"

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/

RUN pip3 install -r requirements.txt

ADD . /app

EXPOSE 8080

RUN chmod +x /app/serve

ENTRYPOINT ["/app/serve"]
