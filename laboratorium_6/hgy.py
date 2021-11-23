
liczba = '1001000'
print(liczba)
liczba = '0' + liczba
print(liczba)
liczba = liczba.replace('1', '2').replace('0', '1').replace('2', '0')
print(liczba)
liczba = list(liczba)[::-1]
print(liczba)
for i in range(len(liczba)):
    liczba[i] = int(liczba[i])
print(liczba)
liczba[0] += 1
print(liczba)
for i in range(len(liczba)):
    if liczba[i] == 2:
        liczba[i] -= 2
        liczba[i + 1] += 1
        print(liczba)
liczba = liczba[::-1]
print(liczba)
x = ''
for i in liczba:
    i = str(i)
    x += f'{i}'
liczba = x
print(liczba)
print(type(liczba))
if liczba == liczba[::-1]:
    print('palindrom!!!')