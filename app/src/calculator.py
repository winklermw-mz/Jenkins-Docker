from src.sqrt_provider import SQRTProvider

class Calculator:
    sqrt_provider: SQRTProvider

    def __init__(self, sqrt_provider: SQRTProvider) -> None:
        self.sqrt_provider = sqrt_provider

    def add(self, a: float, b: float) -> float:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both parameters must be of type float or int")
        return float(a + b)
    
    def sub(self, a: float, b: float) -> float:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both parameters must be of type float or int")
        return float(a - b)
    
    def mult(self, a: float, b: float) -> float:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both parameters must be of type float or int")
        return float(a * b)
    
    def div(self, a: float, b: float) -> float:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both parameters must be of type float or int")
        if b == 0:
            raise TypeError("Second parameter must not be zero")
        return float(a / b)
    
    def sqrt(self, a: float) -> float:
        try:
            value = float(a)
        except ValueError:
            raise Exception("Invalid number")

        if value < 0:
            raise Exception("Negative numbers are not allowed")

        return self.sqrt_provider.run(a)
