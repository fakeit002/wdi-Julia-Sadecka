
import math


class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def write(self):
        return self

    def reduce(self):
        x = math.gcd(self.numerator, self.denominator)
        print(x)
        self.numerator //= x
        self.denominator //= x


n1 = Fraction(1, 2)
Fraction.reduce(n1)
