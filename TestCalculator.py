import random
import unittest
from operator import sub, mul, truediv,add,pow
import CalculatorOperator
import math


class TestStringMethods(unittest.TestCase):
    n1 = random.randint(1, 100)
    n2 = random.randint(1, 100)
    n3 = random.randint(-100, -1)

    def test_plus(self):
        self.assertEqual(CalculatorOperator.plus(self.n1,self.n2),add(self.n1,self.n2))
        self.assertEqual(CalculatorOperator.plus(self.n1,self.n3),add(self.n1,self.n3))

    def test_minus(self):
        self.assertEqual(CalculatorOperator.minus(self.n1, self.n2), sub(self.n1, self.n2))
        self.assertEqual(CalculatorOperator.minus(self.n1, self.n3), sub(self.n1, self.n3))

    def test_multiply(self):
        self.assertEqual(CalculatorOperator.multiply(self.n1, self.n2), mul(self.n1, self.n2))
        self.assertEqual(CalculatorOperator.multiply(self.n1, self.n3), mul(self.n1, self.n3))

    def test_divide(self):
        self.assertEqual(CalculatorOperator.divide(self.n1, self.n2), truediv(self.n1, self.n2))
        self.assertEqual(CalculatorOperator.divide(self.n1, self.n3), truediv(self.n1, self.n3))

    def test_power(self):
        self.assertEqual(CalculatorOperator.power(self.n1, self.n2), pow(self.n1, self.n2))
        self.assertEqual(CalculatorOperator.power(self.n1, self.n3), pow(self.n1, self.n3))
        self.assertEqual(CalculatorOperator.power(self.n3, self.n1), pow(self.n3, self.n1))

    def test_factorial(self):
        self.assertEqual(CalculatorOperator.factorial(self.n1), math.factorial(self.n1))

    def test_sqrt(self):
        self.assertEqual(CalculatorOperator.sqrt(self.n1), math.sqrt(self.n1))




    def test_plus_neg(self):
        self.assertEqual(CalculatorOperator.plus("abc",self.n2),"Вводите только числа")

    def test_minus_neg(self):
        self.assertEqual(CalculatorOperator.minus("abc", self.n2), "Вводите только числа")

    def test_multiply_neg(self):
        self.assertEqual(CalculatorOperator.multiply("abc", self.n2), "Вводите только числа")

    def test_divide_neg(self):
        self.assertEqual(CalculatorOperator.divide("abc", self.n2), "Вводите только числа")
        self.assertEqual(CalculatorOperator.divide(self.n1, 0), "Нельзя делить на 0")

    def test_power_neg(self):
        self.assertEqual(CalculatorOperator.power("abc", self.n2), "Вводите только числа")

    def test_factorial_neg(self):
        self.assertEqual(CalculatorOperator.factorial("abc"), "Вводите только числа")
        self.assertEqual(CalculatorOperator.factorial(-5), "Вводите в факториал положительные числа")
        self.assertEqual(CalculatorOperator.factorial(2.5), "Вводите в факториал целые числа")

    def test_sqrt_neg(self):
        self.assertEqual(CalculatorOperator.sqrt("abc"), "Вводите только числа")
        self.assertEqual(CalculatorOperator.sqrt(-5), "Вводите под корень положительные числа")




if __name__ == '__CalculatorOperator__':
    unittest.CalculatorOperator()
