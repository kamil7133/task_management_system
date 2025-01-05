from flask import Flask
from config import Config
from app.extensions import db, migrate
from app.models import Project, Sprint, Task
from flask_sqlalchemy import SQLAlchemy
from app import create_app
wgi = create_app()

if __name__ == '__main__':
    wgi.run()

