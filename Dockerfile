FROM python:3.8.3-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev git

COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN pip install --upgrade pip
COPY . .

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]