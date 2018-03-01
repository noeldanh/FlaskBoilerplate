from flask import render_template, flash, redirect, url_for, request, g, \
    jsonify, current_app
from flask_login import current_user, login_required
from app import db
from app.models import User, Book, Post
from app.main import bp
from app.main.forms import PostForm

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/home')
@login_required
def home():
    form = PostForm()
    books = Post.query.all()
    return render_template('home.html', form=form, books=books)
