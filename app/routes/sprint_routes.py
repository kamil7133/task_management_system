from flask import Blueprint, jsonify, request, Response
from app.extensions import db
from app.models import Sprint
from datetime import datetime, date
import csv
from io import StringIO

sprint_bp = Blueprint("sprint", __name__, url_prefix="/sprints")
DATE_FORMAT = "%Y-%m-%d"

@sprint_bp.route("/", methods=["GET"])
def get_all_sprints():
    sprints = Sprint.query.all()
    sprints_list = []
    for s in sprints:
        sprints_list.append({
            "id": s.id,
            "name": s.name,
            "start_date": s.start_date.isoformat() if s.start_date else None,
            "end_date": s.end_date.isoformat() if s.end_date else None,
            "project_id": s.project_id
        })
    return jsonify(sprints_list), 200

@sprint_bp.route("/<int:sprint_id>", methods=["GET"])
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

@sprint_bp.route("/", methods=["POST"])
def create_sprint():
    data = request.get_json()
    if "name" not in data or "project_id" not in data:
        return jsonify({"error": "Missing 'name' or 'project_id'"}), 400
    start_date = None
    if "start_date" in data:
        try:
            start_date = datetime.strptime(data["start_date"], DATE_FORMAT).date()
        except ValueError:
            return jsonify({"error": "Invalid 'start_date' format (YYYY-MM-DD)"}), 400
    end_date = None
    if "end_date" in data:
        try:
            end_date = datetime.strptime(data["end_date"], DATE_FORMAT).date()
        except ValueError:
            return jsonify({"error": "Invalid 'end_date' format (YYYY-MM-DD)"}), 400
    new_sprint = Sprint(
        name=data["name"],
        project_id=data["project_id"],
        start_date=start_date,
        end_date=end_date
    )
    db.session.add(new_sprint)
    db.session.commit()
    return jsonify({
        "message": "Sprint created successfully",
        "sprint": {
            "id": new_sprint.id,
            "name": new_sprint.name,
            "start_date": new_sprint.start_date.isoformat() if new_sprint.start_date else None,
            "end_date": new_sprint.end_date.isoformat() if new_sprint.end_date else None,
            "project_id": new_sprint.project_id
        }
    }), 201

@sprint_bp.route("/<int:sprint_id>", methods=["PUT"])
def update_sprint(sprint_id):
    sprint = Sprint.query.get_or_404(sprint_id)
    data = request.get_json()
    if "name" in data:
        sprint.name = data["name"]
    if "project_id" in data:
        sprint.project_id = data["project_id"]
    if "start_date" in data:
        try:
            sprint.start_date = datetime.strptime(data["start_date"], DATE_FORMAT).date()
        except ValueError:
            return jsonify({"error": "Invalid 'start_date' format (YYYY-MM-DD)"}), 400
    if "end_date" in data:
        try:
            sprint.end_date = datetime.strptime(data["end_date"], DATE_FORMAT).date()
        except ValueError:
            return jsonify({"error": "Invalid 'end_date' format (YYYY-MM-DD)"}), 400
    db.session.commit()
    return jsonify({
        "message": "Sprint updated successfully",
        "sprint": {
            "id": sprint.id,
            "name": sprint.name,
            "start_date": sprint.start_date.isoformat() if sprint.start_date else None,
            "end_date": sprint.end_date.isoformat() if sprint.end_date else None,
            "project_id": sprint.project_id
        }
    }), 200

@sprint_bp.route("/<int:sprint_id>", methods=["DELETE"])
def delete_sprint(sprint_id):
    sprint = Sprint.query.get_or_404(sprint_id)
    db.session.delete(sprint)
    db.session.commit()
    return jsonify({"message": "Sprint deleted successfully"}), 200

@sprint_bp.route("/<int:sprint_id>/tasks", methods=["GET"])
def get_sprint_by_tasks(sprint_id):
    sprint = Sprint.query.get_or_404(sprint_id)
    tasks = sprint.tasks
    tasks_list = []
    for t in tasks:
        tasks_list.append({
            "id": t.id,
            "title": t.title,
            "description": t.description,
            "status": t.status,
            "sprint_id": t.sprint_id
        })
    return jsonify(tasks_list), 200

@sprint_bp.route("/<int:sprint_id>/velocity", methods=["GET"])
def get_sprint_velocity(sprint_id):
    sprint = Sprint.query.get_or_404(sprint_id)
    done_tasks = [t for t in sprint.tasks if t.status == "Done"]
    velocity = len(done_tasks)
    return jsonify({
        "sprint_id": sprint.id,
        "sprint_name": sprint.name,
        "velocity": velocity
    }), 200

@sprint_bp.route("/csv", methods=["GET"])
def export_sprints_csv():
    sprints = Sprint.query.all()
    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(["Sprint ID", "Name", "Start Date", "End Date", "Number of Tasks"])
    for s in sprints:
        task_count = len(s.tasks)
        writer.writerow([
            s.id,
            s.name,
            s.start_date.isoformat() if s.start_date else "",
            s.end_date.isoformat() if s.end_date else "",
            task_count
        ])
    output.seek(0)
    return Response(
        output,
        mimetype="text/csv",
        headers={
            "Content-disposition": "attachment; filename=sprints.csv"
        }
    )