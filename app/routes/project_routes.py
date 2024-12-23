from flask import Blueprint, jsonify, request
from app import db
from app.models import Project

project_bp = Blueprint('project_bp', __name__, url_prefix='/projects')

@project_bp.route('/', methods=['GET'])
def get_all_projects():
    pass

@project_bp.route('/<int:project_id>', methods=['GET'])
def get_project(project_id):
    pass

@project_bp.route('/', methods=['POST'])
def create_project():
    pass

@project_bp.route('/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    pass

@project_bp.route('/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    pass

