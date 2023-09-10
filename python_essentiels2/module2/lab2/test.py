import unittest
from unittest.mock import patch
from solution import print_number

class TestPrintNumber(unittest.TestCase):

    @patch('builtins.input', side_effect=['123'])
    def test_print_number(self, mock_input):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_output:
            print_number()
            output = mock_output.getvalue()
            self.assertEqual(output.strip(), " #   #   # ")
            self.assertEqual(output.count('\n'), 4)

if __name__ == '__main__':
    unittest.main()
