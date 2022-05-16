from . import db


class Quotes:
    '''Shows how the API will be consumed'''
    def __init__(self, author, quote):
        self.author = author
        self.quote = quote

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    blogs = db.relationship('Blog', backref='user', lazy='dynamic')


    def __repr__(self):
        return f'User {self.username}'

class Blog(db.Model):
    __tablename__ = 'blogs'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    post = db.Column(db.Text())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

