# manage.py
from app import create_app, db
from app.models import Project, Sprint, Task

app = create_app()

@app.cli.command("seed-data")
def seed_data():
    with app.app_context():
        if Project.query.count() == 0:
            example_project = Project(
                name="Sample Project",
                description="Proof of Concept project."
            )
            db.session.add(example_project)
            db.session.commit()

            example_sprint = Sprint(
                name="Sprint 1",
                project_id=example_project.id,
            )
            db.session.add(example_sprint)
            db.session.commit()

            task1 = Task(
                title="Task A",
                description="To do",
                status="To Do",
                sprint_id=example_sprint.id
            )
            task2 = Task(
                title="Task B",
                description="In progress",
                status="In Progress",
                sprint_id=example_sprint.id
            )
            task3 = Task(
                title="Task C",
                description="Done",
                status="Done",
                sprint_id=example_sprint.id
            )
            db.session.add_all([task1, task2, task3])
            db.session.commit()

            print("seeded data")
        else:
            print("error with seeding data")
