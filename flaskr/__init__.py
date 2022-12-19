import os

from flask import Flask, render_template
from .me import *

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',                                 
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    @app.route('/')
    def home():
        return render_template('home.html', me=me)
    @app.route('/interests/<interest>')
    def getInterest(interest):
            if interest in me["interestnames"]:
                desc=me[interest]["desc"]
                img=me[interest]["img"]
                return render_template('interests.html', me=me, interest=interest, desc=desc, img=img)
            else:
                return render_template('gloop.html')
    return app
    