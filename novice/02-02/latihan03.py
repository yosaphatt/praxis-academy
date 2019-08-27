import unittest

class MyTest(unittest.TestCase):

    def setUp(self):
        self.lst = ['1','2','4']

    def test_in_one(self):
        self.assertIn('2', self.lst)
        self.lst.remove('2')

    def test_in_two(self):
        self.lst.remove('2')
        self.assertIn('2', self.lst)
        
if __name__ == '__main__':
    unittest.main()

    #=============ERROOR++++++++++++++