from flask import Blueprint, jsonify, request
from app.extensions import db
from app.models import Sprint

from Studia.Algorytmy_i_struktury_danych.Wielkanoc.Wielkanoc import data

sprint_bp = Blueprint('sprint', __name__, url_prefix='/sprints')

@sprint_bp.route('/', methods=['GET'])
def get_all_sprints():
    sprints = Sprint.query.all()
    sprints_list = [
        {
            "id": s.id,
            "name": s.name,
            "start date": s.start_date.isoformat() if s.start_date else None,
            "end_date": s.end_date.isoformat() if s.end_date else None,
            "project_id": s.project_id
        }
        for s in sprints
    ]
    return jsonify(sprints_list), 200

@sprint_bp.route('/<int:sprint_id', methods=["GET"])
def get_sprint(sprint_id):
    sprint = Sprint.query.get_or_404(sprint_id)
    sprint_dict = {
        "id": sprint.id,
        "name": sprint.name,
        "start_date": sprint.start_date.isoformat() if sprint.start_date else None,
        "end_date": sprint.end_date.isoformat() if sprint.end_date else None,
        "project_id": sprint.project_id
    }
    return jsonify(sprint_dict), 200

@sprint_bp.route('/', methods=['POST'])
def create_sprint():
    if "name" not in data or "project_id" not in data:
        return jsonify({"error": "Missing 'name or 'project_id'"}), 400

    start_date = data.get("start_date")
    end_date = data.get("end_date")

    new_sprint = Sprint(
        name=data["name"],
        project_id=data["project_id"],
        start_date=start_date,
        end_date=end_date,
    )

    db.session.add(new_sprint)
    db.session.commit()

    return jsonify({
        "message": "Sprint created successfully",
        "sprint": {
            "id": new_sprint.id,
            "name": new_sprint.name,
            "project_id": new_sprint.project_id,
        }
    }), 201

@sprint_bp.route('/<int:sprint_id>', methods=['PUT'])
def update_sprint(sprint_id):
    sprint = Sprint.query.get_or_404(sprint_id)
    data = request.get_json()

    if "name" in data:
        sprint.name = data["name"]
    if "project_id" in data:
        sprint.project_id = data["project_id"]
    if "start_date" in data:
        sprint.start_date = data["start_date"]
    if "end_date" in data:
        sprint.end_date = data["end_date"]

    db.session.commit()

    return jsonify({
        "message": "Sprint updated successfully",
        "sprint": {
            "id": sprint.id,
            "name": sprint.name,
            "project_id": sprint.project_id,
            "start_date": sprint.start_date,
            "end_date": sprint.end_date,
        }
    }), 200

@sprint_bp.route('/<int:sprint_id>', methods=['DELETE'])
def delete_sprint(sprint_id):
    sprint = Sprint.query.get_or_404(sprint_id)
    db.session.delete(sprint)
    db.session.commit()
    return jsonify({"message": "Sprint deleted successfully"}), 200

@sprint_bp.route('/<int:sprint_id>/tasks', methods=['GET'])
def get_sprint_by_tasks(sprint_id):
    sprint = Sprint.query.get_or_404(sprint_id)
    tasks = sprint.tasks

    tasks_list = [
        {
            "id": tasks.id,
            "title": tasks.title,
            "description": tasks.description,
            "status": tasks.status,
            "sprint_id": tasks.sprint_id,
        }
        for tasks in tasks
    ]
    return jsonify(tasks_list), 200