
# Task Management System

## Overview
The **Task Management System** is a web-based application built to facilitate effective project and task management by leveraging Scrum methodologies. This system provides essential tools for managing projects, sprints, and tasks while enabling seamless visualization through an interactive Kanban board. Designed with scalability and modularity in mind, it ensures ease of use for individuals and teams alike.

This project demonstrates advanced concepts in **backend development**, **frontend integration**, and **database design**, highlighting the ability to create production-grade systems with robust testing and reporting capabilities.

---

## Key Features
1. **Project Management**:
   - Full CRUD functionality for creating, editing, and managing projects.
   - Dynamic association of projects with multiple sprints for efficient tracking.

2. **Sprint Management**:
   - Sprint lifecycle management, including start and end dates.
   - Velocity tracking to measure sprint progress using task completion metrics.
   - Export sprint data to **CSV** for analytics and reporting.

3. **Task Management**:
   - CRUD operations for managing tasks across sprints.
   - Support for task prioritization and status updates ("To Do", "In Progress", "Done").
   - Drag-and-drop functionality for easy task movement on the Kanban board.

4. **Interactive Kanban Board**:
   - User-friendly visualization of tasks categorized by their statuses.
   - Real-time task updates with dynamic frontend integration.

5. **Database Integration**:
   - Powered by **SQLite**, ensuring data persistence and efficient querying.
   - Designed using normalized schemas for projects, sprints, and tasks.

6. **RESTful API**:
   - A structured API to enable seamless integration with external systems or extensions.
   - Detailed routes for projects, sprints, and tasks.

7. **Comprehensive Testing**:
   - Unit tests to validate functionality and ensure system reliability.
   - Test cases covering API endpoints, database models, and edge cases.

8. **Reports and Analytics**:
   - Generate sprint reports (e.g., velocity metrics) on demand.
   - Export data to CSV for further analysis or business intelligence tools.

---

## Project Structure

```
task_management_system/
├── app/
│   ├── routes/               # API endpoints for projects, sprints, and tasks
│   ├── static/               # Static files (CSS)
│   ├── templates/            # HTML templates for rendering pages
│   ├── extensions.py         # Database and migration extensions
│   ├── models.py             # Database models
│   └── utils.py              # Utility functions
├── instance/
│   └── mydatabase.db         # SQLite database
├── migrations/               # Database migration files (managed by Alembic)
├── tests/                    # Unit tests for the application
├── manage.py                 # Command-line utility for running tasks
├── Procfile                  # Deployment configuration
├── requirements.txt          # Python dependencies
└── wsgi.py                   # WSGI entry point for deployment
```

---

## Technical Stack

### Backend:
- **Flask**: Lightweight web framework for building RESTful APIs.
- **Flask-SQLAlchemy**: Object-relational mapper (ORM) for database operations.
- **Flask-Migrate**: Database migrations and schema management.

### Frontend:
- **HTML/CSS**: Responsive design for the user interface.
- **JavaScript**: Dynamic task rendering and drag-and-drop functionality on the Kanban board.

### Database:
- **SQLite**: Lightweight relational database for development and testing.

### Tools and Libraries:
- **Alembic**: Database migration management.
- **Pytest**: Unit testing framework.
- **CSV**: Exporting reports for analysis.

---

## Deployment
The project is deployed as a proof of concept and can be accessed at:
[Task Management System Kanban Board](https://task-management-system-cdtw.onrender.com/projects/kanban)

---

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- Virtual environment (optional but recommended)

### Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/<your-username>/task_management_system.git
   cd task_management_system
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database**:
   ```bash
   flask db upgrade
   ```

5. **Run the Application**:
   ```bash
   flask run
   ```

6. **Access the Application**:
   Open your browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

## API Documentation

### Endpoints
1. **Projects**:
   - `GET /projects/`: Retrieve all projects.
   - `POST /projects/`: Create a new project.
   - `PUT /projects/<project_id>`: Update project details.
   - `DELETE /projects/<project_id>`: Delete a project.

2. **Sprints**:
   - `GET /sprints/`: Retrieve all sprints.
   - `POST /sprints/`: Create a new sprint.
   - `GET /sprints/<sprint_id>/velocity`: Retrieve sprint velocity.
   - `GET /sprints/csv`: Export sprint data to CSV.

3. **Tasks**:
   - `GET /tasks/`: Retrieve all tasks.
   - `POST /tasks/`: Create a new task.
   - `PUT /tasks/<task_id>`: Update a task.
   - `DELETE /tasks/<task_id>`: Delete a task.

---

## Future Enhancements
- **Authentication**:
  - Add user authentication and role-based access control (RBAC).
  - Multi-user support for collaboration.

- **Advanced Reporting**:
  - Integrate data visualization tools for advanced analytics.
  - Real-time metrics dashboards.

- **Deployment**:
  - Containerize the application using Docker.
  - Deploy using Kubernetes for scalability.

- **Scalability**:
  - Switch to PostgreSQL for production environments.
  - Implement caching mechanisms to optimize performance.

---

## Author
Developed with passion and precision by **Kamil Piwowarczyk**.  
For inquiries, reach out via [LinkedIn](https://www.linkedin.com/in/kamil-piwowarczyk-6ba839322/).

---

## License
This project is open-source and licensed under the MIT License. Feel free to fork, modify, and use it for personal or commercial purposes.
