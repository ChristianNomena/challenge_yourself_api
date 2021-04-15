from .database import db


class Utilisateur(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pseudo = db.Column(db.String(50), unique=True, nullable=False)
    mail = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(240), nullable=False)

    classements = db.relationship("Classement", back_populates="utilisateur")
    photos = db.relationship("Photo", back_populates="utilisateur")
    effectuers = db.relationship("Effectuer", back_populates="utilisateur")
    aimers = db.relationship("Aimer", back_populates="utilisateur")

    def __init__(self, pseudo, mail, password):
        self.pseudo = pseudo
        self.mail = mail
        self.password = password


class Defi(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    contexte = db.Column(db.Text, nullable=False)
    type = db.Column(db.Integer, nullable=False)
    date_debut = db.Column(db.DateTime, nullable=False)
    date_fin = db.Column(db.DateTime, nullable=False)
    id_categorie = db.Column(db.Integer, db.ForeignKey("categorie.id"))

    classements = db.relationship("Classement", back_populates="defi")
    photos = db.relationship("Photo", back_populates="defi")
    effectuers = db.relationship("Effectuer", back_populates="defi")

    categorie = db.relationship("Categorie", back_populates="defis")

    def __init__(self, contexte, type, date_debut, date_fin, id_categorie):
        self.contexte = contexte
        self.type = type
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.id_categorie = id_categorie


class Categorie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50), unique=True, nullable=False)

    defis = db.relationship("Defi", back_populates="categorie")

    def __init__(self, nom):
        self.nom = nom


class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    likes = db.Column(db.Integer, nullable=True)
    path = db.Column(db.String(220), unique=True, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    id_utilisateur = db.Column(db.Integer, db.ForeignKey("utilisateur.id"))
    id_defi = db.Column(db.Integer, db.ForeignKey("defi.id"))

    aimers = db.relationship("Aimer", back_populates="photo")

    utilisateur = db.relationship("Utilisateur", back_populates="photos")
    defi = db.relationship("Defi", back_populates="photos")

    def __init__(self, likes, path, date, id_utilisateur, id_defi):
        self.likes = likes
        self.path = path
        self.date = date
        self.id_utilisateur = id_utilisateur
        self.id_defi = id_defi


class Classement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rang = db.Column(db.Integer, nullable=True)
    id_defi = db.Column(db.Integer, db.ForeignKey("defi.id"))
    id_utilisateur = db.Column(db.Integer, db.ForeignKey("utilisateur.id"))

    utilisateur = db.relationship("Utilisateur", back_populates="classements")
    defi = db.relationship("Defi", back_populates="classements")

    def __init__(self, rang, id_defi, id_utilisateur):
        self.rang = rang
        self.id_defi = id_defi
        self.id_utilisateur = id_utilisateur


class Effectuer(db.Model):
    id_utilisateur = db.Column(db.Integer, db.ForeignKey("utilisateur.id"), primary_key=True)
    id_defi = db.Column(db.Integer, db.ForeignKey("defi.id"), primary_key=True)

    utilisateur = db.relationship("Utilisateur", back_populates="effectuers")
    defi = db.relationship("Defi", back_populates="effectuers")

    def __init__(self, id_utilisateur, id_defi):
        self.id_utilisateur = id_utilisateur
        self.id_defi = id_defi


class Aimer(db.Model):
    id_photo = db.Column(db.Integer, db.ForeignKey("photo.id"), primary_key=True)
    id_utilisateur = db.Column(db.Integer, db.ForeignKey("utilisateur.id"), primary_key=True)

    utilisateur = db.relationship("Utilisateur", back_populates="aimers")
    photo = db.relationship("Photo", back_populates="aimers")

    def __init__(self, id_photo, id_utilisateur):
        self.id_photo = id_photo
        self.id_utilisateur = id_utilisateur


# db.create_all()
