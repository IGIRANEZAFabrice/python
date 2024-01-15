class Calc:
    def __init__(self):
       pass
    def add(self, a , b):
        return a+b
    def sub(self, a ,b):
        return a-b
    def mult(self, a ,b):
        return a * b
    def div (self,a,b) :
        if b == 0:
              return a," can not be divided by ",b
        else:
            return a/b
    
calculator = Calc()
a = input(": ")
sign = input(": ")
b = input(": ")
a = int(a)
b = int(b)
if sign == "+":
        answer = calculator.add(a,b) 
elif sign == "-":
        answer = calculator.sub(a,b)
elif sign == "*":
        answer = calculator.mult(a,b)
elif sign == "/":
        answer = calculator.div(a,b)
else:
        print('invalid sign')
print(answer)
