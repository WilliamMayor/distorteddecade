from flask import g, Blueprint, current_app, render_template, redirect, request, url_for
from flask.ext.login import current_user, login_required, login_user, logout_user

from forms import SigninForm
from models import User


admin = Blueprint('admin', __name__, template_folder='templates')


@admin.route('/')
@login_required
def home():
    return render_template('home.html', user=current_user)


@admin.route('/bio/')
@login_required
def bio():
    return render_template('home.html', user=current_user)


@admin.route('/music/')
@login_required
def music():
    return render_template('home.html', user=current_user)


@admin.route('/gigs/')
@login_required
def gigs():
    return render_template('home.html', user=current_user)


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
