from flask import Flask
from markupsafe import escape

app = Flask(__name__)
@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def helloworld():
    return 'Hello, World'

@app.route("/<name>")

def hello(name):
    return f"Hello, {escape(name)}!"
