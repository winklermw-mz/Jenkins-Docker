import requests

BASE_URL = "http://host.docker.internal:5001"

def test_webservice_sqrt():
    response = requests.get(f"{BASE_URL}/sqrt/9.0")
    
    assert response.status_code == 200
    assert response.json() == {"result": 3.0}

def test_webservice_sqrt_negative():
    response = requests.get(f"{BASE_URL}/sqrt/-4.0")
    
    assert response.status_code == 400
    assert response.json()["result"] is None
    assert "error" in response.json()

def test_webservice_health_check():
    url = f"{BASE_URL}/health"
    response = requests.get(url)
    
    assert response.status_code == 200
    assert response.json() == {"status": "up"}