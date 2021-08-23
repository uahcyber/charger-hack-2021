UAH Week of Welcome CTF 2021
============================

Scripts and resources for the UAH Cybersecurity Club's 2021 Week of Welcome CTF. 

Usage
-----

To create a new challenge, run:

```bash
./general_scripts/new_challenge.sh
```

To start all challenges, run:

```bash
sudo docker-compose up --build [-d]
```

Challenge Access
----------------

The following addresses in IP:PORT form can be used to access each challenge. This is assuming you are running the challenges on localhost (127.0.0.1), if you are running them elsewhere, just replace the IP:

  * **web/servercheck** - `127.0.0.1:25870`
  * **web/animal-farm** - `127.0.0.1:63122`
  * **web/charger-blues-first-website-pt1** - `127.0.0.1:46081`
  * **web/hacker-name-generator** - `127.0.0.1:34554`
  * **web/blues-billboard** - `127.0.0.1:38256`
  * **pwn/greetings** - `127.0.0.1:19601`
  * **pwn/get_the_flaaaaaaaaaa** - `127.0.0.1:50371`
  * **pwn/insert** - `127.0.0.1:17424`
  * **re/babylock** - `127.0.0.1:15727`
  * **misc/catz** - `127.0.0.1:36416`
  * **misc/calc** - `127.0.0.1:15867`
  * **helpers/web-bot** (not a challenge, just admin bot for XSS) - `127.0.0.1:25870`
