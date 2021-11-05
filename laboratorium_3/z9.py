# saldo początkowe to: 2500
# PIN to: 1234

saldo = 2500
a = ("1")
b = ("2")
c = ("3")
h = 1
while h == 1:
    x = int(input("Wprowadź PIN "))
    while x != 1234:
        x = int(input("Zły PIN, wprowadź dobry PIN" ))
    if x == 1234:
        d = input("Co chcesz zrobić? Wpłata-wprowadź '1'; Wypłata-wprowadź '2'; Sprawdź saldo-wprowadź '3' ")
        if d == c:
            print("Stan twojego konta to: " + str(saldo))
        if d == a:
            e = int(input("Ile? Wpisz kwotę: "))
            saldo = saldo + e
            print("Stan twojego konta to: " + str(saldo))
        if d == b:
            f = int(input("Ile? Wpisz kwotę: "))
            while f > saldo:
                f = int(input("Kwota nie może być większa niż stan konta. Jeśli chcesz wypłacić mniejszą kwotę - wpisz ją, jeśli chcesz zrobić coś innego wpisz '0'"))
                if f == 0:
                    print(".")
                elif f <= saldo:
                    saldo = saldo - f
                    print("Stan twojego konta to: " + str(saldo))
    h = int(input("Czy chcesz coś jeszcze zrobić?: '1' - tak, '2' - nie "))
    if h == 2:
        print("Dziękujemy i zapraszamy ponownie")




