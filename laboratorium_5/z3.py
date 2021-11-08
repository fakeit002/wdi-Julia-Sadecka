# wyznaczenie pierwiastka kwadratowego ze wzoru Newtona
y = 0.0000000001
x = float(input("Wprowadź liczbę, której pierwiastek chcesz poznać: "))

if x < 0:
    print("Nie można wyznaczyć pierwiastka z liczby ujemnej")

elif x == 0:
    print(int(0))

else:
    a = 1
    b = x
    while abs(a - b) >= y:
        # print(a, b)
        a = (a + b) * 0.5
        b = x / a
    print(a)
