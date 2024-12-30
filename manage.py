from app import create_app, db
from app.models import Project, Sprint, Task
from datetime import date
from flask import current_app

app = create_app()

@app.cli.command("seed-data")
def seed_data():
    with app.app_context():
        if Project.query.count() == 0:
            example_project = Project(name="Sample Project with Dates", description="Proof of Concept w/ dates")
            db.session.add(example_project)
            db.session.commit()

            sprint_with_dates = Sprint(
                name="Sprint with Dates",
                project_id=example_project.id,
                start_date=date(2024, 11, 10),
                end_date=date(2024, 11, 20),
            )
            db.session.add(sprint_with_dates)
            db.session.commit()

            task1 = Task(title="Task A", description="To do", status="To Do", sprint_id=sprint_with_dates.id)
            task2 = Task(title="Task B", description="In progress", status="In Progress", sprint_id=sprint_with_dates.id)
            task3 = Task(title="Task C", description="Done", status="Done", sprint_id=sprint_with_dates.id)
            db.session.add_all([task1, task2, task3])
            db.session.commit()

            print("seeded data")
        else:
            print("error seeding data")