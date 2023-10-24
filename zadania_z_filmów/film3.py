# Krzysztof Barałkiewicz
from datetime import datetime


# exercise 1
def fizzBuzz():
    for i in range(1, 100, 1):
        out = ""
        if i % 3 == 0:
            out = out + "fizz"
        if i % 5  == 0:
            out = out + "buzz"
        if out != "":
            print(str(i) + ": " + out)


# exercise 2
def getReversedAndSecondElement(list):
    # list.reverse()
    return list[-2:0:-3]


# exercise 3
def watchFibonacci():
    prevElement = 0
    currentElement = 1
    for i in range(0, 4):
        tempVal = currentElement
        currentElement = prevElement + currentElement
        prevElement = tempVal


# exercise 4
def printRecipie(products):
    if not products:
        return "Empty recipie"

    taxValue = {"A": 12, "B": 8, "E": 22}

    print(datetime.today().date())

    total = 0
    totalTax = 0

    for i in range(0, len(products)):
        total = total + products[i][1]
        totalTax = totalTax + round(products[i][1] * (taxValue.get(products[i][2], 0)) / 100)
        grValue = str(products[i][1])[-2:]
        plnValue = str(products[i][1])[:-2]
        print(f"{i}. {products[i][0]:10} {plnValue:>2}.{grValue:2} {products[i][2]}")


    taxGr = str(totalTax)[-2:]
    taxZl = str(totalTax)[:-2]
    totalGr = str(total)[-2:]
    totalZl = str(total)[:-2]

    endValue = total + totalTax
    endGr = str(endValue)[-2:]
    endZl = str(endValue)[:-2]

    print("-" * 25)
    print(f"TAX {taxZl:>12}.{taxGr}")
    print(f"TOTAL: {totalZl:>9}.{totalGr}")
    print(f"TOTAL+TAX: {endZl:>5}.{endGr}")





fizzBuzz()

print(getReversedAndSecondElement([1, 2, 3, 4, 5, 6, 7, 8, 9]))

watchFibonacci()

products = [
    ["Apples", 1499, "A"],
    ["Milk", 434, "A"],
    ["Chips", 1099, "E"],
    ["Sugar", 699, "B"],
]

print("\n--------------------\n")

print(printRecipie(products))
