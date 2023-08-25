import unittest
from solution import Weeker, WeekDayError 

class TestWeeker(unittest.TestCase):
    def test_weeker_operations(self):
        weekday = Weeker('Mon')
        self.assertEqual(str(weekday), 'Mon')

        weekday.add_days(15)
        self.assertEqual(str(weekday), 'Tue')

        weekday.subtract_days(23)
        self.assertEqual(str(weekday), 'Sun')

    def test_invalid_day(self):
        with self.assertRaises(WeekDayError):
            Weeker('Monday')

if __name__ == '__main__':
    unittest.main()
