import program
import unittest

class TestSum(unittest.TestCase):
    def test_integer(self):
        self.assertEqual(program.addition(10, 5), 15)

if __name__ == '__main__':
    unittest.main()