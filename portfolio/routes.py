from flask import render_template
from . import app 


@app.route('/index', methods=['POST', 'GET'])
@app.route('/', methods=['POST', 'GET'])
def index():

    greeting = 'Welcome to My Data Science Portfolio Website'

    return render_template('/index.html',
                            greeting=greeting)