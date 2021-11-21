
lista = list(input("Wprowadź ciąg znaków: "))
x = lista.index('0')
lista.reverse()
y = lista.index('0')
z = len(lista)
lista.reverse()
lista2 = lista[(x + 1):(z - y - 1)]
print(lista2)

lista3 = []
for i in lista2:
    i = ord(i)
    lista3.append(i)

lista3.sort()
print(lista3)
print(lista3[4])

