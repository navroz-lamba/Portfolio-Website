from flask import Flask, url_for

app = Flask(__name__)


from . import routes