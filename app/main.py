from flask import Flask


APP = Flask(__name__)

@APP.route('/')
def index():
    return 'Welcome to the Index'

### Code Goes Here ###