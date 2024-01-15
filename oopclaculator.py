class Calculator:
    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y

    def mult(self, x, y):
        return x * y

    def div(self, x, y):
        if y != 0:
            return x / y
        else:
            return "Cannot divide by zero"

calc = Calculator()

result_add = calc.add(5, 3)
print("Addition:", result_add)

result_subtract = calc.sub(8, 3)
print("Subtraction:", result_subtract)

result_multiply = calc.mult(4, 6)
print("Multiplication:", result_multiply)

result_divide = calc.div(10, 2)
print("Division:", result_divide)
