# zadanie 1
def getPowerTo3(x):
    return x ** 3


# zadanie 2
def getPolynomial(x, a, b, c):
    return a * x * x + b * x + c


# zadanie 3
def getTimeForTask(name, number, time):
    time = time / 1000
    time = round(time, 3)
    return f"{name} wykonał(a) zadanie nr {number} w {time}s."


# zadanie 4
def getSymetric(a, b):
    c = (a[0] + b[0]) / 2
    d = (a[1] + b[1]) / 2
    return c, d


# zadanie 5
def getBinary(x):
    return len(str(bin(x))) - 2


# zadanie 6
def getAverageFromTuples(x):
    count = 0
    sumation = 0
    for i in x:
        sumation = sumation + i
        count = count + 1
    
    minimal = min(x)
    maximal = max(x)

    average = sumation / count

    return f"Range: < {minimal}; {maximal}> Average: {average}"


# zadanie 7
def showDimensions(width, height, lenght):
    width = round(width, 3)
    height = round(height, 3)
    lenght = round(lenght, 3)
    width = str(width)
    height = str(height)
    lenght = str(lenght)
    column_size = max(len(width), len(height), len(lenght), len("Wartość")) + 1
    text = f"""
    Wymiar    |{formatRow("Wartość", column_size)}
    -----------{"-" * column_size}
    Szerokość |{formatRow(width, column_size)}
    Wysokość  |{formatRow(height, column_size)}
    Długość   |{formatRow(lenght, column_size)}
    """
    return text


def formatRow(a, size):
    return (size - len(a)) * " " + str(a)


# zadanie 8
def getSquareEquation(a, b, c):
    delta = b*b - 4 * a * c
    if delta > 0:
        x1 = (-b - delta**0.5) / (2 * a)
        x2 = (-b + delta**0.5) / (2 * a)
        return x1, x2
    elif delta == 0:
        return -b / (2 * a)


print("---------------------------------")
print("Zadanie 1:\n")
print(getPowerTo3(0))
print(getPowerTo3(1))
print(getPowerTo3(-3))
print(getPowerTo3(2e3))
print("---------------------------------")

print("Zadanie 2:\n")
print(getPolynomial(2, 1, 2, 1))
print("---------------------------------")

print("Zadanie 3:\n")
print(getTimeForTask("Adam", 1, 553467))
print("---------------------------------")

print("Zadanie 4:\n")
print(getSymetric((5, 6), (8, 7)))
print("---------------------------------")

print("Zadanie 5:\n")
print(getBinary(10))
print("---------------------------------")

print("Zadanie 6:\n")
print(getAverageFromTuples((3, -2)))
print("---------------------------------")

print("Zadanie 7:\n")
print(showDimensions(2434.4070, 989.350, 077.202))
print("---------------------------------")

print("Zadanie 8:\n")
print(getSquareEquation(2, -4, 2))
print("---------------------------------")
