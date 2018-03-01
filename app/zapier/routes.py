from flask import render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_user, logout_user, current_user, login_required
from app import create_app, db
from app.zapier import bp
from app.zapier.forms import PostForm
from app.models import Post, User
import json

@bp.route('/zapier', methods=['GET', 'POST'])
# @login_required
# @csrf.exempt
def zapier_home():
    if request.json:
        json_dict = request.get_json()
        emails = json_dict['emails']
        phone = json_dict['phone']
        technician = json_dict['technician']
        u = User.query.get(1)
        new_post = Post(emails=emails, phone=phone, technician=technician, author=u)
        db.session.add(new_post)
        db.session.commit()
        return json.dumps(request.json)
    form = PostForm()
    if form.validate_on_submit():
        # check = Post.query.filter_by(author=form.emails.data).first()
        # if check_author:
        #     print('Author in the system')
        u = User.query.get(1)
        post = Post(emails=form.emails.data, phone=form.phone.data, technician=form.technician.data,
                    author=u)
        # print (current_user)
        db.session.add(post)
        db.session.commit()

        # return jsonify(post)
        return redirect(url_for('main.home'))

    # posts = Post.query.all()
    return render_template('zapier/zapier_home.html', form=form)

@bp.route('/zap', methods=['GET', 'POST'])
@login_required
def zap():
    form = PostForm()
    if not request.json:
        abort(400)
    print (request.json)
    return json.dumps(request.json)
    # data = request.get_json()
    # print (data)
    # emails = request.json['emails']
    # print('wuta')
    # print (emails)
    # phone = request.json['phone']
    # technician = request.json['technician']
    # u = User.query.get(1)
    # new_post = Post(emails=emails, phone=phone, technician=technician, author=current_user)
    # db.session.add(new_post)
    # db.session.commit()

    return render_template('zapier/zapier_home.html', form=form)