from flask import render_template, url_for, redirect, abort
from flask_socketio import SocketIO

from phonetic_alphabet_app import app
from phonetic_alphabet_app.Game import Game

socket = SocketIO(app)

@app.route('/')
def landing():
    return render_template("landing.html")

@app.route("/quiz/<order>")
def serve_game(order):

    global game

    if order == "alphabetical":
        game = Game(random_bool=False)
        return render_template("game.html")
    if order == "random":
        game = Game(random_bool=True)
        return render_template("game.html")
    else:
        return abort(404)

@socket.on("start_quiz")
def order_selected(quiz_order):
    socket.emit("redirect", {"url" : url_for("serve_game", order=quiz_order)})

@socket.on("get_present_question")
def server_present_question():

    letter = game.get_letter()
    choices = game.get_choices()

    socket.emit("next_question", {"letter" : letter, "choices" : choices})

@socket.on("get_next_question")
def get_next_question():

    game.get_next_letter()
    letter = game.get_letter()
    choices = game.get_choices()

    socket.emit("next_question", {"letter" : letter, "choices" : choices})

@socket.on("check_selection")
def check_selection(selection):

    correct = game.check_answer(selection)

    if correct:
        socket.emit("correct")
        """
        This and load game should just deliver the next question.
        Does the letter exist for all clients (how does each client get it's own game state)
        """
    else:
        socket.emit("incorrect")
