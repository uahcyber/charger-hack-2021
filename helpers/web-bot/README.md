web-bot
=======

this is not a challenge. 

it is the admin bot that players can use to submit things like XSS payloads.

this web server is built to be modular, so future competitions can add their challenges to it by creating new files in `to_copy/challs` containing challenge resolvers.

for instance, an XSS resolver used in Charger Hack 2021 looked like this:

```python
from bases.challengeList import *

class XSSChall(Challenge):

    flag = "UAH{sCr1PTiNG_N0T_sk1PpinG_ACr05s_the_s1tE}"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def do(self, data):
        self.open_path_with_cookie(data,{"flag": self.flag})
```

this challenge can then be added to the challenge list by modifying `app.py:execute_me()`:

```python
@app.before_first_request
def execute_me():
    challs = [
        XSSChall("Blues Billboard",f"{main_url}:38256"),
    ]
    CL.extend(challs)
```

tips
----

don't add special characters that require HTML encoding in the challenge display names. this may be fixed later by using a challenge model such as:

```python
Challenge(id, display_name, url)
```

then, the user would just be directed to `/visit/<id>` instead of `/visit/<name>`. 