#This is a better calc than the one we made earlier.

num1 = float(input('Enter the first number: ')) #Here instead of the int function we used the float
#function to enable us to operate with decimals
op = input('Enter an operator: ')
num2 = float(input('Enter the second number: '))
if op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
elif op == '*':
    print(num1 * num2)
elif op == '/':
    print(num1 / num2)
else:
    print('Invalid operator')