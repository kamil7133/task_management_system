def test_create_project(test_client):
    response = test_client.post("/projects/", json={
        "name": "Test Project",
        "description": "A project for testing"
    })
    assert response.status_code == 201

    data = response.get_json()
    assert data["project"]["name"] == "Test Project"

def test_get_all_projects(test_client):
    test_client.post("/projects/", json={
        "name": "Project A",
        "description": "Desc A"
    })
    response = test_client.get("/projects/")
    assert response.status_code == 200

    data = response.get_json()
    assert len(data) == 1
    assert data[0]["name"] == "Project A"
