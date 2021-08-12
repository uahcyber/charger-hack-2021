from flask import Flask, request, render_template
from subprocess import getoutput

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("home.html")


@app.route('/ping',methods=["POST"])
def ping():
    data = request.json['data']
    output = getoutput("ping -c 1 " + data).replace("\n","<br>")
    output = f'<code>{output}</code><br><br><b>'
    if "1 received" in output:
        output += "Server appears to be up!</b>"
    else:
        output += "Server is DOWN!!</b>"
    return output

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080)