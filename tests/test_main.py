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

    assert response.status_code == 200, f"Expected 200, received {response.status_code}. Response: {response.text}"
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
    
    assert response.status_code == 422, f"Expected 422, received {response.status_code}. Response: {response.text}"
    
    

# Get /logs return 200 status code and check list of data return correctly
def test_get_log(db_session):
    response = client.get("/logs")
    assert response.status_code == 200, f"Expected 200, received {response.status_code}. Response: {response.text}"
    data = response.json()

    # Verify if the data returns the correct structure 
    assert isinstance(data, list)
    #Verify if the data exists and checks the strctute of the item in the list
    if len(data) > 0:
        assert "service" in data[0]
        assert "severity" in data[0]
        assert "message" in data[0]

#Get  /logs check limit
def test_get_limit_check(db_session):
    response = client.get("/logs", params={"limit": 0})
    assert len(response.json()) == 0


