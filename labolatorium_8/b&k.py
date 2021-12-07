# funkcja, która zwraca długość najdłuższego, spójnego podciągu rosnącego dla którego suma jego elementów
# jest równa sumie indeksów tych elementów. Do funkcji należy przekazać listę,
# funkcja powinna zwrócić długość znalezionego podciągu lub 0 jeżeli taki podciąg nie istnieje.


def sums(lista):
    mx = 0
    length = 0
    suma = 0
    for i in range(len(lista)):
        suma = 0
        for j in range(i, len(lista)):
            suma += lista[j]
            if lista[j] < lista[j-1] and j > i:
                break
            if suma == sum(range(i,j+1)):
                length = j+1-i
                if length > mx:
                    mx = length
    return mx


tab = [0,1,2,3,4,5,3,4,22,1]
tab2 = [-1, 2, 1231312, -5, 6, 11]
list5 = [-2, 1, 2, 3, 4]
# 0, 1, 3, 6, 10, 15, 21,
print(sums(tab))
print(sums(tab2))
print(sums(list5))