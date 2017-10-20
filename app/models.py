from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager,db


class User(UserMixin,db.Model):
    __tablename__='tb_user'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(128))
    passwd_hash = db.Column(db.String(128))
    email = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self,passwd):
        self.passwd_hash = generate_password_hash(passwd)

    def verify_password(self,passwd):
        return check_password_hash(self.passwd_hash,passwd)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))