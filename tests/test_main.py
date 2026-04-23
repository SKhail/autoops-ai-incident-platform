import pytest
from httpx import AsyncClient 



# test get request is working when getting the data
# def test_get():
#     response = client.get("/logs")
#     # check if reponse is successful
#     assert response.status_code == 200
#     assert response.json() == {"message": "success"}




# What behaviour i am proving?
# GET/logs return stored logs successfully 
# POST/LOGs accepts valid payload and returns 200/201
# Post/Logs reject inbalid payload types or missing fields 