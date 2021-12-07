

def checks(matrix, n):
    primes = ['2', '3', '5', '7']
    for i in range(n):
        f = True
        for j in range(n):
            f2 = False
            for k in str(matrix[i][j]):
                if k in primes:
                    f2 = True
            if not f2:
                f = False
        if f:
            return True
    return False


tab = [[1,2,3], [4,5,6], [7,8,9]]
tab2 = [[15,34,77], [111, 23, 66], [95, 11 ,234]]
print(checks(tab, len(tab)))
print(checks(tab2, len(tab2)))