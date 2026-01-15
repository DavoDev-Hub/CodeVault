import unittest


class Calculator:
    """Clase simple para realizar operaciones matemáticas básicas."""
    
    def add(self, a, b):
        """Suma dos números."""
        return a + b
    
    def subtract(self, a, b):
        """Resta dos números."""
        return a - b
    
    def multiply(self, a, b):
        """Multiplica dos números."""
        return a * b
    
    def divide(self, a, b):
        """Divide dos números."""
        if b == 0:
            raise ValueError("No se puede dividir entre cero")
        return a / b


class TestCalculator(unittest.TestCase):
    """Tests para la clase Calculator."""
    
    def setUp(self):
        """Crea una instancia de Calculator para usar en los tests."""
        self.calc = Calculator()
    
    def test_add(self):
        """Verifica que la suma funcione correctamente."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
    
    def test_subtract(self):
        """Verifica que la resta funcione correctamente."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(10, 10), 0)
    
    def test_multiply(self):
        """Verifica que la multiplicación funcione correctamente."""
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
    
    def test_divide(self):
        """Verifica que la división funcione correctamente."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(9, 3), 3)
        self.assertAlmostEqual(self.calc.divide(5, 2), 2.5)
    
    def test_divide_by_zero(self):
        """Verifica que dividir por cero lance una excepción."""
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)


if __name__ == '__main__':
    unittest.main()
