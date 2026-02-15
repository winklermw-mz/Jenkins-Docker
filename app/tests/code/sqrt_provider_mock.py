import math
from src.sqrt_provider import SQRTProvider

class SQRTProviderMock(SQRTProvider):
    def run(self, value: float) -> float:
        return math.sqrt(value)