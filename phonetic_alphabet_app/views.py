from flask import render_template, url_for, redirect, abort, request
from flask_socketio import SocketIO

from phonetic_alphabet_app import app
from phonetic_alphabet_app.Game import Game

socket = SocketIO(app)

game = Game()

@app.route('/')
def landing():
    return render_template("landing.html")

@app.route("/quiz/<order>")
def serve_game(order):

    game_state = {"order" : order, "current_letter" : None}

    if order == "alphabetical" or order == "random":
        return render_template("game.html")
    else:
        return abort(404)

@socket.on("get_next_question")
def get_next_question(order, current_letter):

    socket.emit("next_question", game.get_next_question(order, current_letter), to=request.sid)

@socket.on("check_selection")
def check_selection(selection, order, current_letter):

    correct = game.check_answer(selection, current_letter)

    if correct:
        socket.emit("correct", to=request.sid)
    else:
        socket.emit("incorrect", to=request.sid)
