# syntax=docker/dockerfile:1

FROM ubuntu:18.04

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev
RUN apt-get install -y sqlite3 libsqlite3-dev

COPY ./requirements.txt /src/requirements.txt

WORKDIR /src

RUN pip3 install -r /src/requirements.txt

COPY ./src /src

RUN sqlite3 /src/quiz.db < /src/quiz.sql

RUN python3 adduser.py

EXPOSE 80
EXPOSE 8080

ENTRYPOINT [ "python3",  "/src/softdes.py" ]

CMD [ "/src/softdes.py" ]