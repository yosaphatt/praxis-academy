import unittest

class MyTest(unittest.TestCase):

    def setUp(self):
        self.lst = ['1','2','4']

    def test_in_one(self):
        self.assertIn('1', self.lst)
        self.lst.remove('1')

    def test_in_two(self):
        self.assertIn('1', self.lst)


if __name__ == '__main__':
    unittest.main()