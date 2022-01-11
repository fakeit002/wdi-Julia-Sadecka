# Rozwiąż rekurencyjnie problem Wież Hanoi. Wskaż kolejne ruchy, które należy wykonać

def hanoi(n, left, middle, right):
    if n == 1:
        print(f'Przenieś krążek {n} z miejsca {left} do {right}')
    else:
        hanoi(n - 1, left, right, middle)
        print(f'Przenieś krążek {n} z miejsca {left} do {right}')
        hanoi(n - 1, middle, left, right)


hanoi(4, 'A', 'B', 'C')
