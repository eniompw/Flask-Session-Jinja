from flask import Flask, render_template, session, redirect
from os import urandom

app = Flask(__name__)
app.secret_key = urandom(16)

@app.route("/")
def home():
    if session.get('username'):
        return render_template("index.html", user=session['username'])
    else:
        return render_template("index.html", user="None")

@app.route("/login")
def login():
    session['username'] = "Bob"
    return redirect("/")

@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect("/")
