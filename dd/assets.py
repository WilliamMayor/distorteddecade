from flask.ext.assets import Environment, Bundle

assets = Environment()

css = Bundle(
    'css/main.scss',
    filters='scss,cssmin',
    output='main.min.css',
    depends='css/*.scss')
assets.register('css', css)

js = Bundle(
    'js/vendor/underscore-min.js',
    Bundle(
        'js/rollbar.js',
        filters='rjsmin'),
    output='main.min.js')
assets.register('js', js)
