# Program, który umożliwia wykonywanie operacji na 2. dowolnych macierzach o wymiarach N×M:
# dodawanie, odejmowanie, mnożenie przez siebie, mnożenie przez skalar.
# Macierze należy pobrać z pliku i zapisać do osobnego pliku wszystkie wyniki działań w taki sposób,
# żeby to było czytelne dla człowieka. Należy obsłużyć niezbędne wyjątki, np. niezgodność wymiarów.

with open("matrix2.txt", "r") as plik:
    matrix = []
    for line in plik:
        a = plik.readline().split()
        for i in range(len(a)):
            a[i] = int(a[i])
        matrix.append(a)

    y = matrix.index([0])
    matrix1 = matrix[0:y]
    matrix2 = matrix[y + 1:]
    print(matrix1)
    print(matrix2)


def sum(n, m):
    x = []
    for i in range(len(n)):
        x.append([])
        for j in range(len(n[0])):
            x[i].append(n[i][j] + m[i][j])
    x = str(x)
    return x


def sub(n, m):
    x = []
    for i in range(len(n)):
        x.append([])
        for j in range(len(n[0])):
            x[i].append(n[i][j] - m[i][j])
    x = str(x)
    return x


def mult(n, m):
    x = []
    for i in range(len(n)):
        x.append([])
        for j in range(len(m[0])):
            x[i].append(0)
            for k in range(len(m)):
                x[i][j] += n[i][k] * m[k][j]
    x = str(x)
    return x


# def scal(n, scalar):
#     for i in range(len(n)):
#         for j in range(len(n[0])):
#             n[i][j] = n[i][j] * scalar
#     n = str(n)
#     return n

# scalar = int(input("Podaj skalar przez, który chcesz przemnożyć macierze:"))


with open('results.txt', 'w') as result:
    try:
        if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
            raise RuntimeError
        result.write('Suma macierzy: \n')
        result.write(sum(matrix1, matrix2))
        result.write('\n\nRoznica macierzy: \n')
        result.write(sub(matrix1, matrix2))
    except RuntimeError:
        result.write('Suma i roznica macierzy nie istnieje. Macierze musza miec wiersze i kolumny rownej dlugosci \n\n')

    try:
        if len(matrix1[0]) != len(matrix2):
            raise ValueError
        result.write('Iloczyn macierzy: \n')
        result.write(mult(matrix1, matrix2))
    except ValueError:
        result.write('\nIloczyn macierzy nie istnieje. Pierwsza macierz musi miec dlugosc wiersza rowną dlugosci kolumny drugiej\n\n')

    # result.write('\n\nWynik mnozenie przez skalar pierwszej macierzy: \n')
    # result.write(scal(matrix1, scalar))
    # result.write('\n\nWynik mnozenie przez skalar drugiej macierzy: \n')
    # result.write(scal(matrix2, scalar))

