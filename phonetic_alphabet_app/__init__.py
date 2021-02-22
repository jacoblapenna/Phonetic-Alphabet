from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)

import phonetic_alphabet_app.views
