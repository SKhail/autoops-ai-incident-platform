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

    assert response.status_code == 200
    data = response.json()
    assert data["service"] == "payment-api"
    assert data["severity"] == "ERROR"
    assert data["message"] == "database timeout"




# # Post/Logs reject inbalid payload types or missing fields 







# # GET/logs return stored logs successfully 
# # def test_get(async_client: AsyncClient):
# #     body = "Test Post"
    
# #     response = async_client.get(
# #         "/logs", 
# #         json={"body: body",
# #      })
   
# #     assert response.status_code == 200  
# #     assert response.json() == {"message": "success"}




