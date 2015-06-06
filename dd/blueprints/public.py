import datetime

from flask import Blueprint, render_template

from dd.models import Intro, Bio, Gig

public = Blueprint('public', __name__, template_folder='templates')


@public.route('/')
def home():
    intro = Intro.query.order_by(Intro.date.desc()).first()
    return render_template('home.html', intro=intro)


@public.route('/bio/')
def bio():
    return render_template('bio.html', bios=Bio.query.all())


@public.route('/music/')
def music():
    return render_template('base.html')


@public.route('/gigs/')
def gigs():
    gigs = Gig.query.all()
    gigs = filter(lambda g: not g.hide, gigs)
    today = datetime.datetime.now()
    past = filter(lambda g: g.when < today, gigs)
    upcoming = filter(lambda g: g.when >= today, gigs)
    return render_template('gigs.html', past=past, upcoming=upcoming)
