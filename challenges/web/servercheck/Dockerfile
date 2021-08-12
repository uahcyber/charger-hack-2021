FROM ubuntu:21.10
LABEL maintainer="uahcybersec@uah.edu"
LABEL version="0.1"
LABEL description="web challenge 'servercheck' for the UAH Cybersecurity Club's 2021 Week of Welcome CTF."

RUN adduser --home /home/ctfuser --shell /bin/sh --disabled-password --gecos "" -q ctfuser

RUN apt-get update
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get -y install python3-pip iputils-ping
RUN pip3 install Flask

ADD to_copy /home/ctfuser/
RUN chmod -R 755 /home/ctfuser
COPY start.sh /start.sh

CMD ["su","ctfuser","./start.sh"]

EXPOSE 8080
