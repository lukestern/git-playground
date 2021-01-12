import sys

parameters = [p for p in sys.argv if 'calculator.py' not in p]

if parameters[0] not in ['/', 'x', '+', '-']:
    raise ValueError("First argument must be an operation:\n Divde: '/'\n Multiply: 'x'(or '*')\n Add:'+'\n Subtract '-'")

for n, i in enumerate(parameters[1:]):
    parameters[n + 1] = int(i)

def Calc(op, a, b):
    if op == '/':
        result = a / b
        return result
    elif op == 'x' or op == '*':
        result = a * b
        return result
    elif op == '+':
        result = a + b
        return result
    elif op == '-':
        result = a - b
        return result

assert Calc('/', 5, 2) == 2.5
assert Calc('x', 10, 5) == 50
assert Calc('*', 10, 5) == 50
assert Calc('*', 0, 5) == 0
assert Calc('+', 1, 2) == 3
assert Calc('-', 10, 5) == 5

print(Calc(parameters[0], parameters[1], parameters[2]))
