FROM ubuntu:16.04

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

COPY ./requirements.txt /requirements.txt

WORKDIR /

RUN pip install -r requirements.txt

COPY . /

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD [ "app/app.py" ]