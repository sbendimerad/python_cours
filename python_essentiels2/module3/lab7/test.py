import unittest
from solution import Point, Triangle  # Replace 'your_source_code' with your actual module name

class TestTriangle(unittest.TestCase):
    def test_perimeter(self):
        triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
        self.assertAlmostEqual(triangle.perimeter(), 3.414213562373095)
        print("Perimeter test passed.")

if __name__ == '__main__':
    unittest.main()
