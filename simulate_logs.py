import requests

log = {
 "service": "payment-api",
 "severity": "ERROR",
 "message": "database timeout"
}

requests.post("http://127.0.0.1:8000/logs", json=log)