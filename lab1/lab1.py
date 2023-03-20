print("Hello, world!")

def calculate(x, y, operation):
    if operation == 'add':
        return x + y
    elif operation == 'sub':
        return x - y
    elif operation == 'mult':
        return x * y
    elif operation == 'div':
        if y == 0:
            print("division by zero is impossible")
        else:
            return x / y