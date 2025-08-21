from app import db, login_manager
from datetime import datetime
from flask_login import UserMixin
#from flask_sqlalchemy import SQLAlchemy

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    nome=db.Column(db.String, nullable=True)
    sobrenome=db.Column(db.String, nullable=True)
    email=db.Column(db.String, nullable=True)
    senha=db.Column(db.String,nullable=True)

class Contato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.DateTime, default=datetime.now())
    nome = db.Column(db.String, nullable=True)
    email = db.Column(db.String, nullable=True)
    assunto = db.Column(db.String, nullable=True)
    mensagem = db.Column(db.String, nullable=True)
    respondido = db.Column(db.Integer, default=0)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_criação = db.Column(db.DateTime, default=datetime.now())
    mensagem = db.Column(db.String, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=True)
