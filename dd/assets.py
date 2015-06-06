from flask.ext.assets import Environment, Bundle
from webassets.filter import register_filter
from webassets_libsass import LibSass

register_filter(LibSass)

assets = Environment()

css = Bundle(
    'css/main.scss',
    filters='libsass,cssmin',
    output='main.min.css',
    depends=['css/*.scss', 'css/*/*.scss'])
assets.register('css', css)

js = Bundle(
    'js/vendor/jquery-1.11.3.min.js',
    'js/vendor/underscore-min.js',
    Bundle(
        'js/dd.js',
        'js/admin/home.js',
        'js/admin/bio.js',
        'js/admin/gigs.js',
        filters='rjsmin'),
    output='main.min.js')
assets.register('js', js)
