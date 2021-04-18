from flask import Flask, request
from .database import db
from .models import Utilisateur
import hashlib


local_database = 'mysql://root:@localhost/challenge_yourself'
global_database = 'mysql://ih1xsuhf3bj02xkl:j14jybwp8pwgx0se@ulsq0qqx999wqz84.chr7pe7iynqr.eu-west-1.rds.amazonaws.com:3306/c4bdcxxeljjwyoh4'


app = Flask(__name__)
app.secret_key = "challenge-^05e77o%aki4ivleu$te@-u7_585y@lcla)9)0__yr+#)u9_&yourself"
app.config['SQLALCHEMY_DATABASE_URI'] = global_database
db.init_app(app)

mdp = hashlib.sha256()


@app.route('/')
def index():
    db.create_all()
    return "Welome to Challenge Yourself API."


@app.route('/users', methods=['GET'])
def get_users():
    utilisateurs = Utilisateur.query.all()
    output = []

    for utilisateur in utilisateurs:
        data = {'id': utilisateur.id, 'pseudo': utilisateur.pseudo, 'mail': utilisateur.mail, 'password': utilisateur.password}
        output.append(data)

    return {"users": output}


@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    utilisateur = Utilisateur.query.get_or_404(id)
    return {'id': utilisateur.id, 'pseudo': utilisateur.pseudo, 'mail': utilisateur.mail, 'password': utilisateur.password}


@app.route('/users', methods=['POST'])
def add_user():
    mdp.update(b"" + request.json['password'].encode())
    utilisateur = Utilisateur(pseudo=request.json['pseudo'], mail=request.json['mail'], password=mdp.hexdigest())
    db.session.add(utilisateur)
    db.session.commit()
    return {'id': utilisateur.id, 'message': 'user created'}


@app.route("/users/<id>", methods=['DELETE'])
def delete_user(id):
    utilisateur = Utilisateur.query.get(id)
    if utilisateur is None:
        return {'id': id, 'message': 'user not found'}

    db.session.delete(utilisateur)
    db.session.commit()
    return {'id': id, 'message': 'user deleted'}


@app.route("/users/<id>", methods=['PUT'])
def update_user(id):
    utilisateur = Utilisateur.query.get(id)
    if utilisateur is None:
        return {'id': id, 'message': 'user not found'}

    if request.json['pseudo'] is not None:
        utilisateur.pseudo = request.json['pseudo']
    if request.json['mail'] is not None:
        utilisateur.mail = request.json['mail']
    if request.json['password'] is not None:
        mdp.update(b"" + request.json['password'].encode())
        utilisateur.password = mdp.hexdigest()

    db.session.commit()

    return {'id': utilisateur.id, 'pseudo': utilisateur.pseudo, 'mail': utilisateur.mail,
            'password': utilisateur.password}


@app.route("/users/test", methods=['GET'])
def test_user():
    utilisateur = Utilisateur.query.filter_by(pseudo="cgraceR").first()
    if utilisateur is None:
        return {'id': id, 'message': 'user not found'}

    utilisateur.pseudo = "cgrace5"
    utilisateur.mail = "cgrace5@monmail.com"
    db.session.commit()

    return {'id': utilisateur.id, 'pseudo': utilisateur.pseudo, 'mail': utilisateur.mail, 'password': utilisateur.password}
