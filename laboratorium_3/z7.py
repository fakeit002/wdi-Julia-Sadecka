a = int(input("Podaj pierwszą liczbę "))
b = int(input("Podaj drugą liczbę "))
x = range(a, b + 1)

if len(x) > 20:
    y = ((a + b) * 0.5)
    if y - int(y) == 0:
        print(int(y - 3), int(y - 2), int(y - 1), int(y + 1), int(y + 2), int(y + 3))
    else:
        print(int(y - 2.5), int(y - 1.5), int(y - 0.5), int(y + 0.5), int(y + 1.5), int(y + 2.5))
    # nie wiem dlaczego ten kod nie działa
    # if type(y) == "<type 'int'>":
    #     print(y - 3, y - 2, y - 1, y + 1, y + 2, y + 3)
    # else:
    #     print(y - 2.5, y - 1.5, y - 0.5, y + 0.5, y + 1.5, y + 2.5)
else:
    for n in x:
        print(n)




