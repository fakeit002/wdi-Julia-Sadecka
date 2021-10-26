saldo = 250000000000
a = ("Wpłata")
b = ("Wypłata")
c = ("Sprawdź saldo" or "sprawdź saldo")
x = int(input("Wpisz PIN"))
if x != 1234:
    print("ZŁY PIN, MASZ JESZCZE JEDNĄ SZANSĘ, ALBO ŚRODKI Z TWOJEGO KONTA ZOSTANĄ SKASOWANE" )
elif x == 1234:
    d = input("Co chcesz zrobić? Wpłata Wypłata Sprawdź saldo ")
    if d == c:
        print(saldo)
    if d == a:
        e = int(input("Ile?"))
        print(saldo + e)




