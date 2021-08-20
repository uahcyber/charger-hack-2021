from flask import Flask, render_template

app = Flask(__name__)

images = [
    'laid-back.jpg',
    'posted-up.jpg',
    'grandpa-blue.jpg'
]

@app.route('/')
def hello():
    return render_template("home.html", images=images)

@app.route('/display/<image>/')
def display(image):
    return render_template("display.html",image=image)

if __name__ == "__main__":
    app.run(host="0.0.0.0")