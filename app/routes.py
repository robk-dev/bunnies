from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('index.html', login=True)

@app.route("/login")
def login():
    return render_template("login.html", login=False)

@app.route("/bunnies")
def bunnies():
    return render_template("bunnies.html", login=False)

@app.route("/carrots")
def carrots():
    return render_template("carrots.html", login=False)

@app.route("/register")
def register():
    return render_template("register.html", login=False)