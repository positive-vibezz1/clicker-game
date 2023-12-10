class Recursion:
    def __init__(self, base, exponent):
        self.base = base
        self.exponent = exponent

    def recursive_power(self, base, exponent):
        if exponent == 0:
            return 1
        else:
            return base * self.recursive_power(base, exponent - 1)