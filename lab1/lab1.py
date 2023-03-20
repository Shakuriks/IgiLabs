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


def get_even_numbers(numbers):
    even_numbers = []

    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)

    return even_numbers


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = get_even_numbers(numbers)

print(result)