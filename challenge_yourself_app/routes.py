from flask import Flask
from .database import db
from .models import Utilisateur
import hashlib


app = Flask(__name__)
app.secret_key = "challenge-^05e77o%aki4ivleu$te@-u7_585y@lcla)9)0__yr+#)u9_&yourself"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/challenge_yourself'
db.init_app(app)

mdp = hashlib.sha256()


@app.route('/')
def index():
    db.create_all()
    return "hello"


@app.route('/users')
def get_users():
    user = Utilisateur.query.all()
    return {"users": user[-1].pseudo}


@app.route('/users/add')
def set_user():
    mdp.update(b"mon nouveau mot de passe")
    user2 = Utilisateur(pseudo="jeanclaude", mail="jeanclaude@monmail.com", password=mdp.hexdigest())
    db.session.add(user2)
    db.session.commit()

    return "User Created"
