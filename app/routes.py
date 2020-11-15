from app import app
from flask import render_template, request


@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('index.html', index=True)


@app.route("/login")
def login():
    return render_template("login.html", login=True)


@app.route("/bunnies", methods=['GET'])
def bunnies():
    bunnies_data = [{
        "bunny_id": "sexy-bunny-19",
        "name": "John Carrotson",
        "bio": "A hopper and a chopper for anything hoppening.",
        "score": "6.5/10",
        "origin": "New York"
    }, {
        "bunny_id": "i-like-carrots",
        "name": "Lolita Bunny",
        "bio": "Likes hanging out at the carrot stand in the mall.",
        "score": "8.5/10",
        "origin": "Washington"
    }, {
        "bunny_id": "c4rr07 4r3al",
        "name": "Anonymous",
        "bio": "Can burrow into any network patch.",
        "score": "??/??",
        "origin": "Dark Web"
    }, {
        "bunny_id": "fluffy",
        "name": "Fluffy McFluffer",
        "bio": "The fluffliest fluff to ever be fluffed.",
        "score": "9.5/10",
        "origin": "Mexico"
    }, {
        "bunny_id": "bugs",
        "name": "Bugs Bunny",
        "bio": "Always causes bugs and breaks production.",
        "score": "3/10",
        "origin": "Burrow End"
    }]

    # print(bunnies_data[0])
    return render_template("bunnies.html", data=bunnies_data, bunnies=True)


@app.route("/bunnies", methods=['POST'])
def voted():
    bunny = {
        'id': request.form['bunny_id'],
        'name': request.form['name'],
        'upvote': request.form['upvote'],
        'bio': request.form['bio']
    }

    return render_template("bunny.html", bunny=bunny, bunnies=True)


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
    return render_template("register.html", login=False, register=True)
