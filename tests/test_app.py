from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_activities():
    # Arrange & Act
    response = client.get("/activities")
    
    # Assert
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_signup_and_duplicate():
    # Arrange
    activity = "Chess Club"
    email = "new_student@mergington.edu"
    
    # Act: Sign up first time
    res1 = client.post(f"/activities/{activity}/signup?email={email}")
    assert res1.status_code == 200
    
    # Act: Duplicate signup
    res2 = client.post(f"/activities/{activity}/signup?email={email}")
    
    # Assert
    assert res2.status_code == 400