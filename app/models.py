
from . import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Quotes:
    '''Shows how the API will be consumed'''
    def __init__(self, author, quote):
        self.author = author
        self.quote = quote

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    blogs = db.relationship('Blog', backref='user', lazy='dynamic')
    pass_secure = db.Column(db.String(255))
    email = db.Column(db.String(255),unique=True,index=True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def delete_user(self):
        db.session.delete(self)
        db.session.commit()

    @property
    def password(self):
        raise AttributeError('You cannot read the passowrd attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure,password)



    def __repr__(self):
        return f'User {self.username}'

class Blog(UserMixin,db.Model):
    __tablename__ = 'blogs'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    post = db.Column(db.Text())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    category = db.Column(db.String(255), index=True)
    time = db.Column(db.DateTime, default = datetime.utcnow)
    comment = db.relationship('Comments', backref='user', lazy='dynamic')

    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    def delete_blog(self):
        db.session.delete(self)
        db.session.commit()

        
    def __repr__(self):
        return f'Blog {self.post}'

class Comments(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key = True)
    comment = db.Column(db.String())
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    blog_id = db.Column(db.Integer,db.ForeignKey('blogs.id'))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    def delete_comment(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_comments(cls, blog_id):
        '''
        Takes in blo and retrieves all comments for that blog
        '''
        comments = Comments.query.filter_by(blog_id = blog_id).all()
        return comments

    def __repr__(self):
        return f'User {self.name}'
