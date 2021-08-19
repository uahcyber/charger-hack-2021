from flask import abort, Flask, request, render_template
import urllib.parse
from bases.challengeList import ChallengeList
from challs.xss import XSSChall

app = Flask(__name__)

#main_url = "http://challs.ctf.uahcyber.club"

main_url = "http://127.0.0.1"

CL = None

@app.route('/')
def home():
    return render_template("home.html",challenges=CL.challs)

@app.route('/bot/<name>')
def bot(name):
    chall = CL.getFromName(name)
    if not chall:
        abort(404)
    return render_template("bot.html",challenge=chall)

@app.route('/visit/<name>',methods=["POST"])
def visit(name):
    chall = CL.getFromName(name)
    if not chall:
        abort(404)
    data = request.json['data']
    chall.do(data) # maybe do urllib.parse.quote() here, not sure
    return "sent request"

if __name__ == "__main__":
    challs = [
        XSSChall("test",f"{main_url}:5000"),
    ]
    CL = ChallengeList(challs)
    app.run(host="0.0.0.0")