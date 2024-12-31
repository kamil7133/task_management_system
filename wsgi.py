from flask import Flask
from config import Config
from app.extensions import db, migrate
from app.models import Project, Sprint, Task
from flask_sqlalchemy import SQLAlchemy

def create_app():
    wgi = Flask(__name__)
    wgi.config.from_object(Config)

    db.init_app(wgi)
    migrate.init_app(wgi, db)

    from app.routes.project_routes import project_bp
    wgi.register_blueprint(project_bp)

    from app.routes.sprint_routes import sprint_bp
    wgi.register_blueprint(sprint_bp)

    from app.routes.task_routes import task_bp
    wgi.register_blueprint(task_bp)



wgi = create_app()

if __name__ == '__main__':
    wgi.run()

