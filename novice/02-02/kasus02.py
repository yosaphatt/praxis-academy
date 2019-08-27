import unittest


class TestSum(unittest.TestCase):

    def tambah(self):
        self.assertEqual(tambah([1, 2, 3]), 6, "Should be 6") #mengecek nilai apakah sama atau tidak

    def tambah_tuple(self): 
        self.assertEqual(tamabah((1, 2, 2)), 6, "Should be 6") #mengecek nilai apakah sama atau tidak

if __name__ == '__main__':
    unittest.main()