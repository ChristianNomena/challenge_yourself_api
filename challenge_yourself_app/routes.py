from flask import Flask, request
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


"""@app.route('/users/add')
def insert_user():
    mdp.update(b"mon mot de passe")

    user1 = Utilisateur(pseudo="cgrace5", mail="cgrace5@monmail.com", password=mdp.hexdigest())
    db.session.add(user1)
    db.session.commit()

    mdp.update(b"mon nouveau mot de passe")

    user2 = Utilisateur(pseudo="jeanclaude", mail="jeanclaude@monmail.com", password=mdp.hexdigest())
    db.session.add(user2)
    db.session.commit()

    return "User Created"


@app.route("/users/delete/<id>")
def delete_user(id):
    # user = Utilisateur.query.filter_by(id=id).first()
    utilisateur = Utilisateur.query.get_or_404(id)
    db.session.delete(utilisateur)
    db.session.commit()
    return "User deleted with id {}".format(id)
"""