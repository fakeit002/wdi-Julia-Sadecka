
def sum(n, m):
    x = []
    for i in range(len(n)):
        x.append([])
        for j in range(len(n[0])):
            x[i].append(n[i][j] + m[i][j])
        for i in range(len(x)):
            print(i, '\n')
    return x

def sub(n, m):
    x = []
    for i in range(len(n)):
        x.append([])
        for j in range(len(n[0])):
            x[i].append(n[i][j] - m[i][j])
    return x

def mult(n, m):
    x = []
    for i in range(len(n)):
        x.append([])
        for j in range(len(m[0])):
            x[i].append(0)
            for k in range(len(m)):
                x[i][j] += n[i][k] * m[k][j]
    return x

def scal(n, scalar):
    for i in range(len(n)):
        for j in range(len(n[0])):
            n[i][j] = n[i][j] * scalar
    return n

def comp(n, m):
    if len(n) == len(m) and len(n[0]) == len(m[0]):
        print('Suma macierzy: \n', sum(n, m), '\nRóżnica macierzy: \n', sub(n, m), '\n')
    else:
        print('Suma i różnica macierzy nie istnieje. Macierze muszą mieć wiersze i kolumny równej długości')
    if len(n[0]) == len(m):
        print('Iloczyn macierzy: \n', mult(n, m))
    else:
        print('Iloczyn macierzy nie istnieje. Pierwsza macierz musi mieć długość wiersza równą długości kolumny')
    print('Mnożenie przez skalar pierwszej macierzy: \n', scal(n, scalar), '\nMnożenie przez skalar drugiej macierzy: \n', scal(m, scalar))

m1 = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9],
      [1, 1, 1]]

m2 = [[1, 0, 2],
      [3, 1, 0],
      [0, 1, 1],
      [2, 0, 1]]

m3 = [[1, 2, 4, 0],
      [2, 1, 0, 1],
      [1, 0, 1, 2]]

m4 = [[1, 2, 3],
      [-1, 0, 1]]

m5 = [[1, 1, 0],
      [2, -1, 1],
      [3, 0, 0]]


scalar = int(input("Podaj skalar przez, który chcesz przemnożyć macierze:"))

print(comp(m1, m2))
