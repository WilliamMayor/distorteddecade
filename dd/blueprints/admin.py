from flask import (
    Blueprint, current_app, render_template, redirect, request, url_for, flash)
from flask.ext.login import (
    current_user, login_required, login_user, logout_user)

from dd.forms import (
    SigninForm, IntroForm, UserForm, BioForm, GigForm, EmbedForm)
from dd.models import db, User, Intro, Bio, Gig, Embed

admin = Blueprint('admin', __name__, template_folder='templates')


@admin.route('/')
@login_required
def home():
    return render_template(
        'admin/home.html', user=current_user,
        users=[
            UserForm(None, obj=u)
            for u in User.query.filter(User.username != 'Admin').all()],
        intro=IntroForm(obj=Intro.query.order_by(Intro.date.desc()).first()),
        create=UserForm(None))


@admin.route('/home/intro/', methods=['POST'])
@login_required
def home_intro_create():
    form = IntroForm()
    if form.validate_on_submit():
        try:
            i = Intro()
            form.populate_obj(i)
            db.session.add(i)
            db.session.commit()
            flash('Intro updated!', 'info')
        except Exception as e:
            current_app.logger.error(str(e))
            flash('There was an error saving the intro, sorry', 'error')
    else:
        current_app.logger.error(str(form.errors))
        flash('There was an error with that intro, sorry', 'error')
    return redirect(url_for('.home'))


@admin.route('/users/', methods=['POST'])
@login_required
def users_create():
    form = UserForm()
    if form.validate_on_submit():
        try:
            u = User()
            del form.uid
            form.populate_obj(u)
            u.set_password(form.password.data)
            db.session.add(u)
            db.session.commit()
            flash('User created!', 'info')
        except Exception as e:
            current_app.logger.error(str(e))
            flash('There was an error creating the user, sorry', 'error')
    else:
        current_app.logger.error(str(form.errors))
        flash('There was an error with the new user details, sorry', 'error')
    return redirect(url_for('.home'))


@admin.route('/users/<int:uid>/', methods=['POST'])
@login_required
def users_update(uid):
    u = User.query.get(uid)
    form = UserForm(obj=u)
    if form.validate_on_submit() and u.username != 'Admin':
        try:
            if form.password.data:
                u.set_password(form.password.data)
            del form.password
            form.populate_obj(u)
            db.session.add(u)
            db.session.commit()
            flash('User updated!', 'info')
        except Exception as e:
            current_app.logger.error(str(e))
            flash('There was an error updating the user, sorry', 'error')
    else:
        current_app.logger.error(str(form.errors))
        flash('There was an error with those user details, sorry', 'error')
    return redirect(url_for('.home'))


@admin.route('/users/<int:uid>/delete/', methods=['POST'])
@login_required
def users_delete(uid):
    u = User.query.get(uid)
    form = UserForm(obj=u)
    can_delete = all([
        form.validate_on_submit(),
        form.username.data == u.username,
        u.username != 'Admin'])
    if can_delete:
        try:
            db.session.delete(u)
            db.session.commit()
            flash('User deleted!', 'info')
        except Exception as e:
            current_app.logger.error(str(e))
            flash('There was an error deleting the user, sorry', 'error')
    else:
        current_app.logger.error(str(form.errors))
        flash('There was an error with those user details, sorry', 'error')
    return redirect(url_for('.home'))


@admin.route('/bio/')
@login_required
def bio():
    return render_template(
        'admin/bio.html', user=current_user,
        bios=[
            BioForm(None, obj=b, prefix=str(b.bid))
            for b in Bio.query.all()],
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
        flash('Bio created!', 'info')
    else:
        current_app.logger.error(str(form.errors))
        flash('There was an error saving the bio, sorry', 'error')
    return redirect(url_for('.bio'))


@admin.route('/bio/<int:bid>/update/', methods=['POST'])
@login_required
def bio_update(bid):
    form = BioForm(prefix=str(bid))
    if form.validate_on_submit():
        b = Bio.query.get(bid)
        form.populate_obj(b)
        db.session.add(b)
        db.session.commit()
        flash('Bio updated!', 'info')
    else:
        current_app.logger.error(str(form.errors))
        flash('There was an error saving the bio, sorry', 'error')
    return redirect(url_for('.bio'))


@admin.route('/bio/<int:bid>/delete/', methods=['POST'])
@login_required
def bio_delete(bid):
    b = Bio.query.get(bid)
    form = BioForm(obj=b, prefix=str(bid))
    if form.validate_on_submit() and form.name.data == b.name:
        try:
            db.session.delete(b)
            db.session.commit()
            flash('Bio deleted!', 'info')
        except Exception as e:
            current_app.logger.error(str(e))
            flash('There was an error deleting the bio, sorry', 'error')
    else:
        current_app.logger.error(str(form.errors))
        flash('There was an error with those bio details, sorry', 'error')
    return redirect(url_for('.bio'))


@admin.route('/gigs/')
@login_required
def gigs():
    return render_template(
        'admin/gigs.html', user=current_user,
        gigs=[
            GigForm(None, obj=g, prefix=str(g.gid))
            for g in Gig.query.all()],
        form=GigForm())


@admin.route('/gigs/create/', methods=['POST'])
@login_required
def gigs_create():
    form = GigForm()
    if form.validate_on_submit():
        g = Gig()
        del form.gid
        form.populate_obj(g)
        db.session.add(g)
        db.session.commit()
        flash('Gig created!', 'info')
    else:
        current_app.logger.error(str(form.errors))
        flash('There was an error creating the gig, sorry', 'error')
    return redirect(url_for('.gigs'))


@admin.route('/gigs/<int:gid>/update/', methods=['POST'])
@login_required
def gigs_update(gid):
    form = GigForm(prefix=str(gid))
    if form.validate_on_submit():
        g = Gig.query.get(gid)
        form.populate_obj(g)
        db.session.add(g)
        db.session.commit()
        flash('Gig updated!', 'info')
    else:
        current_app.logger.error(str(form.errors))
        flash('There was an error saving the gig, sorry', 'error')
    return redirect(url_for('.gigs'))


@admin.route('/gigs/<int:gid>/delete/', methods=['POST'])
@login_required
def gigs_delete(gid):
    g = Gig.query.get(gid)
    form = GigForm(obj=g, prefix=str(gid))
    if form.validate_on_submit() and form.name.data == g.name:
        try:
            db.session.delete(g)
            db.session.commit()
            flash('Gig deleted!', 'info')
        except Exception as e:
            current_app.logger.error(str(e))
            flash('There was an error deleting the gig, sorry', 'error')
    else:
        current_app.logger.error(str(form.errors))
        flash('There was an error with those gig details, sorry', 'error')
    return redirect(url_for('.gigs'))


@admin.route('/music/')
@login_required
def music():
    return render_template(
        'admin/music.html', user=current_user,
        embeds=[
            EmbedForm(None, obj=e, prefix=str(e.eid))
            for e in Embed.query.all()],
        form=EmbedForm())


@admin.route('/music/create/', methods=['POST'])
@login_required
def music_create():
    form = EmbedForm()
    if form.validate_on_submit():
        e = Embed()
        del form.eid
        form.populate_obj(e)
        db.session.add(e)
        db.session.commit()
        flash('Embed added!', 'info')
    else:
        current_app.logger.error(str(form.errors))
        flash('There was an error adding the embed, sorry', 'error')
    return redirect(url_for('.music'))


@admin.route('/music/<int:eid>/update/', methods=['POST'])
@login_required
def music_update(eid):
    form = EmbedForm(prefix=str(eid))
    if form.validate_on_submit():
        e = Embed.query.get(eid)
        form.populate_obj(e)
        db.session.add(e)
        db.session.commit()
        flash('Embed updated!', 'info')
    else:
        current_app.logger.error(str(form.errors))
        flash('There was an error saving the embed, sorry', 'error')
    return redirect(url_for('.music'))


@admin.route('/music/<int:eid>/delete/', methods=['POST'])
@login_required
def music_delete(eid):
    e = Embed.query.get(eid)
    form = EmbedForm(obj=e, prefix=str(eid))
    if form.validate_on_submit() and form.name.data == e.name:
        try:
            db.session.delete(e)
            db.session.commit()
            flash('Embed deleted!', 'info')
        except Exception as e:
            current_app.logger.error(str(e))
            flash('There was an error deleting the embed, sorry', 'error')
    else:
        current_app.logger.error(str(form.errors))
        flash('There was an error with those embed details, sorry', 'error')
    return redirect(url_for('.music'))


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
