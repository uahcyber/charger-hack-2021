FROM ubuntu:21.10
LABEL maintainer="uahcybersec@uah.edu"
LABEL version="0.1"
LABEL description="web challenge 'hacker-name-generator' for the UAH Cybersecurity Club's 2021 Week of Welcome CTF."

RUN adduser --home /home/ctfuser --shell /bin/bash --disabled-password --gecos "" -q ctfuser

RUN apt-get update
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get -y install php php-xml

ADD --chown=root:ctfuser to_copy /home/ctfuser/
RUN chmod -R 550 /home/ctfuser
COPY start.sh /start.sh
COPY flag.txt /flag.txt

CMD ["su","ctfuser","./start.sh"]

EXPOSE 8000
