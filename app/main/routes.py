from flask import render_template, flash, redirect, url_for, request, g, \
    jsonify, current_app
from flask_login import current_user, login_required
from app import db
from app.models import User
from app.main import bp

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/home')
@login_required
def home():
    return render_template('home.html')
