import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.config.from_object('config.Config')
    app.jinja_options.setdefault('extensions', []).append('jinja2_base64_filters.Base64Filters')

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # register the database
    db.init_app(app)

    # register the cli
    from parsons import cli
    cli.init_app(app)

    # apply the blueprints to the app
    from parsons import puzzle
    app.register_blueprint(puzzle.bp)

    # make url_for('index') == url_for('puzzle.index')
    # in another app, you might define a separate main index here with
    # app.route, while giving the puzzle blueprint a url_prefix, but for
    # the tutorial the puzzle will be the main index
    app.add_url_rule('/', endpoint='index')

    return app
