class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

    @staticmethod
    def average(numbers):
        if not numbers:
            raise ValueError("The list of numbers is empty.")
        return sum(numbers) / len(numbers)

    @staticmethod
    def percentage(part, whole):
        if whole == 0:
            raise ValueError("Whole cannot be zero.")
        return (part / whole) * 100