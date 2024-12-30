from flask import Blueprint, jsonify, request
from app.extensions import db
from app.models import Task, Sprint

task_bp = Blueprint('task', __name__, url_prefix='/tasks')

@task_bp.route('/', methods=['GET'])
def get_all_tasks():
    tasks=Task.query.all()
    tasks_list=[
        {
            "id": t.id,
            "title": t.title,
            "description": t.description,
            "status": t.status,
            "sprint_id": t.sprint_id
        }
        for t in tasks
    ]
    return jsonify(tasks_list), 200

@task_bp.route('/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task=Task.query.get_or_404(task_id)
    task_dict={
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "status": task.status,
        "sprint_id": task.sprint_id
    }
    return jsonify(task_dict), 200

@task_bp.route('/', methods=['POST'])
def create_task():
    data = request.get_json()

    valid_statuses = ["To Do", "In Progress", "Done"]
    if "status" in data and data["status"] not in valid_statuses:
        return jsonify({"error": "Invalid status"}), 400

    if not data or "title" not in data or "sprint_id" not in data:
        return jsonify({"error": "Missing required parameter"}), 400

    sprint = Sprint.query.get(data["sprint_id"])
    if not sprint:
        return jsonify({"error": "Invalid sprint_id"}), 400

    new_task = Task(
        title=data["title"],
        description=data.get("description", ""),
        status=data.get("status", "To Do"),
        sprint_id=data["sprint_id"]
    )
    db.session.add(new_task)
    db.session.commit()

    return jsonify({
        "message": "Task created successfully",
        "task": {
            "id": new_task.id,
            "title": new_task.title,
            "description": new_task.description,
            "status": new_task.status,
            "sprint_id": new_task.sprint_id
        }
    }), 201



@task_bp.route('/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task =Task.query.get_or_404(task_id)
    data = request.get_json()

    valid_statuses = ["To Do", "In Progress", "Done"]
    if "status" in data and data["status"] not in valid_statuses:
        return jsonify({"error": "Invalid status"}), 400

    if not data:
        return jsonify({"error": "No data provided"}), 400

    if "title" in data and "description" in data:
        task.title = data["title"]
    if "status" in data:
        task.status = data["status"]
    if "description" in data:
        task.description = data["description"]
    if "sprint_id" in data:
        task.sprint_id = data["sprint_id"]

    db.session.commit()
    return jsonify({
        "message": "Task updated successfully",
        "task": {
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "status": task.status,
            "sprint_id": task.sprint_id
        }
    }), 200

@task_bp.route('/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task =Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task deleted successfully"}), 200

