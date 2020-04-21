from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def sayHi():
    return "Hello!"

@app.route("/webpage")
def displayPage():
    return render_template("index.html")

@app.route("/<string:name>")
def specificHi(name):
    name = name.capitalize()
    return f"Hello, {name}!"