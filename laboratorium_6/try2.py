# czy liczba jest palindromem i palindromem w systemie dwójkowym

try:
    liczba = int(input("Podaj liczbę: "))
    # if liczba == 0:
    #     raise Exception("Liczba jest palindromem \nLiczba w postaci binarnej jest palindromem")
except ValueError:
    print("Ojj... Ta liczba nie jest naturalna, wprowadź liczbę naturalną")


# odwrócenie liczby
def odwrócenie(liczba):
    y = liczba
    odwr = 0
    while y > 0:
        x = y % 10
        odwr = odwr * 10 + x
        y = (y - x) / 10
        y = float(y)
    # print(odwr)
    return odwr


# zamiana na binarne
def binarne(liczba):
    a = int(liczba)
    liczba2 = ''
    while a > 0:
        liczba2 = str(a % 2) + liczba2
        a = int(a / 2)
    liczba2 = int(liczba2)
    print(liczba2)
    return liczba2


# sprawdzenie czy liczby są palindromami
if odwrócenie(abs(liczba)) == abs(liczba):
    print("Liczba jest palindromem")
else:
    print("Liczba nie jest palindromem")
# print(odwr)

if liczba < 0: # Zamienia liczby na U2
    liczba = str(binarne(abs(liczba)))
    print(liczba)
    liczba = '0' + liczba
    print(liczba)
    liczba = liczba.replace('1', '2').replace('0', '1').replace('2', '0')
    print(liczba)
    liczba = list(liczba)[::-1]
    print(liczba)

    for i in range(len(liczba)):
        liczba[i] = int(liczba[i])
    print(liczba)

    liczba[0] += 1
    print(liczba)
    for i in range(len(liczba)):
        if liczba[i] == 2:
            liczba[i] -= 2
            liczba[i + 1] += 1
            print(liczba)
    liczba = liczba[::-1]
    print(liczba)
    x = ''
    for i in liczba:
        i = str(i)
        x += f'{i}'
    liczba2 = x
    print(liczba)

if odwrócenie(binarne(liczba)) == binarne(liczba):
    print("Liczba w postaci binarnej jest palindromem")
else:
    print("Liczba w postaci binarnej nie jest palindromem")


