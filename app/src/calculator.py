class Calculator:
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