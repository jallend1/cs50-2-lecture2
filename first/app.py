from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!"

@app.route("/jason")
def jason():
    return("Hello Jason!")

@app.route("/paula")
def paula():
    return("Hello Paula!")

@app.route("/<string:name>")
def hello(name):
    return f"Hello, Mr/Ms {name}"
