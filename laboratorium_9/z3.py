# Program wczytujący tablicę dwuwymiarową o ustalonym wymiarze n×n
# wypełnioną liczbami naturalnymi. Dla danej tablicy należy napisać funkcję,
# która odpowiada na pytanie, czy w tablicy istnieje wiersz,
# w którym każda liczba zawiera co najmniej jedną cyfrę będącą liczbą pierwszą.
# Wymiar tablicy powinien być definiowany przez użytkownika.


import random
n = int(input("Podaj liczbę która będzie wymiarem tablicy: "))
tab = []
tab2 = []
for i in range(n):
    for j in range(n):
        y = random.randint(1, 100)
        tab.append(y)
    tab2.append(tab)
    tab = []
print(tab2)


def checks(tab, n):
    primes = ['2', '3', '5', '7']
    for i in range(n):
        f = True  #flaga
        for j in range(n):
            f2 = False
            for k in str(tab[i][j]):
                # print(tab[i][j])
                if k in primes:
                    f2 = True
                    break
            if f2 is False:
                f = False
        if f is True:
            return True
    return False


print(checks(tab2, n))


# tab3 = [[1,2,3], [4,5,6], [7,8,9]]
tab4 = [[15,34,77], [111, 23, 66], [95, 11 ,234]]
# print(checks(tab3, len(tab3))
print(checks(tab4, len(tab4)))
