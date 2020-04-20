from flask import (Flask, render_template)
app = Flask(__name__)

@app.route('/')
def index():
    return "Hi!"

@app.route('/word/<string:name>')
def hello(name):
    return ("Hello, {}!".format(name))


@app.route('/<string:name>')
def showAPage(name): 
    language = name
    return render_template('index.html', language=language)
