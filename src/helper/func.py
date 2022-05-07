import os

from flask_login import LoginManager
from dotenv import load_dotenv
load_dotenv()


def init_app(app):
    app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY", "RANDOM")
    app.config['JSON_AS_ASCII'] = False
    login_manager = LoginManager()
    login_manager.init_app(app)
    return login_manager
