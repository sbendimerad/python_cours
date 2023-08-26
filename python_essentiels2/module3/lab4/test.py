import unittest
from solution import Timer

class TestTimer(unittest.TestCase):
    def test_timer_operations(self):
        timer = Timer(23, 59, 59)
        self.assertEqual(str(timer), "23:59:59")

        timer.next_second()
        self.assertEqual(str(timer), "00:00:00")

        timer.prev_second()
        self.assertEqual(str(timer), "23:59:59")

        print("All tests passed!")

if __name__ == '__main__':
    unittest.main()
