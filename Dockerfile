FROM python:3.10.4-alpine

RUN mkdir /project
WORKDIR /project

COPY requirements.txt /project

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev


RUN pip install --no-cache-dir -r requirements.txt

COPY . /project

RUN mkdir -p /var/log/gunicorn

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]