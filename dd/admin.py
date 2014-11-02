from flask import g, Blueprint, current_app, render_template, redirect, request, url_for, jsonify, flash
from flask.ext.login import current_user, login_required, login_user, logout_user

from forms import SigninForm, BioForm
from models import db, User, Intro, Bio


admin = Blueprint('admin', __name__, template_folder='templates')


@admin.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        try:
            intro = Intro()
            intro.text = request.form['intro']
            db.session.add(intro)
            db.session.commit()
        except Exception as e:
            current_app.logger.error(str(e))
            flash('There was an error saving the intro', 'error')
    return render_template(
        'admin/home.html', user=current_user,
        users=User.query.all(),
        intro=Intro.query.order_by(Intro.date.desc()).first())



@admin.route('/users/', methods=['POST'])
@login_required
def add_user():
    data = request.json
    if not all(data.values()):
        return jsonify(error='Missing field: username, email or password'), 400
    u = User.query.filter_by(username=data['username']).first()
    if u is not None:
        return jsonify(error='That username is already taken'), 400
    u = User()
    u.username = data['username']
    u.email = data['email']
    u.set_password(data['password'])
    try:
        db.session.add(u)
        db.session.commit()
        return jsonify(user=u.as_json()), 201
    except Exception as e:
        current_app.logger.error(str(e))
        return jsonify(error='There was a database error, check the logs'), 500


@admin.route('/users/<int:uid>/', methods=['POST'])
@login_required
def update_user(uid):
    data = request.json
    if not all([data.get('username', None), data.get('email', None)]):
        return jsonify(error='Missing field: username or email'), 400
    u = User.query.filter_by(username=data['username']).first()
    if u is not None and u.id != uid:
        return jsonify(error='That username is already taken'), 400
    u = User.query.get(uid)
    if not u.is_editable():
        return jsonify(error='You cannot edit this user'), 400
    u.username = data['username']
    u.email = data['email']
    if 'password' in data and data['password'] and data['password'] != '********':
        u.set_password(data['password'])
    try:
        db.session.add(u)
        db.session.commit()
        return jsonify(user=u.as_json())
    except Exception as e:
        current_app.logger.error(str(e))
        return jsonify(error='There was a database error, check the logs'), 500


@admin.route('/users/<int:uid>/delete/', methods=['POST'])
@login_required
def delete_user(uid):
    data = request.json
    if not data.get('username', None):
        return jsonify(error='Missing field: username'), 400
    u = User.query.get(uid)
    if not u.is_deletable():
        return jsonify(error='You cannot delete this user'), 400
    if data['username'] != u.username:
        return jsonify(error='Confirm the delete by providing the username'), 400
    try:
        db.session.delete(u)
        db.session.commit()
        return jsonify(message='Deleted')
    except Exception as e:
        current_app.logger.error(str(e))
        return jsonify(error='There was a database error, check the logs'), 500


@admin.route('/bio/')
@login_required
def bio():
    return render_template(
        'admin/bio.html', user=current_user,
        bios=[BioForm(None, obj=b) for b in Bio.query.all()],
        form=BioForm())


@admin.route('/bio/create/', methods=['POST'])
@login_required
def bio_create():
    form = BioForm()
    if form.validate_on_submit():
        b = Bio()
        del form.bid
        form.populate_obj(b)
        db.session.add(b)
        db.session.commit()
    else:
        print form.errors
        flash('There was an error saving the bio, sorry', 'error')
    return redirect(url_for('.bio'))


@admin.route('/bio/update/<int:bid>/', methods=['POST'])
@login_required
def bio_update(bid):
    form = BioForm()
    if form.validate_on_submit():
        b = Bio.query.get(bid)
        form.populate_obj(b)
        db.session.add(b)
        db.session.commit()
    else:
        print form.errors
        flash('There was an error saving the bio, sorry', 'error')
    return redirect(url_for('.bio'))


@admin.route('/music/')
@login_required
def music():
    return render_template('base.html', user=current_user)


@admin.route('/gigs/')
@login_required
def gigs():
    return render_template('base.html', user=current_user)


@admin.route('/signin/', methods=['GET', 'POST'])
def signin():
    if current_user is not None and current_user.is_authenticated():
        return redirect(url_for('.home'))
    form = SigninForm()
    if form.validate_on_submit():
        u = User.query.filter(User.username == form.username.data).first()
        if u is not None and u.check_password(form.password.data):
            login_user(u)
            return redirect(request.args.get('next') or url_for('.home'))
        form.username.errors.append('Username or password not recognised')
    return render_template('admin/signin.html', form=form)


@admin.route("/signout/")
@login_required
def signout():
    logout_user()
    return redirect(url_for('public.home'))
