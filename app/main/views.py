
from flask import render_template, request, redirect, url_for, abort
from app.models import *
from app.requests import get_quote
from . import main
from flask_login import login_required,current_user
from .. import db,photos
from .forms import *

@main.route('/', methods = ['GET','POST'])
def index():
    quote = get_quote()
    blogs = Blog.query.all()
    technology = Blog.query.filter_by(category= 'Technology').all()
    science = Blog.query.filter_by(category= 'Science').all()
    food = Blog.query.filter_by(category='Food').all()
    entertainment = Blog.query.filter_by(category = 'Entertainment').all()
    history = Blog.query.filter_by(category = 'History').all()

    
    return render_template('index.html', quote=quote, technology=technology,
    science=science,food=food,history=history,entertainment=entertainment,
    blogs=blogs)

@main.route('/blog', methods=['POST','GET'])
@login_required
def new_blog():
    form = BlogForm()
    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data
        category = form.category.data
        user_id = current_user
        new_blog_object = Blog(post=post,user_id=current_user._get_current_object().id,category=category,title=title)
        new_blog_object.save_blog()
        return redirect(url_for('main.index'))

    return render_template('blog/blog.html', form=form )

@main.route('/user/<name>')
@login_required
def profile(name):
    user = User.query.filter_by(username = name).first()
    user_id = current_user._get_current_object().id
    posts = Blog.query.filter_by(user_id = user_id).all()
    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user,posts=posts)



@main.route('/comment/<int:blog_id>', methods = ['POST','GET'])
@login_required
def comment(blog_id):
    form = CommentForm()
    blog = Blog.query.get(blog_id)
    all_comments = Comments.query.filter_by(blog_id = blog_id).all()

    if form.validate_on_submit():
        comment = form.comment.data 
        blog_id = blog_id
        user_id = current_user._get_current_object().id
        new_comment = Comments(comment = comment,user_id = user_id,blog_id = blog_id)
        new_comment.save_comment()
        return redirect(url_for('.comment', blog_id = blog_id))

    return render_template('comment.html', form =form, blog = blog,all_comments=all_comments)


@main.route('/user/<name>/updateprofile', methods = ['POST','GET'])
@login_required
def updateprof(name):
    form = UpdateProfile()
    user = User.query.filter_by(username = name).first()
    if user == None:
        abort(404)

    if form.validate_on_submit():
        user.bio = form.bio.data
        user.save_user()
        return redirect(url_for('.profile',name = name))

    return render_template('profile/updateprof.html',form =form)


@main.route('/user/<name>/update/pic',methods= ['POST'])
@login_required
def update_pic(name):
    user = User.query.filter_by(username = name).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',name=name))

@main.route('/blog/<int:blog_id>')
@login_required
def blog(blog_id):
    comments = Comments.query.filter_by(blog_id = blog_id).all()
    heading = 'Comments'
    blog = Blog.query.get_or_404(blog_id)

    title = 'Blogs'
    return render_template('blog/blog.html', title = title, blog = blog, comments = comments, heading = heading)

