# Krzysztof Barałkiewicz
# exercise 1
def create_dictionary(word):
    dictionary = {}
    for i in word:
        if i in dictionary:
            dictionary[i] = dictionary[i] + 1
        else:
            dictionary[i] = 1

    return dictionary


# exercise 2
def remove_special_words(sentence, letter):
    array = sentence.split(" ")
    result = ""
    for i in array:
        if not i.count(letter[0]) >= letter[1]:
            result = result + i + " "
    return result


# exercise 3
def remove_special_words_with_special_letters(sentence, letters):
    array = sentence.split(" ")
    result = ""
    for i in array:
        found = False
        for j in letters:
            if i.count(j[0]) >= j[1]:
                found = True
        if not found:
            result = result + i + " "
    return result


print(create_dictionary("kukułka"))

print(remove_special_words("Alice in wonderland went into a deep coma.", ("e", 2)))

print(remove_special_words_with_special_letters("I literally can't deal with this drama right now.", [("a", 2), ("l", 3)]))
