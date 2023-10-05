def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}


def calculator():
    want_to_continue = 'y'
    num1 = float(input("What's the first number: "))
    while want_to_continue == 'y':
        for op in operations:
            print(op)
        operator = input("Chose an operation: ")
        num2 = float(input("What's the next number: "))
        result = ((operations[operator])(num1, num2))
        print(f"{num1} {operator} {num2} = {result}")
        print(result)
        want_to_continue = (input(
            f"To continue calculation with {result} type 'y'\nto start new calculation type 'n'\nto exit type 'e'\n ")).lower()
        if want_to_continue == 'y':
            num1 = result
        elif want_to_continue == 'n':
            calculator()
        elif want_to_continue == 'e':
            break


calculator()
