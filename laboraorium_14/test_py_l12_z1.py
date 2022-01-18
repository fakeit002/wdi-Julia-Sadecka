# Liczby wymierne są reprezentowane przez krotkę (l,m).
# Gdzie: l – liczba całkowita oznaczająca licznik, m – liczba naturalna oznaczająca mianownik.
# Proszę napisać funkcję wykonujące podstawowe operacje na ułamkach,
# m. in. dodawanie, odejmowanie, mnożenie, dzielenie, potęgowanie, skracanie, wypisywanie i wczytywanie.
# Test: Używając tych funkcji proszę napisać funkcję rozwiązującą układ 2 równań z 2 niewiadomymi.

import math


class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def write(self):
        return self

    def reduce(self):
        x = math.gcd(self.numerator, self.denominator)
        self.numerator //= x
        self.denominator //= x
        return self

    def addition(self, f):
        num1 = self.numerator * f.denominator
        num2 = f.numerator * self.denominator
        den = self.denominator * f.denominator
        result = Fraction(num1 + num2, den)
        result.reduce()
        return result

    def subtraction(self, f):
        num1 = self.numerator * f.denominator
        num2 = f.numerator * self.denominator
        den = self.denominator * f.denominator
        result = Fraction(num1 - num2, den)
        result.reduce()
        return result

    def multiplication(self, f):
        result = Fraction(self.numerator * f.numerator, self.denominator * f.denominator)
        result.reduce()
        return result

    def division(self, f):
        num = self.numerator * f.denominator
        den = self.denominator * f.numerator
        if den < 0:
            num = -num
            den = -den
        result = Fraction(num, den)
        result.reduce()
        return result


class TestZ1:
    def test_reduce(self):
        a = Fraction(5 ,25)
        assert a.reduce().numerator == 1
        assert a.reduce().denominator == 5

    def test_addition(self):
        b = Fraction(4, 5)
        c = Fraction(3, 10)
        assert b.addition(c).numerator == 11
        assert b.addition(c).denominator == 10


def main():
    # zmienne
    num01 = input('(Liczba przy pierwszym x) \nWprowadź licznik i mianownik oddzielone spacjami pierwszego ułamka: ')
    num02 = input('(Liczba przy pierwszym y) \nWprowadź licznik i mianownik oddzielone spacjami drugiego ułamka: ')
    num03 = input('Wprowadź licznik i mianownik wynik pierwszego równania: ')
    num04 = input('Wprowadź licznik i mianownik liczby przy drugim x: ')
    num05 = input('Wprowadź licznik i mianownik liczby przy drugim y: ')
    num06 = input('Wprowadź licznik i mianownik wyniku drugiego równania: ')
    tup01 = num01.split()
    tup02 = num02.split()
    tup03 = num03.split()
    tup04 = num04.split()
    tup05 = num05.split()
    tup06 = num06.split()
    f01 = Fraction(int(tup01[0]), int(tup01[1]))
    f02 = Fraction(int(tup02[0]), int(tup02[1]))
    f03 = Fraction(int(tup03[0]), int(tup03[1]))
    f04 = Fraction(int(tup04[0]), int(tup04[1]))
    f05 = Fraction(int(tup05[0]), int(tup05[1]))
    f06 = Fraction(int(tup06[0]), int(tup06[1]))

    # funkcje dla f01 i f02
    add = Fraction.addition(f01, f02)
    sub = Fraction.subtraction(f01, f02)
    mult = Fraction.multiplication(f01, f02)
    div = Fraction.division(f01, f02)
    red1 = Fraction.reduce(f01)
    red2 = Fraction.reduce(f02)

    # Wyniki działań
    print(f'\nSkrócone ułamki: \nPierwszy: {red1.numerator}/{red1.denominator}\nDrugi: {red2.numerator}/{red2.denominator}')
    print(f'\nWynik dodawania to: {add.numerator}/{add.denominator}')
    print(f'Wynik odejmowania to: {sub.numerator}/{sub.denominator}')
    print(f'Wynik mnożenia to: {mult.numerator}/{mult.denominator}')
    print(f'Wynik dzielenia to: {div.numerator}/{div.denominator}')

    # rozwiązanie równania metodą wyznaczników
    w = Fraction.subtraction(Fraction.multiplication(f01, f05), Fraction.multiplication(f04, f02))
    wx = Fraction.subtraction(Fraction.multiplication(f03, f05), Fraction.multiplication(f06, f02))
    wy = Fraction.subtraction(Fraction.multiplication(f01, f06), Fraction.multiplication(f04, f03))
    x = Fraction.division(wx, w)
    y = Fraction.division(wy, w)
    print(f'\nx to: {x.numerator}/{x.denominator}')
    print(f'y to: {y.numerator}/{y.denominator}')
    # Dla liczb( 1 5, 6 8, 5 4, -1 5, 3 4, 4 16)
    # Wyniki powinny być: (1/5, 3/4, 19/20, -11/20, 3/20, 4/15, 5/2, 1)


if __name__ == "__main__":
    main()