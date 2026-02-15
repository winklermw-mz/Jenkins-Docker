import math

class SquareRoot:
    def run(self, value: float) -> float:
        try:
            value = float(value)
        except ValueError:
            raise Exception("Invalid number")

        if value < 0:
            raise Exception("Negative numbers are not allowed")
        
        return math.sqrt(value)