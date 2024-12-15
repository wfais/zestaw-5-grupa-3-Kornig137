from fractions import Fraction
from functools import reduce
from math import gcd

def fracMultiplication(a: Fraction, b: Fraction):
    num = a.numerator * b.numerator
    den = a.denominator * b.denominator
    greatestCommDiv = gcd(num, den)
    if greatestCommDiv != 1:
        num //= greatestCommDiv
        den //= greatestCommDiv
        
    return Fraction(num, den)

def product(fracs):
    t = reduce(fracMultiplication, fracs)
    return t.numerator, t.denominator


if __name__ == "__main__":
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)
