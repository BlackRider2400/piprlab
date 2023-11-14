def change_negative_to_zero(list):
    table = []
    for i in list:
        table.append(i if i > 0 else 0)
    return table


print(change_negative_to_zero([-1, 3, 5, -3, 0]))
