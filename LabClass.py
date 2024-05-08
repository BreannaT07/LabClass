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

# I was in a group with Antonio and we were able to discuss and understand how the code functions. We talk about our understandings on how the code, from 1 to 14, was able to define what the fractions were and how it set them up. 
# It was understandable until we had reached line 16 in our code, as it was confusing to read what that part of the code's function was and how it was supposed to be used in the code. 
