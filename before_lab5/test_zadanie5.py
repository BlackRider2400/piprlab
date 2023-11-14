from zadanie5 import count_element_above_average


def test_default_input():
    data = [[1, 2, 3], [5, 6, 7], [], [3, 4, 5], ["12a", 1, 4]]
    assert count_element_above_average(data) == [1, 1, "DZIELENIE PRZEZ ZERO", 1, "ZŁA WARTOŚĆ"]


def test_standard_input():
    data = [[1, 2, 3], [1, 2, 3, 4, 5, 6, 7], [1, 4, 5, 5], [10, 40, 80, 100], [1, 1, 1]]
    assert count_element_above_average(data) == [1, 3, 3, 2, 0]


def test_empty_input():
    data = [[]]
    assert count_element_above_average(data) == ["DZIELENIE PRZEZ ZERO"]


def test_wrong_input():
    data = [["12a", 1, 4]]
    assert count_element_above_average(data) == ["ZŁA WARTOŚĆ"]