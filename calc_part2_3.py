f = open('Workshop1_ex1_part2_input.txt', 'r')
lines = f.read().splitlines()

def CheckAndCalculate(input):
    parameters = input.split(' ')
    if parameters[0] == 'calc':
        CheckCalcParameters(parameters[1:])
        print(Calc(parameters[1], parameters[2], parameters[3]))

def CheckCalcParameters(parameters):
    if parameters[0] not in ['/', 'x', '+', '-', '%']:
         raise ValueError("First argument must be an operation:\n Divde: '/'\n Multiply: 'x'(or '*')\n Add:'+'\n Subtract '-'\n Modulo: '^'")

def Calc(op, a, b):
    a = int(a)
    b = int(b)
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
    elif op == '%':
        result = a % b
        return result

for line in lines:
    CheckAndCalculate(line)
