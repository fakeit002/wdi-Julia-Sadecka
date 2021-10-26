a = float(input("Podaj pierwszą liczbę "))
b = float(input("Podaj drugą liczbę "))
# gdy któraś liczba jest mniejsza od zera
if a < 0 and b < 0:
    print("Koniec programu, obie liczby ujemne")
    exit()()
# jeżeli liczba jest mniejsza od 0
if a < 0:
    a = abs(a)
if b < 0:
    b = abs(b)
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**2)
print(b**2)
print(a**0.5)
print(b**0.5)
if a*b == 10:
    print("Yay!")
''' bardzo się cieszę, że 
działa '''
