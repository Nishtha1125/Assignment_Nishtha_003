from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_create_student():
    response = client.post(
        "/students",
        json={
            "id": 100,
            "name": "Test Student",
            "age": 21,
            "course": "BCA",
            "email": "teststudent@gmail.com"
        }
    )

    assert response.status_code == 201
    assert response.json()["name"] == "Test Student"


def test_get_all_students():
    response = client.get("/students")

    assert response.status_code == 200


def test_get_student_by_id():
    response = client.get("/students/100")

    assert response.status_code == 200
    assert response.json()["id"] == 100


def test_update_student():
    response = client.put(
        "/students/100",
        json={
            "id": 100,
            "name": "Updated Student",
            "age": 22,
            "course": "BSC",
            "email": "updated@gmail.com"
        }
    )

    assert response.status_code == 200
    assert response.json()["name"] == "Updated Student"


def test_delete_student():
    response = client.delete("/students/100")

    assert response.status_code == 200