FROM python:3.12.3-alpine3.20

ENV PYTHONUNBUFFERED 1
ARG APP_PORT

COPY ./requirements.txt /tmp/requirements.txt
COPY ./src /app
WORKDIR /app
EXPOSE $APP_PORT

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    rm -rf /tmp
ENV PATH="/py/bin:$PATH"

RUN adduser \
        --disabled-password \
        --no-create-home \
        you-book-user
USER you-book-user
