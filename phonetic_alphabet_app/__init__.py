from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)

import phonetic_alphabet_app.views
import phonetic_alphabet_app.Game
import phonetic_alphabet_app.Alphabet
import phonetic_alphabet_app.Words
