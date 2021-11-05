a = int(input("Wprowadź liczbę: "))

print(((" ") * a) + ("X"))

for i in range(1, a):
    print((" " * (a - i)) + ("*" * ((2 * i) + 1)))

print(((" ") * a) + ("U"))

