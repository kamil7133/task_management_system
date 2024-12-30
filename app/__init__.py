from flask import Flask
from config import Config
from .extensions import db, migrate
from app.models import Project, Sprint, Task
from flask_sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes.project_routes import project_bp
    app.register_blueprint(project_bp)

    from .routes.sprint_routes import sprint_bp
    app.register_blueprint(sprint_bp)

    from .routes.task_routes import task_bp
    app.register_blueprint(task_bp)

    return app

