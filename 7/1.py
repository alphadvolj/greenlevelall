class Polynomial:
    def __init__(self, coefficients):
        self._coefficients = coefficients

    @property
    def degree(self):
        return len(self._coefficients) - 1

    def __repr__(self):
        terms = []
        for power, coeff in enumerate(self._coefficients):
            if coeff != 0:
                if power == 0:
                    terms.append(f"{coeff}")
                elif power == 1:
                    terms.append(f"{coeff}x")
                else:
                    terms.append(f"{coeff}x^{power}")
        return " + ".join(reversed(terms)) if terms else "0"

    def __call__(self, x):
        return sum(coeff * (x ** power) for power, coeff in enumerate(self._coefficients))

    def __add__(self, other):
        if not isinstance(other, Polynomial):
            return NotImplemented
        new_coefficients = [
            a + b for a, b in zip(self._coefficients, other._coefficients)
        ]
        new_coefficients += self._coefficients[len(new_coefficients):] + other._coefficients[len(new_coefficients):]
        return Polynomial(new_coefficients)

    def __sub__(self, other):
        if not isinstance(other, Polynomial):
            return NotImplemented
        new_coefficients = [
            a - b for a, b in zip(self._coefficients, other._coefficients)
        ]
        new_coefficients += self._coefficients[len(new_coefficients):] + [-b for b in other._coefficients[len(new_coefficients):]]
        return Polynomial(new_coefficients)

    def __mul__(self, other):
        if not isinstance(other, Polynomial):
            return NotImplemented
        new_degree = self.degree + other.degree
        new_coefficients = [0] * (new_degree + 1)
        for i, a in enumerate(self._coefficients):
            for j, b in enumerate(other._coefficients):
                new_coefficients[i + j] += a * b
        return Polynomial(new_coefficients)

    def derivative(self):
        new_coefficients = [coeff * power for power, coeff in enumerate(self._coefficients)][1:]
        return Polynomial(new_coefficients)

    def evaluate(self, x):
        return self(x)


class QuadraticPolynomial(Polynomial):
    def __init__(self, coefficients):
        if len(coefficients) != 3:
            raise ValueError("Квадратичный полином должен иметь ровно 3 коэффициента.")
        super().__init__(coefficients)

    def discriminant(self):
        a = self._coefficients[2]
        b = self._coefficients[1]
        c = self._coefficients[0]
        return b ** 2 - 4 * a * c

    def find_roots(self):
        a = self._coefficients[2]
        b = self._coefficients[1]
        c = self._coefficients[0]
        d = self.discriminant()
        if d < 0:
            return []
        elif d == 0:
            return [-b / (2 * a)]
        else:
            return [(-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)]


p1 = Polynomial([1, 2, 3])
p2 = Polynomial([0, -1, 1])

print("P1:", p1)
print("P2:", p2)
print("P1 + P2:", p1 + p2)
print("P1 - P2:", p1 - p2)
print("P1 * P2:", p1 * p2)
print("P1(2):", p1(2))
print("P1 derivative:", p1.derivative())

q = QuadraticPolynomial([1, -3, 2])
print("Quadratic Polynomial:", q)
print("Discriminant:", q.discriminant())
print("Roots:", q.find_roots())