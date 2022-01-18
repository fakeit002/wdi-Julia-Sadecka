# funkcja, która zwraca długość najdłuższego, spójnego podciągu rosnącego dla którego suma jego elementów
# jest równa sumie indeksów tych elementów. Do funkcji należy przekazać listę,
# funkcja powinna zwrócić długość znalezionego podciągu lub 0 jeżeli taki podciąg nie istnieje.

import pytest

list1 = [1, 1, 2, 1, 2, 3, 4]
# result1 = 2
list2 = [67, 34, 2, 5, 11, 10, 1, 5, 8, 10, 13, 14, 9, 90]
# result2 = 6
list3 = [1, 2, 3, 2, 1, 5, 6]
# result3 = 0
list4 = [1, 2, 3, 3, 4, 5, 1, 7, 8, 9, 15]  # 1+7+8+9+15=40, 6+7+8+9+10=40
# result4 = 5
list5 = [-2, 1, 2, 3, 4]


def compare(a):
    result = 0  # długość podciągu rosnącego maksymalnego
    length = 1  # długość podciągu
    total = a[0]  # suma elementów
    index = 0  # suma indeksów
    if type(a) != list:
        raise ValueError('Podaj listę!')
    for i in range(len(a) - 1):
        if a[i + 1] > a[i]:
            length += 1
            total += a[i + 1]
            index += i + 1
            if length > result and total == index:
                result = length
        elif a[i + 1] <= a[i]:
            length = 1
            total = a[i + 1]
            index = i + 1
    print("Result: " + str(result))
    return result


class TestZ6:

    def test_compare(self):
        a = [1, 1, 2, 1, 2, 3, 4]
        b = [67, 34, 2, 5, 11, 10, 1, 5, 8, 10, 13, 14, 9, 90]
        c = [1, 2, 3, 2, 1, 5, 6]
        assert compare(a) == 2
        assert compare(b) == 6
        assert compare(c) == 0
