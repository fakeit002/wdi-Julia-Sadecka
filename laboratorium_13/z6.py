tab = []
def pascal(n):
    if n == 1:
        tab.append(1)
    else:
        tab.append(1, pascal(n-1 + tab[0]))

pascal(3, 3)
