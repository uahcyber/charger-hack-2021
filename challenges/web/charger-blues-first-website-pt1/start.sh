#!/bin/bash

# BEGIN DONT TOUCH
cd /home/ctfuser
# END DONT TOUCH

# modify me to run the challenge

gunicorn --bind 0.0.0.0:5000 server:app
