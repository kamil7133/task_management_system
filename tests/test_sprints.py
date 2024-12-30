def test_create_sprint(test_client):
    project_resp = test_client.post("/projects/", json={
        "name": "Test Project",
        "description": "For sprint testing"
    })
    project_data = project_resp.get_json()
    project_id = project_data["project"]["id"]

    sprint_resp = test_client.post("/sprints/", json={
        "name": "Sprint 1",
        "project_id": project_id
    })
    assert sprint_resp.status_code == 201
    sprint_data = sprint_resp.get_json()
    assert sprint_data["sprint"]["name"] == "Sprint 1"

def test_get_sprints(test_client):
    project_resp = test_client.post("/projects/", json={
        "name": "Test Project 2",
        "description": "For sprint testing"
    })
    project_id = project_resp.get_json()["project"]["id"]

    sprint_resp = test_client.post("/sprints/", json={
        "name": "Sprint A",
        "project_id": project_id
    })

    all_sprints = test_client.get("/sprints/")
    assert all_sprints.status_code == 200
    sprints_data = all_sprints.get_json()
    assert len(sprints_data) == 1
    assert sprints_data[0]["name"] == "Sprint A"

def test_update_sprint(test_client):
    project_resp = test_client.post("/projects/", json={
        "name": "Test Project 3",
        "description": "For update test"
    })
    project_id = project_resp.get_json()["project"]["id"]

    sprint_resp = test_client.post("/sprints/", json={
        "name": "Sprint B",
        "project_id": project_id
    })
    sprint_id = sprint_resp.get_json()["sprint"]["id"]

    update_resp = test_client.put(f"/sprints/{sprint_id}", json={
        "name": "Sprint B - Updated"
    })
    assert update_resp.status_code == 200

    get_resp = test_client.get(f"/sprints/{sprint_id}")
    sprint_data = get_resp.get_json()
    assert sprint_data["name"] == "Sprint B - Updated"

def test_delete_sprint(test_client):
    project_resp = test_client.post("/projects/", json={
        "name": "Delete Project",
        "description": "For delete test"
    })
    project_id = project_resp.get_json()["project"]["id"]

    sprint_resp = test_client.post("/sprints/", json={
        "name": "Sprint to Delete",
        "project_id": project_id
    })
    sprint_id = sprint_resp.get_json()["sprint"]["id"]

    delete_resp = test_client.delete(f"/sprints/{sprint_id}")
    assert delete_resp.status_code == 200

    get_resp = test_client.get(f"/sprints/{sprint_id}")
    assert get_resp.status_code == 404
