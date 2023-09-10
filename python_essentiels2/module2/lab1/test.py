import unittest

def mysplit(strng):
    # Your mysplit() implementation here

class TestMySplit(unittest.TestCase):
    def test_comma_separated_string(self):
        self.assertEqual(mysplit("To be or not to be, that is the question"), 
                         ['To', 'be', 'or', 'not', 'to', 'be,', 'that', 'is', 'the', 'question'])

    def test_no_space_after_comma(self):
        self.assertEqual(mysplit("To be or not to be,that is the question"), 
                         ['To', 'be', 'or', 'not', 'to', 'be,that', 'is', 'the', 'question'])

    def test_only_spaces(self):
        self.assertEqual(mysplit("   "), [])

    def test_single_word_with_spaces(self):
        self.assertEqual(mysplit(" abc "), ['abc'])

    def test_empty_string(self):
        self.assertEqual(mysplit(""), [])

if __name__ == '__main__':
    unittest.main()
