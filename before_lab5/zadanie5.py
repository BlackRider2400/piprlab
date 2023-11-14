def count_element_above_average(data):
    output = []
    for i in data:
        elements_sum = 0
        elements_count = 0
        average = 0
        count_above_average = 0
        try:
            for j in i:
                j = int(j)
                elements_sum = elements_sum + j
                elements_count = elements_count + 1
            average = int(elements_sum / elements_count)
            for j in i:
                if j > average:
                    count_above_average = count_above_average + 1
            output.append(count_above_average)
        except ValueError:
            output.append("ZŁA WARTOŚĆ")
        except ZeroDivisionError:
            output.append("DZIELENIE PRZEZ ZERO")

    return output