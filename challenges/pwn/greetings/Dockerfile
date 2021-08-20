FROM ubuntu:21.10
LABEL maintainer="uahcybersec@uah.edu"
LABEL version="0.1"
LABEL description="pwn challenge 'greetings' for the UAH Cybersecurity Club's 2021 Week of Welcome CTF."

RUN adduser --home /home/ctfuser --shell /bin/bash --disabled-password --gecos "" -q ctfuser
RUN apt-get update
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get -y install xinetd

ADD --chown=root:ctfuser src /home/ctfuser/
COPY chall.xinetd /etc/xinetd.d/chall
RUN touch /var/log/xinetdlog

RUN su ctfuser -c 'rm /home/ctfuser/main.c /home/ctfuser/Makefile'
RUN chmod -R 550 /home/ctfuser

EXPOSE 1337

CMD service xinetd start && sleep 2 && tail -f /var/log/xinetdlog