from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_bcrypt import Bcrypt


from config import Config

jwt = JWTManager()
db = SQLAlchemy()
bcrypt = Bcrypt()

def create_app() -> Flask:
    app:Flask = Flask(__name__)
    app.config.from_object(Config)
    jwt.init_app(app)
    db.init_app(app)
    bcrypt.init_app(app)
    CORS(app)
    from routes import test_bp

    app.register_blueprint(test_bp, url_prefix="/v1")

    return app
