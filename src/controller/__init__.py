from flask_mail import Mail
from flask_jwt_extended import JWTManager
from authlib.integrations.flask_client import OAuth

import os
my_mail = Mail()
jwt_manager = JWTManager()
oauth = OAuth()


def init_app(app):
    my_mail.init_app(app)
    jwt_manager.init_app(app)
    oauth.init_app(app)
