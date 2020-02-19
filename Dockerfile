FROM ubuntu:18.04
# FROM alpine:3.9

RUN apt-get update && apt-get install -y libssl-dev && apt-get install -y python3-pip python3-dev libmysqlclient-dev && apt-get clean
RUN apt-get -y install locales git
RUN locale-gen en_US.UTF-8
ENV LC_ALL en_US.UTF-8

WORKDIR /code
ADD requirements.txt /code/
RUN pip3 install -r requirements.txt
ADD . /code/

EXPOSE 8000

CMD ["python3", "/code/manage.py", "runserver", "0.0.0.0:8000"]

