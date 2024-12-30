from flask import Blueprint, request, jsonify
from app.extensions import db
from datetime import date
from . import db


project_bp = Blueprint('project', __name__, url_prefix='/projects')

class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

class Sprint(db.Model):
    __tablename__ = 'sprints'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.Date, nullable=True)
    end_date = db.Column(db.Date, nullable=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)

    project = db.relationship("Project", backref="sprints")

class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(50), default="To Do")
    sprint_id = db.Column(db.Integer, db.ForeignKey('sprints.id'), nullable=False)
    sprint = db.relationship('Sprint', backref='tasks')