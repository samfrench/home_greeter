FROM resin/rpi-raspbian

MAINTAINER Sam French <Sam.French@bbc.co.uk>

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN apt-get -y update
RUN apt-get install -y build-essential git ssh

WORKDIR /home/pi/work

ENV HOME=/home/pi/work

COPY Makefile /home/pi/work/Makefile

RUN make install_system_dependencies
RUN apt-get install -y python3-pip python3-dev
RUN make install_pipenv
RUN rm -rf /usr/local/lib/python3.4/dist-packages/requests*

ADD . /home/pi/work

RUN make install_application_dependencies
