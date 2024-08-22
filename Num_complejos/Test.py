import unittest
import Complejos as lc

class TestStringMethods(unittest.TestCase):

    def test_Suma(self):
        self.assertEqual(lc.Suma((1, 2), (3, 4)), (4, 6))
        self.assertEqual(lc.Suma((-1, -2), (3, 4)), (2, 2))

    def test_Producto(self):
        self.assertEqual(lc.Producto((1, 2), (3, 4)), (-5, 10))
        self.assertEqual(lc.Producto((-1, -2), (3, 4)), (5, -10))

    def test_Resta(self):
        self.assertEqual(lc.Resta((1, 2), (3, 4)), (-2, -2))
        self.assertEqual(lc.Resta((-1, -2), (3, 4)), (-4, -6))

    def test_Division(self):
        self.assertEqual(lc.Division((1, 2), (3, 4)), (0.44, 0.08))
        self.assertEqual(lc.Division((-1, -2), (3, 4)), (-0.44, -0.08))

    def test_Modulo(self):
        self.assertEqual(lc.Modulo((2, 2)), 2.83)
        self.assertEqual(lc.Modulo((10, 10)), 14.14)

    def test_Conjugado(self):
        self.assertEqual(lc.Conjugado((1, 5)), (1, -5))
        self.assertEqual(lc.Conjugado((4, -9)), (4, 9))

    def test_Fase(self):
        self.assertEqual(lc.Fase((5, 5)), 0.79)
        self.assertEqual(lc.Fase((0, 8)), 1.57)
        
    def test_Car_Polar(self):
        result1 = lc.Car_Polar((1, 1))
        self.assertAlmostEqual(result1[0], 1.41, delta=0.01)
        self.assertAlmostEqual(result1[1], 0.79, delta=0.01)

        result2 = lc.Car_Polar((5, 0))
        self.assertAlmostEqual(result2[0], 5.0, delta=0.01)
        self.assertAlmostEqual(result2[1], 0.0, delta=0.01)

    def test_Polar_Car(self):
        result1 = lc.Polar_Car([1.41, 0.79])
        self.assertAlmostEqual(result1[0], 1.0, delta=0.02)
        self.assertAlmostEqual(result1[1], 1.0, delta=0.02)

        result2 = lc.Polar_Car([5.0, 0.0])
        self.assertAlmostEqual(result2[0], 5.0, delta=0.02)
        self.assertAlmostEqual(result2[1], 0.0, delta=0.02)

if __name__ == '__main__':
    unittest.main()

