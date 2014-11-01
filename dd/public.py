from flask import Blueprint, current_app, render_template

public = Blueprint('public', __name__, template_folder='templates')


@public.route('/')
def home():
    return render_template('home.html')


@public.route('/bio/')
def bio():
    return render_template('home.html')


@public.route('/music/')
def music():
    return render_template('home.html')


@public.route('/gigs/')
def gigs():
    return render_template('home.html')

