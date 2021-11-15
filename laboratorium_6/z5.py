# czy liczba jest palindromem i palindromem w systemie dwójkowym

n = input("Podaj liczbę")
x = int(n) % 10
while x > 0:
    x = int(n) % 10
    n = (int(n) - x) / 10
    print(x)

