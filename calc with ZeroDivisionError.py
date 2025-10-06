
num1 = float(input('Enter the first number: '))
op = input('Enter the operator: (+, -, *, /): ')
num2 = float(input('Enter the second number: '))
if op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
elif op == '*':
    print(num1 * num2)
elif op == '/':
    if num2 != 0: # this checks if the 2nd no is 0 or not since we can't divide a number by zero
        print(num1 / num2)
    else:
        print('ZeroDivisionError')
else:
    print('Invalid operator')
