from random import randint

data = [
    ["Tomek B", ["Paulina", "Krzysztof", "Julia"]],
    ["Paulina", ["Tomek B", "Krzysztof", "Julia", "Ula", "Danka"]],
    ["Krzysztof", ["Tomek B", "Julia", "Paulina"]],
    ["Julia", ["Tomek B", "Paulina", "Krzysztof", "Ula"]],
    ["Ula", ["Oleg", "Iwona", "Janek", "Paulina", "Julia"]],
    ["Oleg", ["Ula", "Iwona", "Janek"]],
    ["Iwona", ["Janek", "Ula", "Oleg", "Paulina"]],
    ["Janek", ["Iwona", "Ula", "Oleg", "Paulina"]],
    ["Marek", ["Danka"]],
    ["Danka", ["Marek", "Julia", "Paulina"]],
    ["Andrzej", []],
    ["Tomek S", ["Kajka", "Maciej"]],
    ["Maciej", ["Kajka", "Tomek S"]],
    ["Kajka", ["Tomek S", "Maciej"]]
]

output = []

for i in data:
    ok = False
    while not ok:
        random_number = randint(0, len(data) - 1)
        check = True
        for j in output:
            if j[1] == data[random_number][0]:
                check = False
            if j[0] == data[random_number][0] and j[1] == i[0]:
                check = False

        if data[random_number][0] not in i[1] and data[random_number][0] != i[0] and check:
            output.append((i[0], data[random_number][0]))
            ok = True

for i in output:
    print(i[0], " ma ", i[1])