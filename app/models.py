from flask import Blueprint, request, jsonify
from app.extensions import db

project_bp = Blueprint('project', __name__, url_prefix='/projects')

class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

