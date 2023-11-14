def change_to_list(data):
    output = []
    for i in data:
        for j in i:
            output.append(j)
    return output


print(change_to_list([(1, 4), (8, 5), (20, 69)]))
