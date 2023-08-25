import unittest
from solution import Point 

class TestPoint(unittest.TestCase):
    def test_distance_from_xy(self):
        point1 = Point(0, 0)
        self.assertAlmostEqual(point1.distance_from_xy(2, 0), 2.0)
        print("distance_from_xy test passed.")

    def test_distance_from_point(self):
        point1 = Point(0, 0)
        point2 = Point(1, 1)
        self.assertAlmostEqual(point1.distance_from_point(point2), 1.4142135623730951)
        print("distance_from_point test passed.")

if __name__ == '__main__':
    unittest.main()
