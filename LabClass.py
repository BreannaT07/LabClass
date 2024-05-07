import math

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def show(self):
        print(f"{self.numerator}/{self.denominator}")

    def simplify(self):
        common_divisor = math.gcd(self.numerator, self.denominator)
        self.numerator = self.numerator // common_divisor
        self.denominator = self.denominator // common_divisor

    def add(self, other_fraction):
        new_numerator = self.numerator * other_fraction.denominator + self.denominator * other_fraction.numerator
        new_denominator = self.denominator * other_fraction.denominator
        result = Fraction(new_numerator, new_denominator)
        result.simplify()
        return result
    
def main():
    frac1 = Fraction(5, 6)
    frac2 = Fraction(4, 9)

    print("First fraction:")
    frac1.show()

    print("Second fraction:")
    frac2.show()

    print("Sum of fractions:")
    result = frac1.add(frac2)
    result.show()

if __name__ == "__main__":
    main()

#_#