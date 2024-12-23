from flask import Flask
from config import Config
from .extensions import db, migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes.project_routes import project_bp
    app.register_blueprint(project_bp)

    return app