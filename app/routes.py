from werkzeug.wrappers import Response
from app import app
from flask import render_template, request, json, redirect, flash
from app import db
from app.models import User, Bunny, Vote
from app.forms import RegisterForm, LoginForm


@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('index.html', index=True)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if request.form.get('email') == 'test@example.com':
            flash('You have successfully logged in!', 'success')
            return redirect('/home')
        else:
            flash('Sorry, something went wrong', 'danger')
    return render_template("login.html", title='Login', form=form, login=True)


bunnies_data = [{
    "id": "sexy-bunny-19",
    "name": "John Carrotson",
    "bio": "A hopper and a chopper for anything hoppening.",
    "score": "6.5/10",
    "origin": "New York"
}, {
    "id": "i-like-carrots",
    "name": "Lolita Bunny",
    "bio": "Likes hanging out at the carrot stand at the mall.",
    "score": "8.5/10",
    "origin": "Washington"
}, {
    "id": "c4rr07 4r3al",
    "name": "Anonymous",
    "bio": "Can burrow into any network patch.",
    "score": "??/??",
    "origin": "Dark Web"
}, {
    "id": "fluffy",
    "name": "Fluffy McFluffer",
    "bio": "The fluffliest fluff to ever be fluffed.",
    "score": "9.5/10",
    "origin": "Mexico"
}, {
    "id": "bugs",
    "name": "Bugs Bunny",
    "bio": "Always causes bugs and breaks production.",
    "score": "3/10",
    "origin": "Burrow End"
}]


@app.route("/bunnies", methods=['GET'])
def bunnies():
    # print(bunnies_data[0])
    return render_template("bunnies.html", data=bunnies_data, bunnies=True)


@app.route("/vote", methods=['POST', 'GET'])
def vote():
    bunny = {
        'id': request.form['id'],
        'name': request.form['name'],
        'upvote': request.form['upvote'],
        'bio': request.form['bio']
    }

    return render_template("vote.html", bunny=bunny, bunnies=True)


@app.route("/carrots")
def carrots():
    carrots_data = [{
        "carrot_id": "trump-carrot",
        "name": "34 carat carrot",
        "description": "Carrot made of solid gold.",
        "taste": "0/10",
        "texture": "1/10"
    }, {
        "carrot_id": "le-old-mcdonald",
        "name": "Old Yi Faithful Carrot",
        "description": "For the senior hoppers' choppers.",
        "taste": "3/10",
        "texture": "7/10"
    }, {
        "carrot_id": "standard",
        "name": "Free Range Carrots",
        "description": "Organically grown, fresh picked, free-range carrots.",
        "taste": "8/10",
        "texture": "9/10"
    }]

    # print(carrots_data[0])
    return render_template("carrots.html", data=carrots_data, carrots=True)


@app.route("/register")
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if request.form.get('email') == 'test@example.com':
            flash('You have successfully logged in!', 'success')
            return redirect('/home')
        else:
            flash('Sorry, something went wrong', 'danger')
    return render_template("register.html", title='New Bunny Lover Registration', form=form, register=True)


@app.route('/api/', methods=['GET'])
@app.route('/api/<id>', methods=['GET'])
def api(id=None):
    data = bunnies_data
    for idx, obj in enumerate(bunnies_data):
        if (obj['id'] == id):
            data = bunnies_data[idx]
    return Response(json.dumps(data), mimetype='application/json')


@app.route('/user')
def user():
    return render_template('user.html', users=User.objects.all())
