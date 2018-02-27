from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user, login_required
from app import create_app, db
from app.book import bp
from app.models import User, Book
from app.book.forms import BookForm

@bp.route('/add', methods=['GET', 'POST'])
def add_book():
    form = BookForm()
    if form.validate_on_submit():
        check_author = Book.query.filter_by(author=form.author.data).first()
        if check_author:
            print ('Author in the system')
        book = Book(title=form.title.data, author=form.author.data, review=form.review.data, rating=form.rating.data, mybooks=current_user)
        # print (book.mybooks)
        db.session.add(book)
        db.session.commit()
    return render_template('book/add_book.html', form=form)
