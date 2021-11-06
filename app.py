from flask.templating import render_template
from models import RegistrationControls
from alembic import op
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from models import db
import os


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = os.environ['FLASK_SECRET']
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URI_UPDATED']

    migrate = Migrate(app, db)
    db.init_app(app)
    migrate.init_app(app, db)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @app.errorhandler(404)
    def page_not_found(e):
        # note that we set the 404 status explicitly
        return render_template('404.html'), 404

    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app
