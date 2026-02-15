import requests

class SQRTProvider:
    BASE_URL = "http://host.docker.internal:5001"

    def run(self, value: float) -> float:
        response = requests.get(f"{self.BASE_URL}/sqrt/{value}")
        if response.status_code != 200:
            raise Exception(f"Service returned error code {response.status_code}")
        
        return float(response.json()["result"])