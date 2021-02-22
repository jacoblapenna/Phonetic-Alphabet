from phonetic_alphabet_app import app
from flask import render_template, url_for, redirect, abort
from flask_socketio import SocketIO

socket = SocketIO(app)

@app.route('/')
def landing():
    return render_template("landing.html")

@app.route("/quiz/<order>")
def serve_game(order):
    print(order)
    if order == "alphabetical":
        return render_template("game.html")
    if order == "random":
        return render_template("game.html")
    else:
        return abort(404)

@socket.on("start_quiz")
def order_selected(quiz_order):
    print(url_for("serve_game", order=quiz_order))
    return redirect(url_for("serve_game", order=quiz_order))
