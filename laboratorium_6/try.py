liczba = int(input("Podaj liczbę: "))
if liczba == 0:
    print("Liczba jest palindromem \nLiczba w postaci binarnej jest palindromem")
else:
# odwrócenie liczby
    y = liczba
    # x = ''
    odwr = 0
    while y > 0:
        x = y % 10
        odwr = odwr * 10 + x
        y = (y - x) / 10
        y = float(y)
    # print(odwr)

# zamiana na binarne
    a = liczba
    liczba2 = ''
    while a > 0:
        liczba2 = str(a % 2) + liczba2
        a = int(a / 2)
    print(liczba2)
    liczba2 = int(liczba2)

# odwrócona liczba w postaci binarnej
    b = liczba2
    # x2 = ''
    odwr2 = 0
    while b > 0:
        x2 = b % 10
        odwr2 = odwr2 * 10 + x2
        b = (b - x2) / 10
        b = int(b)
    # print(odwr2)

# sprawdzenie czy liczby są palindromami
    if odwr == liczba:
        print("Liczba jest palindromem")
    else:
        print("Liczba nie jest palindromem")

    if odwr2 == liczba2:
        print("Liczba w postaci binarnej jest palindromem")
    else:
        print("Liczba w postaci binarnej nie jest palindromem")