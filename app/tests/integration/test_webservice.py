import requests
import pytest
from src.calculator import Calculator
from src.sqrt_provider import SQRTProvider

def test_webservice_sqrt():
    calc = Calculator(SQRTProvider())
    assert calc.sqrt(4.0) == 2.0

def test_webservice_sqrt_negative():
    calc = Calculator(SQRTProvider())
    with pytest.raises(Exception):
        calc.sqrt(-1.0)

def test_webservice_health_check():
    url = "http://host.docker.internal:5001/health"
    response = requests.get(url)
    
    assert response.status_code == 200
    assert response.json() == {"status": "up"}
