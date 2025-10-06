

def add_numbers(a, b):
    return a + b
def subtract_numbers(a, b):
    return a - b
def multiply_numbers(a, b):
    return a * b
def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: You can't divide by zero"
    except Exception as e:
        return f"Error: {str(e)}"
print(add_numbers(10,60)) #returns the output 70
print(subtract_numbers(90,40)) #returns 50
print(multiply_numbers(30,7)) #output 210
print(divide_numbers('a' ,10)) #Error: unsupported operand type(s) for /: 'str' and 'int'
# a string cannot be divided by an integer
