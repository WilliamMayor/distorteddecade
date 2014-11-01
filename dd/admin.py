from flask import Blueprint, current_app, render_template

admin = Blueprint('admin', __name__, template_folder='templates')


@admin.route('/')
def home():
    return render_template('home.html')

@admin.route('/bio/')
def bio():
    return render_template('home.html')


@admin.route('/music/')
def music():
    return render_template('home.html')


@admin.route('/gigs/')
def gigs():
    return render_template('home.html')