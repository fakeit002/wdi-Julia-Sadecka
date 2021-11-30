# funkcja, która zwraca długość najdłuższego, spójnego podciągu rosnącego dla którego suma jego elementów
# jest równa sumie indeksów tych elementów. Do funkcji należy przekazać listę,
# funkcja powinna zwrócić długość znalezionego podciągu lub 0 jeżeli taki podciąg nie istnieje.
list1 = [1, 1, 2, 1, 2, 3, 4]
# result1 = 2
list2 = [67, 34, 2, 5, 11, 10, 1, 5, 8, 10, 13, 14, 9, 90]
# result2 = 6
list3 = [1, 2, 3, 2, 1, 5, 6]# - suma-15, index-15, max-3
# result3 = 0
list4 = [1, 2, 3, 3, 4, 5, 1, 7, 8, 9, 15]# - suma-34, index-34, max-4
# result4 = 3

def compare(a):
    result = 0
    length = 1
    suma = 0
    index = 0
    for i in range(len(a) - 1):
        print('i', i)
        if a[i + 1] > a[i]:
            length += 1
            print('length', length)
            suma += a[i + 1]
            print('suma', suma)
            index += i + 1
            print('index', index)
            if length > result and suma == index:
                result = length
                print('result', result)
        elif a[i + 1] <= a[i]:
            length = 1
            suma = a[i + 1]
            index = i + 1
    print(result)
    print("Result: " + str(result))


# compare(list1)
# compare(list2)
# compare(list3)
compare(list4)
