from flask import Flask
from decouple import config as env

from apps.admin.routes import admin_bp
from models.auth import User
from models.core import Business

from utils import migrate, db, login_manager

from apps.auth.routes import auth_bp
from apps.core.routes import core_bp


def create_app():
    myapp = Flask(__name__)
    myapp.config.from_object(env('APP_SETTINGS'))
    myapp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    myapp.register_blueprint(core_bp)
    myapp.register_blueprint(auth_bp, url_prefix='/accounts')
    myapp.register_blueprint(admin_bp, url_prefix='/admin')
    db.init_app(myapp)
    login_manager.init_app(myapp)
    migrate.init_app(myapp, db)

    return myapp


app = create_app()


@login_manager.user_loader
def load_user(user_id):
    # Implement a method to load a user from your data source (e.g., database)
    # For this example, we'll just return a User object with the given user_id
    return User(user_id)


if __name__ == '__main__':
    app.run()
