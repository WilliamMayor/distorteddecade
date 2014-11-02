from flask import Blueprint, current_app, render_template

from models import Intro, Bio

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
    return render_template('base.html')

