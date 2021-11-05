# Kalkulator
import random
x = 't'
while x == 't':
    a = int(input("Podaj pierwszą liczbę: "))
    b = int(input("Podaj drugą liczbę: "))
    c = input("Podaj znak działania: ")
    if c == '+':
        d = a + b
    elif c == '-':
        d = a - b
    elif c == '/':
        if b == 0:
            print("error, nie można dzielić przez 0")
            d = ' '
        else:
            d = a/b
    elif c == '*':
        d = a * b
    elif c == '**':
        d = a ** b
    elif c == '^':
        d = a ** (1 / b)
    elif c == 'x':
        if a > b:
            print("Pierwsza liczba musi być mniejsza od drugiej")
            d = ' '
        else:
            d = {random.randint(a, b)}

    print(d)
    x = input("Czy chcesz wprowadzić inne dane? 't' - tak, 'n' - nie: ")
    if x == 'n':
        break




