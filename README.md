# Task Management System (Scrum/Kanban)

A proof-of-concept web application for managing tasks, sprints, and projects in a Scrum-like environment. Features a Kanban board with drag-and-drop task updates, CRUD operations on projects/sprints/tasks, simple reporting, and CSV export.

---

## Table of Contents
1. [Features](#features)
2. [Tech Stack](#tech-stack)
3. [Project Structure](#project-structure)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Endpoints](#endpoints)
7. [Tests](#tests)
8. [Deployment](#deployment)
9. [License](#license)

---

## Features
- **CRUD** for Projects, Sprints, and Tasks:
  - Each Project has multiple Sprints.
  - Each Sprint has multiple Tasks.
  - Tasks support statuses: *To Do*, *In Progress*, *Done*.
- **Kanban Board**:
  - Drag-and-drop tasks to change status.
  - Automatic refresh of the board after updates.
- **Reports**:
  - Export Sprints to CSV.
  - Simple Velocity calculation (`done_tasks` count in a sprint).
- **Dates in Sprints**:
  - Optional `start_date` and `end_date` for each sprint.
  - Simple calculation of remaining days (`time-remaining` endpoint).
- **Testing**:
  - Comprehensive unit tests (Pytest) for CRUD and functionalities.

---

## Tech Stack
- **Backend**: Python 3, Flask, Flask-SQLAlchemy, Flask-Migrate, Gunicorn
- **Database**: SQLite (local) or PostgreSQL (production if desired)
- **Frontend**: HTML + CSS + JavaScript (minimal; uses Jinja2 templates for layout)
- **Deployment**: Render / Heroku (Gunicorn + Procfile)

---

## Project Structure
```
task_management_system/
├── app/
│   ├── __init__.py           # create_app() + blueprint registrations
│   ├── models.py             # SQLAlchemy models (Project, Sprint, Task)
│   ├── routes/
│   │   ├── project_routes.py # endpoints for projects
│   │   ├── sprint_routes.py  # endpoints for sprints (including CSV export)
│   │   └── task_routes.py    # endpoints for tasks
│   ├── templates/
│   │   ├── base.html         # main layout
│   │   └── kanban.html       # Kanban Board UI
│   └── static/
│       ├── css/             # styles.css
│       └── js/              # (optional JS files)
├── config.py                # Flask config (SQLALCHEMY_DATABASE_URI, SECRET_KEY)
├── manage.py                # create_app() + CLI commands (seed-data)
├── Procfile                 # for Gunicorn on Render/Heroku
├── requirements.txt         # dependencies
├── migrations/             # Flask-Migrate scripts
└── tests/
    ├── test_projects.py
    ├── test_sprints.py
    └── test_tasks.py
```

---

## Installation
1. **Clone** this repository:
   ```bash
   git clone https://github.com/your-username/task_management_system.git
   cd task_management_system
   ```
2. **Create** and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # macOS/Linux
   ```
3. **Install** dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. **Set up** environment variables (optional):
   ```bash
   export FLASK_APP=manage.py
   export FLASK_ENV=development
   export SECRET_KEY="your-secret-key"
   # For production DB: export DATABASE_URL="postgresql://..."
   ```

---

## Usage
1. **Apply migrations**:
   ```bash
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```
2. **Seed** sample data (optional):
   ```bash
   flask seed-data
   ```
3. **Run** the server:
   ```bash
   flask run
   ```
4. Open `http://127.0.0.1:5000/projects/kanban` to view the Kanban board.

---

## Endpoints
- **Projects**:  
  - `GET /projects/` → list projects  
  - `POST /projects/` → create project  
  - `GET /projects/<id>` → retrieve project  
  - `PUT /projects/<id>` → update project  
  - `DELETE /projects/<id>` → delete project  

- **Sprints**:  
  - `GET /sprints/` → list sprints  
  - `POST /sprints/` → create sprint (with optional `start_date`, `end_date`)  
  - `PUT /sprints/<id>` → update sprint  
  - `DELETE /sprints/<id>` → delete sprint  
  - `GET /sprints/csv` → export all sprints to CSV  
  - `GET /sprints/<id>/tasks` → tasks for a sprint  
  - `GET /sprints/<id>/velocity` → velocity (done tasks count)  
  - `GET /sprints/<id>/time-remaining` → days left to `end_date`  

- **Tasks**:  
  - `GET /tasks/` → list tasks  
  - `POST /tasks/` → create task (with status)  
  - `GET /tasks/<id>` → retrieve task  
  - `PUT /tasks/<id>` → update status/description  
  - `DELETE /tasks/<id>` → delete task

---

## Tests
1. **Pytest** is used for unit testing.  
2. Tests are located in the `tests/` folder:
   ```bash
   pytest
   ```
3. Make sure to configure a test database or use SQLite in-memory for isolated testing.

---

## Deployment

### Proof-Of-Concept
You can test my app on this site:



## License
This project is open-source for educational and demonstration purposes.  
Feel free to adapt it as needed.
