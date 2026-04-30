from fastapi.testclient import TestClient
from main import app 

client = TestClient(app)

# What behaviour i am proving?

# POST/LOGs accepts valid payload and returns 200/201
def test_post_log_success(db_session): 
    response = client.post("/logs", json={
        "service": "payment-api",
        "severity": "ERROR",
        "message":  "database timeout" })
    print(response)

    assert response.status_code == 200, f"Expected 200, received {response.status_code}. Reponse: {response.text}"
    data = response.json()
    assert data["service"] == "payment-api"
    assert data["severity"] == "ERROR"
    assert data["message"] == "database timeout"


# # Post/Logs reject inbalid data
def test_post_log_missing_message(db_session):
    response = client.post("/logs", json={
        "service": "payment-api",
        "severity": "123",
        "message":  "database timeout" })
    
    assert response.status_code == 422, f"Expected 422, received {response.status_code}. Reponse: {response.text}"
    
    

# Get /logs check list returned 



#Get  /logs check limit



