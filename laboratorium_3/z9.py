saldo = 2500
a = ("1")
b = ("2")
c = ("3")
x = int(input("Wprowadź PIN"))
if x != 1234:
    print("ZŁY PIN, MASZ JESZCZE JEDNĄ SZANSĘ, ALBO ŚRODKI Z TWOJEGO KONTA ZOSTANĄ SKASOWANE" )
elif x == 1234:
    d = input("Co chcesz zrobić? Wpłata-wprowadź '1'; Wypłata-wprowadź '2'; Sprawdź saldo-wprowadź '3' ")
    if d == c:
        print("Stan twoje konta to:")
        print(saldo)
    if d == a:
        e = int(input("Ile?"))
        print("Stan twojego konta to: ")
        saldo = saldo + e
        print(saldo+e)
    if d == b:
        f = int(input("Ile?"))
        if f>saldo:
            print("Kwota nie może być większa niż stan konta")
            y = input("Czy chcesz wypłacić mniejszą kwotę? [tak/nie]")
            if y == tak:






