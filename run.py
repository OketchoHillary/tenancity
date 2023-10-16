from flask import Flask

from models.auth import User
from models.core import Business, Property

from utils import migrate, db

from apps.auth.routes import auth_bp
from apps.core.routes import core_bp

def create_app():
    myapp = Flask(__name__)
    myapp.config.from_object('config.DevelopmentConfig')
    myapp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    myapp.register_blueprint(core_bp)
    myapp.register_blueprint(auth_bp, url_prefix='/accounts')
    db.init_app(myapp)
    migrate.init_app(myapp, db)

    return myapp


app = create_app()

if __name__ == '__main__':
    app.run()
