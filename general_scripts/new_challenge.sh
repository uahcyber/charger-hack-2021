#!/usr/local/bin/bash

# generates a new challenge subdirectory with default file structure
# for use in the UAH Cybersecurity Club 2021 Week of Welcome CTF 

SAVED_PWD=`pwd`
USED_PORTS=("22" "80") # add any ports actively used by the host server here

echo "Creating new CTF challenge"
read -p "Category: " CATEGORY
read -p "Name: " NAME

cd "$(dirname "$0")" # get into script directory to reference ../challenges

if [ -d "../challenges/$CATEGORY/$NAME" ]; then
    echo "Challenge with name $NAME already created in the $CATEGORY category"
    exit
fi

read -p "Description: " DESC
read -p "Needs Docker? [y/n]: " NEEDS_DOCKER

mkdir -p ../challenges/$CATEGORY/$NAME/solution
touch ../challenges/$CATEGORY/$NAME/flag.txt
mkdir -p ../challenges/$CATEGORY/$NAME/dist

echo -n $DESC >> ../challenges/$CATEGORY/$NAME/description.txt

if [ ${NEEDS_DOCKER^^} == "Y" ]; then
    read -p "What port will need to be exposed from the container?: " PORT
    mkdir -p ../challenges/$CATEGORY/$NAME/to_copy
    cat <<EOT >> ../challenges/$CATEGORY/$NAME/Dockerfile
FROM ubuntu:21.10
LABEL maintainer="uahcybersec@uah.edu"
LABEL version="0.1"
LABEL description="$CATEGORY challenge '$NAME' for the UAH Cybersecurity Club's 2021 Week of Welcome CTF."

RUN adduser --home /home/ctfuser --shell /bin/bash --disabled-password --gecos "" -q ctfuser

ADD --chown=root:ctfuser to_copy /home/ctfuser/
RUN chmod -R 550 /home/ctfuser
COPY start.sh /start.sh

CMD ["su","ctfuser","./start.sh"]

EXPOSE $PORT
EOT

    cat <<EOT >> ../challenges/$CATEGORY/$NAME/start.sh
#!/bin/bash

# BEGIN DONT TOUCH
cd /home/ctfuser
# END DONT TOUCH

# modify me to run the challenge
EOT
    chmod +x ../challenges/$CATEGORY/$NAME/start.sh
    readarray -t FOUND_PORTS < <(grep -rnw "docker run -it --rm -p" ../challenges/ | cut -d':' -f3 | awk -F'-it --rm -p ' '{ print $NF }')
    USED_PORTS+=("${FOUND_PORTS[@]}")    
    while true; do
        FPORT=`shuf -i1024-65535 -n1`
        # if new port is not in array of already used host ports
        if [[ ! " ${USED_PORTS[@]} " =~ " ${FPORT} " ]]; then
            break
        fi
    done
    cat <<EOT >> ../docker-compose.yaml
  ${CATEGORY,,}-${NAME,,}:
    restart: always
    build:
      context: "./challenges/${CATEGORY,,}/${NAME,,}"
      dockerfile: "./Dockerfile"
    ports:
      - "$FPORT:$PORT"
EOT
    echo "Place any final binaries/flag files in $CATEGORY/$NAME/to_copy and modify $CATEGORY/$NAME/start.sh as needed."
    echo "To test the container, run $CATEGORY/$NAME/test.sh as root."
fi

echo "Created challenge in $CATEGORY/$NAME!"
cd $SAVED_PWD
exit