from flask import Flask
from config import Config
from app.extensions import db, migrate
from app.models import Project, Sprint, Task
from flask_sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from .app.routes.project_routes import project_bp
    app.register_blueprint(project_bp)

    from .app.routes.sprint_routes import sprint_bp
    app.register_blueprint(sprint_bp)

    from .app.routes.task_routes import task_bp
    app.register_blueprint(task_bp)



app = create_app()

if __name__ == '__main__':
    app.run()

