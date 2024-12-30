def test_create_task(test_client):
    project_resp = test_client.post("/projects/", json={
        "name": "Task Project",
        "description": "For tasks test"
    })
    project_id = project_resp.get_json()["project"]["id"]

    sprint_resp = test_client.post("/sprints/", json={
        "name": "Sprint for tasks",
        "project_id": project_id
    })
    sprint_id = sprint_resp.get_json()["sprint"]["id"]

    task_resp = test_client.post("/tasks/", json={
        "title": "Write Tests",
        "description": "Add more coverage",
        "status": "To Do",
        "sprint_id": sprint_id
    })
    assert task_resp.status_code == 201
    task_data = task_resp.get_json()
    assert task_data["task"]["title"] == "Write Tests"
    assert task_data["task"]["status"] == "To Do"

def test_get_tasks(test_client):
    project_resp = test_client.post("/projects/", json={
        "name": "Task Project B",
        "description": "For tasks test"
    })
    project_id = project_resp.get_json()["project"]["id"]

    sprint_resp = test_client.post("/sprints/", json={
        "name": "Sprint for tasks B",
        "project_id": project_id
    })
    sprint_id = sprint_resp.get_json()["sprint"]["id"]

    test_client.post("/tasks/", json={
        "title": "Task #1",
        "sprint_id": sprint_id
    })
    test_client.post("/tasks/", json={
        "title": "Task #2",
        "sprint_id": sprint_id
    })

    tasks_resp = test_client.get("/tasks/")
    assert tasks_resp.status_code == 200
    tasks_data = tasks_resp.get_json()
    assert len(tasks_data) == 2

def test_update_task(test_client):
    project_resp = test_client.post("/projects/", json={
        "name": "Update Task Project",
        "description": "Testing update on tasks"
    })
    project_id = project_resp.get_json()["project"]["id"]

    sprint_resp = test_client.post("/sprints/", json={
        "name": "Sprint for update tasks",
        "project_id": project_id
    })
    sprint_id = sprint_resp.get_json()["sprint"]["id"]

    task_resp = test_client.post("/tasks/", json={
        "title": "Task to update",
        "status": "To Do",
        "sprint_id": sprint_id
    })
    task_id = task_resp.get_json()["task"]["id"]

    update_resp = test_client.put(f"/tasks/{task_id}", json={
        "status": "In Progress"
    })
    assert update_resp.status_code == 200

    get_resp = test_client.get(f"/tasks/{task_id}")
    task_data = get_resp.get_json()
    assert task_data["status"] == "In Progress"

def test_delete_task(test_client):
    project_resp = test_client.post("/projects/", json={
        "name": "Delete Task Project",
        "description": "Testing deletion of tasks"
    })
    project_id = project_resp.get_json()["project"]["id"]

    sprint_resp = test_client.post("/sprints/", json={
        "name": "Sprint for delete tasks",
        "project_id": project_id
    })
    sprint_id = sprint_resp.get_json()["sprint"]["id"]

    task_resp = test_client.post("/tasks/", json={
        "title": "Task to delete",
        "status": "To Do",
        "sprint_id": sprint_id
    })
    task_id = task_resp.get_json()["task"]["id"]

    delete_resp = test_client.delete(f"/tasks/{task_id}")
    assert delete_resp.status_code == 200

    get_resp = test_client.get(f"/tasks/{task_id}")
    assert get_resp.status_code == 404
