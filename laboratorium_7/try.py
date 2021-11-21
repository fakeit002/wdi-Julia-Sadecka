
lista = ['a', 'b', 'c', 'd', ]
print(lista)
lista.append('e')
print(lista)
lista.insert(3, 'ojej')
print(lista)
lista.extend('e')
print(lista)
print(len(lista))
for i in lista:
    print(i)
x = 0
while x < len(lista):
    print(lista[x])
    x += 1