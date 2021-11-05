a = int(input("Podaj pierwszą liczbę "))
b = int(input("Podaj drugą liczbę "))
x = range(a, b + 1)
if len(x) > 20:
    y = ((a + b) * 0.5)
    if str(type(y)) == "<class 'int'>":
        print(y)
    else:
        print(y + 1)
else:
    for n in x:
        print(n)

# for n in x:
#     print(n)
# x = 2
# print(type(x))
# a = 3
# b = 3.5


