# FROM python:alpine3.8
FROM tiangolo/uwsgi-nginx:python3.8-alpine
WORKDIR /app
COPY . /app/

RUN /bin/sh -c pip install -r requirement.txt
EXPOSE 5000
CMD [ "python", "app.py" ]