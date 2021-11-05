# saldo początkowe to: 2500
# PIN to: 1234

saldo = 2500
a = ("1")
b = ("2")
c = ("3")
h = 1
while h == 1:
    x = int(input("Wprowadź PIN "))
# błędny PIN
    while x != 1234:
        x = int(input("Zły PIN, wprowadź dobry PIN "))
# poprawny PIN
    if x == 1234:
        d = input("Co chcesz zrobić? Wpłata-wprowadź '1'; Wypłata-wprowadź '2'; Sprawdź saldo-wprowadź '3' ")
# stan konta
        if d == c:
            print("Stan twojego konta to: " + str(saldo))
# wpłata
        if d == a:
            e = float(input("Ile? Wpisz kwotę: "))
            saldo = saldo + e
            print("Stan twojego konta to: " + str(saldo))
# wypłata
        if d == b:
            f = float(input("Ile? Wpisz kwotę: "))
            while f > saldo:
                f = float(input("Kwota nie może być większa niż stan konta. Jeśli chcesz wypłacić mniejszą kwotę - wpisz ją, jeśli chcesz zrobić coś innego wpisz '0'"))
                if f == 0:
                    print(".")
                elif f <= saldo:
                    saldo = saldo - f
                    print("Stan twojego konta to: " + str(saldo))
    h = int(input("Czy chcesz coś jeszcze zrobić?: '1' - tak, '2' - nie "))
    if h == 2:
        print("Dziękujemy i zapraszamy ponownie")




