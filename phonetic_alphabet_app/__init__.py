
from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__.split('.')[0])

from phonetic_alphabet_app import views
