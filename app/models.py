from app import db
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

#tabela de usuários

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique = True)
    password = db.Column(db.String(120))
    posts = db.relationship("Post", backref="author", lazy="dynamic")
    def __repr__(self):
        return "<User {}>".format(self.username)


#tabela de posts
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.Integer, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)

db.create_all()
db.session.commit()
