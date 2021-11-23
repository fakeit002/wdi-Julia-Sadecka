# czy liczba jest palindromem i palindromem w systemie dwójkowym

try:
    liczba = int(input("Podaj liczbę: "))
    if liczba == 0:
        print("Liczba jest palindromem \nLiczba w postaci binarnej jest palindromem")
    else:
# odwrócenie liczby
        def odwrócenie(liczba):
            y = liczba
            odwr = 0
            while y > 0:
                x = y % 10
                odwr = odwr * 10 + x
                y = (y - x) / 10
                y = float(y)
            print(odwr)
            return odwr
        odwrócenie(liczba)
# sprawdzenie czy liczby są palindromami
        if odwrócenie(liczba) == liczba:
            print("Liczba jest palindromem")
        else:
            print("Liczba nie jest palindromem")
        # print(odwr)

# zamiana na binarne
        a = liczba
        liczba2 = ''
        while a > 0:
            liczba2 = str(a % 2) + liczba2
            a = int(a / 2)
        print(liczba2)
        liczba2 = int(liczba2)

        odwrócenie(liczba2)

        if odwrócenie(liczba2) == liczba2:
            print("Liczba w postaci binarnej jest palindromem")
        else:
            print("Liczba w postaci binarnej nie jest palindromem")
except ValueError:
    print("Ojj... Ta liczba nie jest naturalna, wprowadź liczbę naturalną")
