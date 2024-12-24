import pylab as p
from flask import Blueprint, jsonify, request
from app import db
from app.models import Project

project_bp = Blueprint('project_bp', __name__, url_prefix='/projects')

@project_bp.route('/', methods=['GET'])
def get_all_projects():
    projects = Project.query.all()
    projects_list = [
        {
            "id": p.id,
            "name": p.name,
            "description": p.description
        }
        for p in projects
    ]
    return jsonify(projects_list), 200

@project_bp.route('/<int:project_id>', methods=['GET'])
def get_project(project_id):
    project = Project.query.get_or_404(project_id)
    return jsonify({
        "id": project.id,
        "name": project.name,
        "description": project.description
    }), 200

@project_bp.route('/', methods=['POST'])
def create_project():
    data = request.get_json()
    new_project = Project(
        name=data.get('name'),
        description=data.get('description')
    )
    db.session.add(new_project)
    db.session.commit()
    return jsonify({
        "message": "Project created successfully",
        "id": new_project.id
    }), 201

@project_bp.route('/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    project = Project.query.get_or_404(project_id)
    data = request.get_json()
    project.name = data.get('name', project.name)
    project.description = data.get('description', project.description)
    db.session.commit()
    return jsonify({
        "message": "Project updated successfully"
    }), 200

@project_bp.route('/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    project = Project.query.get_or_404(project_id)
    db.session.delete(project)
    db.session.commit()
    return jsonify({
        "message": "Project deleted successfully"
    }), 200

@project_bp.route('/<int:project_id>/sprints', methods=['GET'])
def get_sprints_by_project(project_id):
    project = Project.query.get_or_404(project_id)
    sprints = project.sprints

    sprints_list = []
    for s in sprints:
        sprints_list.append({
            "id": s.id,
            "name": s.name,
            "start_date": s.start_date.isoformat() if s.start_date else None,
            "end_date": s.end_date.isoformat() if s.end_date else None,
            "project_id": s.project_id,
        })
    return jsonify(sprints_list), 200
