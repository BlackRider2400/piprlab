def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise TypeError
    return a * b


def divide(a, b):
    return a / b
