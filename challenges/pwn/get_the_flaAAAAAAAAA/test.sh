#!/bin/bash
docker build -t pwn-get_the_flaaaaaaaaaa .
echo "hosting pwn-get_the_flaaaaaaaaaa on: localhost 50371"
docker run -it --rm -p 50371:1337 --name test-pwn-get_the_flaaaaaaaaaa pwn-get_the_flaaaaaaaaaa #/bin/bash
