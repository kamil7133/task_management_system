from flask import Blueprint, jsonify, request, Response
from app.extensions import db
from app.models import Sprint
from datetime import date
import csv
from io import StringIO

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

@sprint_bp.route('/<int:sprint_id>', methods=["GET"])
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
    data = request.get_json()

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

@sprint_bp.route('/<int:sprint_id>/velocity', methods=['GET'])
def get_sprint_velocity(sprint_id):
    sprint = Sprint.query.get_or_404(sprint_id)

    done_tasks = [t for t in sprint.tasks if t.status == "Done"]
    velocity = len(done_tasks)

    return jsonify({
        "sprint_id": sprint.id,
        "sprint_name": sprint.name,
        "velocity": velocity
    }), 200


@sprint_bp.route("/<int:project_id>/time-remaining", methods=['GET'])
def get_time_remaining(sprint_id):
    sprint = Sprint.query.get_or_404(project_id)
    if sprint.end_date is None:
        return jsonify({"message": "Missing 'end_date'"}), 400

    today = date.today()
    if today > sprint.end_date:
        days_left = 0
    else:
        days_left = (sprint.end_date - today).days

    return jsonify({
        "sprint_id": sprint.id,
        "days_left": days_left
    }), 200


@sprint_bp.route("/<int:project_id>/sprints_csv", methods=["GET"])
def export_sprints_csv(project_id):
    project = Project.query.get_or_404(project_id)

    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(["Sprint ID", "Sprint Name", "Start Date", "End Date", "Tasks Count"])

    for sprint in project.sprints:
        task_count = len(sprint.tasks)
        writer.writerow([
            sprint.id,
            sprint.name,
            sprint.start_date,
            sprint.end_date,
            task_count
        ])

    output.seek(0)
    return Response(
        output,
        mimetype="text/csv",
        headers={
            "Content-disposition": f"attachment; filename=project_{project_id}_sprints.csv"
        }
    )