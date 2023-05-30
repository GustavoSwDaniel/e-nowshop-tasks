FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONHTTPSVERIFY=0


RUN apt-get -y update && \
    apt-get install -y --no-install-recommends make wget gcc python3-dev libzbar0 && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /usr/async_tasks

COPY ./async_tasks .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt --trusted-host 44.211.201.219
CMD [ "celery", "-A", "async_tasks.tasks.orders", "worker", "--loglevel=info" ]

